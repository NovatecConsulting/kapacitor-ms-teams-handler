from src.core import message_to_teams
from configuration.configuration import log_path
import logging
import sys
import json


def arg_check():
    logger = logging.getLogger('arg_check')
    logger.debug('Check sys arguments')
    try:
        if len(sys.argv) == 2:
            webhook = sys.argv[1]
            if "https://" not in webhook:
                logger.debug('The webhook URL must start with "https://"')
                sys.exit()
            return webhook
        else:
            logger.debug('Not enough arguments were found/passed (Argument 1 must be the ms teams webhook)')
            sys.exit()
    except Exception as e:
        print(e)


def main():
    logger = logging.getLogger('main')
    logging.basicConfig(filename=log_path,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logger.debug('Init main')
    webhook = arg_check()
    logger.debug('Read in stdin json and call message_to_teams')
    message_to_teams(alert_json=json.loads(sys.stdin.readline()), webhook=webhook)


if __name__ == '__main__':
    main()
