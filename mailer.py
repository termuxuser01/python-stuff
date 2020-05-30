import argparse
import configparser
import smtplib
from email.message import EmailMessage

def main(to, server, port, from_addr, passwd):
    print('With love from {} to {}'.format(from_addr, to))
    # build message
    subject = "With love from me to you!"
    text = '''what's up i just wanted to know how you've been doing
    how are the kids?
    '''
    msg = EmailMessage()

    msg.set_content(text)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to

    # setup connection
    server = smtplib.SMTP_SSL(server, port)
    server.login(from_addr, passwd)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('email', type=str, help='Email address to send email')
    parser.add_argument('-c', type=argparse.FileType('r'), help='config file for your account',
                        dest='config', default=None)
    
    args = parser.parse_args()

    if not args.config:
        print('Error need a config file')
        parser.print_help()
        exit(1)
    
    config = configparser.ConfigParser()

    config.read_file(args.config)

    main(args.email, server=config['DEFAULT']['server'], port=config['DEFAULT']['port'],
        from_addr=config['DEFAULT']['email'], passwd=config['DEFAULT']['password'])
