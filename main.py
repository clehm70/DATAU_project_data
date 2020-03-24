
def convert_big_number2(nb):
    """
    Convert string in a form $XX.YYM or $XX.YYB into a numeric type to make possible future calculation
    :param nb: str representing a number in a df row
    :return: return the str converted into an int
        Convert string in a form $XX.YYM or $XX.YYB into a numeric type to make possible future calculation
        :param nb: str representing a number in a df row
        :return: return the str converted into an int
    """
    if nb != 'n/a':
        nb = nb.replace('$', '')
@@ -22,19 +22,31 @@ def convert_big_number2(nb):
        return 0


def columns_list(csv_uri):
def columns_list(csv_uri, sep):
    """
        Create a list of columns name from a csv.
        :param: csv_uri: uri of the csv
        :param: sep: separator
        :return: return list of csv
    """
    return list(pd.read_csv(
        csv_uri,
        sep="\t",
        sep=sep,
        nrows=1))


def read_csv(csv_uri):
    cols = columns_list(csv_uri)
def read_csv(csv_uri, sep):
    """
        Read a csv and optimize it's import into a DataFrame.
        :param: csv_uri: uri of the csv
        :param: sep: separator
        :return: Pandas DataFrame
    """
    cols = columns_list(csv_uri, sep)

    df = pd.read_csv(
        csv_uri,
        sep="\t",
        sep=sep,
        index_col='id',
        dtype={
            'id': 'int32',
@@ -55,4 +67,5 @@ def read_csv(csv_uri):
if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    read_csv(
        "https://gist.githubusercontent.com/gfelot/de17feb69320fff0a3bf1d59b9d42a06/raw/af6fcd62000b92cae8b80b285380cc7b66044a12/mock_data.tsv")
        "https://gist.githubusercontent.com/gfelot/de17feb69320fff0a3bf1d59b9d42a06/raw/af6fcd62000b92cae8b80b285380cc7b66044a12/mock_data.tsv",
        '\t')