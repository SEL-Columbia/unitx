"""

"""
import re
from logging import getLogger
from logging import Formatter
from logging import StreamHandler
from logging import DEBUG
from urlparse import parse_qs

from yaml import load
from unitx import parsers

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
        results = apply(f, args)
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
    for classifer in config['classifers']:
        if re.match(classifer['classifer'], message['body']):
            message['classification'] = classifer
            return message
    return message


@log_function
def final_parse(message):
    parse_func = getattr(parsers, message['classification']['parser'])
    return parse_func(message)


@log_function
def route_message(message):
    for route in config['routes']:
        for match in route['matchers']:
            if re.match(match, message.get('body')):
                message['route'] = route
                return message
    return message


def run_main(message):
    """
    """
    assert len(message) is not 0
    assert isinstance(message, str)
    return route_message(final_parse(classify(initial_parse(message))))
