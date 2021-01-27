from configuration.configuration import http_proxy, https_proxy
import requests
import logging

logger = logging.getLogger('core')


def message_to_teams(alert_json: dict, webhook: str) -> None:
    try:
        proxy_dict = {"http": http_proxy, "https": https_proxy}
        json_message = {
            "title": alert_json["message"],
            "text":  alert_json["details"].replace("<br>", "  \n") + "  \nTime: " + alert_json["time"]
        }
        logger.debug("Triggering MS-Teams webhook: {}".format(webhook))
        response = requests.post(url=webhook, proxies=proxy_dict, json=json_message)
    except ConnectionError as connection_error:
        logger.error('Connection Error: {}'.format(connection_error))
    except Exception:
        logger.exception("Triggering the MS-Teams webhook failed")
