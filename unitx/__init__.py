"""

"""
import re
from logging import getLogger
from logging import Formatter
from logging import StreamHandler
from logging import DEBUG
from urlparse import parse_qs
import argparse

from yaml import load

log = getLogger('unitx.main')
log.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = StreamHandler()
handler.setFormatter(formatter)

log.addHandler(handler)


def load_config(file_path):
    return load(open(file_path))

config = load_config('config.yaml')


def log_function(f):
    def wrap(*args):
        #log.info('Calling %s with --> %s' % (f.__name__, args[0]))
        results = f(*args)
        #log.info('Returning %s with--> %s' % (f.__name__, results))
        return results
    return wrap


@log_function
def initial_parse(raw_message):
    c = {}
    for key, value in parse_qs(raw_message).iteritems():
        c[key] = value[0]
    return c


@log_function
def classify(message):
    """
    """
    for classifer in config['classifers']:
        if re.match(classifer['classifer'], message['body']):
            print 'stuff'
            message['classification'] = classifer['name']
            return message
    return message


def run_main(message):
    """
    """
    return classify(initial_parse(message))


def run_command_line():
    parser = argparse.ArgumentParser(
        description='Process SharedSolar Messages')
    parser.add_argument('message', type=str, help='Give me your message!!')
    args = parser.parse_args()
    log.info('Got raw message -->  %s' % args.message)
    run_main(args.message)
