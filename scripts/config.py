import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

DATA_IMPORT_LOCATION = './data'
IMPORT_FILE_NAME = 'horror_movies'
