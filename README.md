# civic2clinvar

`civic2clinvar` is a python-based command line utility for extracting [CIViC](https://civicdb.org) assertions and translating them into ClinVar records.

## Installation
`$ pip install civic2clinvar`

## Usage
```bash
$ civic2clinvar --help

Usage: civic2clinvar [OPTIONS] ASSERTION_IDS

  This command generates a ClinVar-formatted csv file from a specified set
  of CIViC assertions.

  ASSERTION_IDS are a comma-separated list of assertions, and accepts
  integer ranges. Example usage:

  civic2clinvar 1,3-5

  The above command outputs a ClinVar submission form describing CIViC
  assertions 1, 3, 4, and 5 to clinvar.csv (the default output file). Output
  destination may be controlled with the --out option, detailed below.

  CIViC assertions that are rejected or pending are skipped.

Options:
  --aid-file FILENAME  Optional file of newline-separated assertion IDs. This
                       option is mutually exclusive with the ASSERTION_IDS
                       argument.
  -o, --out FILENAME   Output file (default: clinvar.csv), use '-' for STDOUT
  --help               Show this message and exit.
```