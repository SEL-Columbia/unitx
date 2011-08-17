"""

"""

from logging import getLogger
from logging import Formatter
from logging import StreamHandler
from logging import DEBUG
from urlparse import parse_qs
import argparse

from yaml import load, dump

log = getLogger('unitx.main')
log.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = StreamHandler()
handler.setFormatter(formatter)

log.addHandler(handler)

commands = []

def wrap_message_reducer(message):
    """
    Function to reduce the values of a dict to one value instead of a
    list.
    """
    log.info('Starting message reducing --> %s' % message)
    c = {}
    for key, value in message.iteritems():
        c[key] = value[0]
    log.info('Reduced message --> %s' % c)
    return c

def wrap_message_parser(message):
    """
    Function that takes a message and tries to parse its body key.

    Possible parse options.
      1. Meter message
         (job=pp&....)
         (pcu#) 
      2. Consumer messages
         9.1234.1234
         bal.1123

    """
    body = message.get('body')
    if body is not None:
        if body.startswith('('):
            log.info('Meter message found')
            return message
        elif isinstance(body[0], str) or isinstance(body[0], int):
            log.info('Consumer message found')
            message['payload'] = body.split('.')
            log.info('Message payload --> %s ' % message)
            return message
    else:
        log.debug('Message %s has no body key' % message)
        return message


def wrap_message_command(message):
    """
    Takes a message and matches it to a list of global commands
    """
    message['command'] = 'test'
    return message


def wrap_router(message, config):
    """
    """
    log.info('Loading router config --> %s' % config)
    message['configuration'] = load(open(config))
    return message



def invoke_router(command):
    """
    Takes a command a command is a message_dict excep it has a command
    key which is a function to be called.
    """
    log.info('Running --> %s' % command)


def run(message, config):
    assert type(message) == str
    message = wrap_message_command(
        wrap_router(
            wrap_message_parser(
                wrap_message_reducer(parse_qs(message))),
            config
            )
        )
        
    invoke_router(message)


def run_command_line():
    parser = argparse.ArgumentParser(
        description='Process SharedSolar Messages')
    parser.add_argument('message', type=str, help='Give me your message!!')
    parser.add_argument('config', type=str, help='Router config file')
    args = parser.parse_args()
    log.info('==================================================')
    log.info('Got raw message -->  %s' % args.message)
    run(args.message, args.config)


