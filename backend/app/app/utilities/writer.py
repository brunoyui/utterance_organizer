import logging
from app.db.session import SessionLocal
import csv

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Writer:
    def write():
        pass

class WriterCSV(Writer):
    def write(self, dataset, file_path):
        with open(file_path,'w') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            for key, value in dataset.items():
                tsv_writer.writerow(value[0])
            tsv_file.close()


class WriterDatabase(Writer):
    def write(self, dataset):
        count = 0
        for key, value in dataset.items():
            count += len(value)
            print(str(key), '->', value[0])
        print(count)