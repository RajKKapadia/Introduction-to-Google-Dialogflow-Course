import logging
import sys

LOGGING_FORMAT = '%(asctime)s (%(module)s -> %(filename)s): %(levelname)s -> %(message)s'

logging.basicConfig(
    format=LOGGING_FORMAT,
    handlers=[
        logging.StreamHandler(sys.stdout)
    ],
    level='INFO'
)
