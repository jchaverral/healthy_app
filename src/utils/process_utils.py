import pandas              as pd
import numpy               as np


def round_data(df,columns_round,round_number=0):
    _df = df.copy()
    _df[columns_round] = _df[columns_round].round(round_number)
    return _df

def convert_to_int(df,columns_type,type_col=int):
    _df = df.copy()
    _df[columns_type] = _df[columns_type].astype(type_col)  
    return _df