import numpy as np
import pandas as pd
from sklearn.datasets import load_iris  # You can replace this with any sklearn dataset loader

def load_dataset_to_dataframe(loader):
    """
    Converts a sklearn dataset into a pandas DataFrame including target labels and names if available.
    
    Parameters:
    - loader: a function that loads an sklearn dataset.
    
    Returns:
    - A pandas DataFrame with features and target, with target names as categorical data if available.
    """
    # Load the dataset
    data = loader()
    
    # Check if target names are available, otherwise use numerical targets
    if 'target_names' in data and data.target_names is not None:
        target_name = 'species'
        data_df = pd.DataFrame(data=np.c_[data['data'], data['target']], columns=data['feature_names'] + ['target'])
        data_df[target_name] = pd.Categorical.from_codes(data.target, data.target_names)
    else:
        target_name = 'target'
        data_df = pd.DataFrame(data=np.c_[data['data'], data['target']], columns=data['feature_names'] + [target_name])
    
    return data_df
