import pandas as pd
import os
from os import path

def load_data (path_to_data):
    ATCO_CSV = pd.read_csv(path_to_data)
    return ATCO_CSV