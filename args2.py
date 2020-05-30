import argparse
# use a config file for parameters
import configparser
# store resault in file
import sys

def main(num1, num2, output):
    r = num1 * num2
    print('the resault is {}'.format(r), file=output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, default=0, help='One of the multiplicants')
    parser.add_argument('-n2', type=int, default=0, help='The other multiplicant')
    # add the optional config file to the program
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='a config file')
    # configure the flag to output to a file
    parser.add_argument('-o', type=argparse.FileType('w'), help='Output file',
                        dest='output', default=sys.stdout)

    args = parser.parse_args()

    if args.config:
        # the config file should contain
        # [ARGUMENTS]
        # n1=5
        # n2=7

        config = configparser.ConfigParser()
        config.read_file(args.config)
        # transform values
        # access the ARGUMENTS dictionary and the n1 and n2 parameters inside that dictionary
        args.n1 = int(config['ARGUMENTS']['n1'])
        args.n2 = int(config['ARGUMENTS']['n2'])

    main(args.n1, args.n2, args.output)
