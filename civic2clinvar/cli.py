import click
import logging
from civic2clinvar.c2c import assertions_to_clinvar_csv


@click.command()
@click.argument('assertion_ids')
@click.option('--aid-file', type=click.File('r'),
              help='Optional file of newline-separated assertion IDs. '
                   'This option is mutually exclusive with the ASSERTION_IDS argument.')
@click.option('-o', '--out', help="Output file (default: clinvar.csv), use '-' for STDOUT",
              type=click.File('w'), default='clinvar.csv')


def main(out, assertion_ids=None, aid_file=None):
    """This command generates a ClinVar-formatted csv file from a specified set of CIViC assertions.

    ASSERTION_IDS are a comma-separated list of assertions, and accepts integer ranges. Example usage:

    civic2clinvar 1,3-5

    The above command outputs a ClinVar submission form describing CIViC assertions 1, 3, 4, and 5 to clinvar.csv
    (the default output file). Output destination may be controlled with the --out option, detailed below.

    CIViC assertions that are rejected or pending are skipped.
    """

    logging.debug('Processing arguments')
    if aid_file and assertion_ids:
        logging.error("Expected one of assertion IDs or '--aid-file' option, not both.")
        return
    elif aid_file:
        id_list = list(aid_file)
    elif assertion_ids:
        id_list = list()
        id_chunks = assertion_ids.split(',')
        for chunk in id_chunks:
            try:
                id_list.append(int(chunk))
            except ValueError:
                start, end = chunk.split('-')
                id_list += list(range(int(start), int(end)+1))
    else:
        logging.error("Expected one of assertion IDs or '--aid-file' option.")
        return
    logging.debug('Argument processing complete')
    assertions_to_clinvar_csv(id_list, out)
