import pandas as pd

def load_data(filepath, num_rows=None):
    """
    Load data from a CSV file.

    Parameters:
    filepath (str): The path to the CSV file.
    num_rows (int, optional): The number of rows to load. If None, all rows are loaded.

    Returns:
    pd.DataFrame: The loaded data.
    """
    data = pd.read_csv(filepath, nrows=num_rows)
    return data