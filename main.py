from src.core import message_to_teams
from configuration.configuration import log_path
import logging
import sys
import json


def arg_check():
    logger = logging.getLogger('arg_check')
    try:
        if len(sys.argv) == 2:
            webhook = sys.argv[1]
            if "https://" not in webhook:
                logger.error('The webhook URL must start with "https://" \n'
                             'Received URL: {}'.format(webhook))
                sys.exit()
            return webhook
        else:
            logger.error('Not enough or too many arguments were passed. \n'
                         'Example usage: python3 main.py "https://webhook-url" < tests/example_alert.json')
            sys.exit()
    except Exception as e:
        logger.exception("Parsing arguments failed")


def main():
    logger = logging.getLogger('main')
    logging.basicConfig(filename=log_path,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    webhook = arg_check()
    logger.debug('Read in stdin json and call message_to_teams')
    message_to_teams(alert_json=json.loads(sys.stdin.readline()), webhook=webhook)


if __name__ == '__main__':
    main()
