import logging
import argparse
from IPython import embed

def main(gom_file, zwich_file, output=False):
    embed()
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merging two datasets from GOM and ZWICK',
                                     epilog='Script that merges to dataset to one')
    parser.add_argument('-g', '--gom-file', help='File with GOM data', required=True)
    parser.add_argument('-z', '--zwich-file', help='File with Zwick data', required=True)
    parser.add_argument('-o', '--output-file', help='Name of file for output (csv). If not provided, it will go to '
                                                    'stdout', default=False, required=False)
    parser.add_argument('-v', '--verbose', action='store_true', help='increase output verbosity')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    else:
        logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.INFO)
    main(args.gom_file, args.zwich_file, args.output_file)
