from os import listdir
from os.path import join

import pandas


class IndicationsReader:
    def __init__(self, directory_path, column_number):
        self._directory_path = directory_path
        self._column_number = column_number

    def get_indications(self):
        indications = {}
        for file_path in self._get_file_paths():
            indications[file_path] = self._read_indication(file_path)

        return indications

    def _read_indication(self, file_path):
        df = pandas.read_csv(file_path, header=None)
        return [float('.'.join(str(reading).split(','))) for reading in list(df.iloc[:, self._column_number])]

    def _get_file_paths(self):
        return [join(self._directory_path, f) for f in listdir(self._directory_path)]
