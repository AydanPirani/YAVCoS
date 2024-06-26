import argparse
from utilities import parser_generator

def main():
    parser = parser_generator.ParserGenerator()
    args = parser.get_args()
    args.func(args)

if __name__ == "__main__":
    main()