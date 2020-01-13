import pandas
import pandas as pd


class TSVStepsArrayLoader(object):
    @staticmethod
    def load(file_path):
        try:
            df = pd.read_csv(file_path, sep='\t', header=None, skip_blank_lines=True).dropna()
        except pandas.errors.EmptyDataError:
            raise pandas.errors.EmptyDataError('No data to read.')
        if df.empty:
            raise IOError('The file is empty.')
        return df.values[0].astype(int).tolist()


        """
        with open(file_path) as tsv_file:
            tsv_reader = csv.reader(tsv_file, delimiter='\t')
            next(tsv_reader)
            row = [int(row[1]) for row in tsv_reader]
        return row
        """