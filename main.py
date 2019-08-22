import logging
import argparse
from lib.gom import Gom
from lib.zwick import Zwick
import lib.functions as functions
from IPython import embed


def main(gom_file, zwich_file, output=False):
    functions.init_program()

    gom = Gom(gom_file)
    gom.load_csv(';')
    gom_breakpointing = gom.get_max_row(3)

    zwick = Zwick(zwich_file)
    zwick.load_csv("\t")
    zwick_breakingpoint = zwick.get_max_row(1)
    logging.info(r"The breaking point for ")

    for final_row_number in range(gom_breakpointing[0]):
        pass
    embed()




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Merging two datasets from GOM and ZWICK',
                                     epilog='Script that merges two datasets into one')
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
