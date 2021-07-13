import logging
import requests

logger = logging.getLogger(__name__)


# TODO: may make more sense to move to an app settings
IP_CHECK_URL = 'https://checkip.amazonaws.com'


def get_public_ip() -> str:
    try:
        res = requests.get(IP_CHECK_URL)
        assert res.status_code == 200
        return res.text.strip()
    except Exception:
        logger.error('Error checking public ip')
        return 'unknown'
