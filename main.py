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
    logging.info(f"The breaking point for gom is at {gom.csv[gom_breakpointing[0]][0]} sec")

    zwick = Zwick(zwich_file)
    zwick.load_csv("\t")
    zwick_breakingpoint = zwick.get_max_row(1)
    diff_time = gom.csv[gom_breakpointing[0]][0] - zwick.csv[zwick_breakingpoint[0]][2]
    logging.info(f"The breaking point for zwick is at {zwick.csv[zwick_breakingpoint[0]][2]} sec. "
                 f"Difference of {diff_time} sec")
    generated_csv = []
    zwick_working_row_id = 0
    for generating_row_id in range(1, gom_breakpointing[0]):
        gom_working_row = gom.csv[gom_breakpointing[0] - generating_row_id]
        index = 0
        collect_zwick_avarage = []
        while zwick.csv[zwick_breakingpoint[0]-index][2] + diff_time >= gom_working_row[0]:
            collect_zwick_avarage.append(zwick.csv[zwick_breakingpoint[0]-index])
            index += 1
        break
        avg = [float(sum(col)) / len(col) for col in zip(*collect_zwick_avarage)]
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
