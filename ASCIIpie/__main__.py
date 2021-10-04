from ASCIIpie import asciipie_file
import argparse
import sys
import os


def main():
    argparser = argparse.ArgumentParser(description='Convert images to ASCII art')

    argparser.add_argument('path',
                           help='input file path')

    argparser.add_argument('-o',
                           '--output',
                           help='output file path')

    args = argparser.parse_args()
    output_path = args.output
    input_path = args.path
    if not os.path.isfile(input_path):
        print('This file doesn\'t exist')
        sys.exit()
    asciipie_file(
        input_file=input_path,
        output_file=output_path
    )


if __name__ == "__main__":
    main()
