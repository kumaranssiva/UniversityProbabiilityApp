import pandas as pd
import numpy as np
import joblib

def input_scalar(df):
    path = '/Users/kavitha/Desktop/MLProjects/hackathon/Notebook/standard_scaler.sav'
    scalar = joblib.load(path)
    final_df = scalar.transform(df)
    return final_df