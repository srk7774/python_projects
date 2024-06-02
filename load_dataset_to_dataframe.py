import pandas as pd
from sklearn.utils import Bunch

def load_dataset_to_dataframe(dataset: Bunch) -> pd.DataFrame:
    """
    Convert a sklearn dataset to a pandas DataFrame, including target variable as a categorical column name if applicable.

    Parameters:
    dataset (Bunch): The sklearn dataset to convert.

    Returns:
    pd.DataFrame: The dataset as a pandas DataFrame.
    """
    # Convert the dataset to a DataFrame
    df = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    
    # Add the target if available
    if 'target' in dataset:
        df['target'] = dataset.target
        
        # Add the target names as a categorical column if available
        if 'target_names' in dataset:
            df['target_name'] = pd.Categorical.from_codes(dataset.target, dataset.target_names)

    return df
