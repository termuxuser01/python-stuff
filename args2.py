import argparse
# use a config file for parameters
import configparser
# store resault in file
import sys
# use of cron to schedule execution
from datetime import datetime
# enable error loggin
import logging

LOG_FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
LOG_LEVEL = logging.DEBUG

def main(num1, num2, output):
    r = num1 * num2
    print('[{}] the resault is {}'.format(datetime.utcnow().strftime('%d/%m/%Y %X'), r), file=output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-n1', type=int, default=0, help='One of the multiplicants')
    parser.add_argument('-n2', type=int, default=0, help='The other multiplicant')
    # add the optional config file to the program
    parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='a config file',
                        default='/etc/automate.ini')
    # configure the flag to output to a file
    # append to log
    parser.add_argument('-o', type=argparse.FileType('a'), help='Output file',
                        dest='output', default=sys.stdout)
    # add option for logging file
    parser.add_argument('-l', dest='log', type=str, help='log file',
                        default=None)

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

    if args.log:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL, filename=args.log)
    else:
        logging.basicConfig(format=LOG_FORMAT, level=LOG_LEVEL)

    try:
        main(args.n1, args.n2, args.output)
    except Exception as exp:
        logging.exception('There was an error, exiting...')
        exit(1)
