from ASCIIpie import asciipie
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

    argparser.add_argument('-g',
                           '--grayscale',
                           default=False,
                           action='store_true',
                           help='use grayscale')

    argparser.add_argument('-t',
                           '--text',
                           default=False,
                           action='store_true',
                           help='output to text file')

    args = argparser.parse_args()
    keep_color = not args.grayscale
    output_path = args.output
    input_path = args.path
    text_mode = args.text
    if not os.path.isfile(input_path):
        print('This file doesn\'t exist')
        sys.exit()
    asciipie(
        input_file=input_path,
        output_file=output_path,
        keep_color=keep_color,
        text_mode=text_mode
    )


if __name__ == "__main__":
    main()
