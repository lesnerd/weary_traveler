import pandas
import pandas as pd


class CSVStepsArrayLoader(object):
    @staticmethod
    def load(file_path):
        try:
            df = pd.read_csv(file_path, sep=',', header=None, skip_blank_lines=True).dropna()
        except pandas.errors.EmptyDataError:
            raise pandas.errors.EmptyDataError('No data to read.')
        if df.empty:
            raise IOError('The file is empty.')
        return df.values[0].astype(int).tolist()

        """
        df = pd.read_csv(file_path, usecols=[1], sep=',')
        if df.empty:
            raise IOError('The file is empty.')
        print(df.values.astype(int).tolist())
        return df.iloc[:,0].tolist()

        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            row = [int(row[1]) for row in csv_reader]
            return row
        """