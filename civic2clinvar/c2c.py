from civicpy import civic
import csv
import logging


CLINVAR_FIELDS = [
    '##Local ID',
    'Gene symbol',
    'Reference sequence',
    'HGVS',
    'Chromosome',
    'Start',
    'Stop',
    'Reference allele',
    'Alternate allele',
    'Variation identifiers',
    'Alternate designations',
    'URL',
    'Condition ID type',
    'Condition ID value',
    'Preferred condition name',
    'Condition category',
    'Condition comment',
    'Clinical significance',
    'Clinical significance citation',
    'Citations or URLs for clinical significance without database identifiers',
    'Comment on clinical significance',
    'Explanation if clinical significance is other or drug response',
    'Collection method',
    'Allele origin',
    'Affected status',
    'Comment',
    'Private comment',
    'ClinVarAccession'
]


def assertions_to_clinvar_csv(assertion_ids, file, **kwargs):

    assertions = civic.get_assertions_by_ids(assertion_ids)
    with file as f:
        writer = csv.DictWriter(f, CLINVAR_FIELDS)
        writer.writeheader()
        for assertion in assertions:
            if assertion.status != 'accepted':
                logging.warning(f'Skipping {assertion.status} assertion AID:{assertion.id}.')
                continue
            variant = assertion.variant
            record = dict()
            record['##Local ID'] = f'AID:{assertion.id}'
            record['Gene symbol'] = assertion.gene.name
            rt = variant.coordinates.representative_transcript
            record['Reference sequence'] = rt
            matches = [x for x in variant.hgvs_expressions if x.startswith(rt)]
            if matches:
                record['HGVS'] = matches[0]
            record['Chromosome'] = variant.coordinates.chromosome
            record['Start'] = variant.coordinates.start
            record['Stop'] = variant.coordinates.stop
            record['Reference allele'] = variant.coordinates.reference_bases
            record['Alternate allele'] = variant.coordinates.variant_bases
            var_ids = [f'VariationID:{x}' for x in variant.clinvar_entries]
            record['Variation identifiers'] = \
                ';'.join(var_ids)
            record['Alternate designations'] = \
                '|'.join([variant.name] + variant.aliases)
            record['URL'] = variant.site_link
            if assertion.hpo_ids:
                record['Condition ID type'] = 'HPO'
                record['Condition ID value'] = ';'.join(assertion.hpo_ids)
            disease = assertion.disease.name
            if assertion.disease.doid:
                disease = f'{disease} (DOID:{assertion.disease.doid})'
            record['Preferred condition name'] = disease
            et = assertion.evidence_type.lower()
            if et == 'predictive':
                record['Condition category'] = 'drug response'
                record['Clinical significance'] = 'drug response'
            elif et in ['diagnostic', 'prognostic']:
                record['Condition category'] = 'finding'
                record['Clinical significance'] = 'other'
            else:
                msg = f'No routine for exporting {et} assertions at this time. Skipping AID:{assertion.id}.'
                logging.warning(msg)
                continue
            record['Condition comment'] = kwargs.get('condition_comment', '')  # TODO: Resolve what is expected here
            record['Clinical significance citation'] = ';'.join(variant.source_ids)
            record['Citations or URLs for clinical significance without database identifiers'] = '|'.join(
                [x.site_link for x in variant.evidence_items])
            record['Comment on clinical significance'] = assertion.summary
            record['Explanation if clinical significance is other or drug response'] = \
                ' '.join([assertion.evidence_direction, assertion.clinical_significance])
            record['Collection method'] = 'literature only'
            vo = assertion.variant_origin
            if vo:
                record['Allele origin'] = vo
            else:
                s = {x.variant_origin for x in assertion.evidence}
                if len(s) == 1:
                    record['Allele origin'] = s.pop()
                else:
                    record['Allele origin'] = ''
            record['Affected status'] = 'unknown'
            record['Comment'] = kwargs.get('comment', '')
            record['Private comment'] = kwargs.get('private_comment', '')
            record['ClinVarAccession'] = kwargs.get('clinvar_accession', '')
            writer.writerow(record)
