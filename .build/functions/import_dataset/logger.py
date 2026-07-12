import logging
import os


LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    "dataset_import.log"
)


def get_logger():

    logger = logging.getLogger("CrimeLensImporter")

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    console = logging.StreamHandler()

    console.setFormatter(formatter)

    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(console)

    logger.addHandler(file_handler)

    return logger