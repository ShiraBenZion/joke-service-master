import logging
from typing import Optional
from auth import Auth


def setup_logger(log_to_file: bool = True, log_file_path: Optional[str] = 'app.log',
                 message_format: str = '%(asctime)s - %(levelname)s - %(message)s',
                 date_format: str = '%Y-%m-%d %H:%M:%S'):
    """
    define the logger with flexible options to change where the output goes/
    date format and message format

    :param message_format:
    :param log_to_file: do write to a file (default: False)
    :param log_file_path: file's path (default: '%(asctime)s - %(levelname)s - %(message)s')
    :param date_format: date format (default: '%Y-%m-%d %H:%M:%S')
    """
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(fmt=message_format, datefmt=date_format)

    if log_to_file:
        handler = logging.FileHandler(log_file_path)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)


def log_request(request, response):
    logger = logging.getLogger()
    account_print = "UNAUTHORIZED" if not Auth.is_account_authorized(request=request) \
        else str(request.headers.get('authorization'))
    log_message = (
        f"Account: {account_print} | "
        f"IP: {request.client.host} | "
        f"Endpoint: {request.url.path} | "
        f"Method: {request.method} | "
        f"Status Code: {response.status_code}"
    )
    logger.info(log_message)

