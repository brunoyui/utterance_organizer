import logging

from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.utilities import ReaderCSV, WriterDatabase, WriterCSV

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DATASET_FILE_PATH = "./data/dataset3.tsv"

DATASET_FILE_WRITE_PATH = './data/datasetW.tsv'

def load() -> None:
    db = SessionLocal()
    dataset = read()
    write(dataset)

def read():
    reader = ReaderCSV()
    return reader.read(DATASET_FILE_PATH)

def write(dataset):
    writer = WriterCSV()
    print(len(dataset))
    writer.write(dataset, DATASET_FILE_WRITE_PATH)


def main() -> None:
    logger.info("Start loading process")
    load()
    logger.info("Finish loading process")


if __name__ == "__main__":
    main()
