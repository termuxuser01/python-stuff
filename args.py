import argparse

def main(character, number):
    print(character * number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='The number of times to print hash')
    # add optional argument for character to print (default will be #)
    # If an argument starts with a -, it is considered an optional parameter
    parser.add_argument('-c', type=str, help='The character to be printed', 
                        default='#')
    # add option to print uppercase characters
    # The actions store_true and store_false can be used to generate flags, arguments that don't require any extra parameters. 
    # he name of the property in the args object will be, by default, the name of the argument (without the dash, if it's present).
    # You can change it with dest. 
    parser.add_argument('-U', '--uppercase', action='store_true', default=False,
                        dest='uppercase',
                        help='Use flag to print in uppercase' )

    args = parser.parse_args()

    if args.uppercase:
        args.c = args.c.upper()

    main(args.c, args.number)
