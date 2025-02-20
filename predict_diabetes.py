import pandas as pd
from pycaret.classification import predict_model, load_model

def load_data(filepath):
    """
    Loads diabetes data into a DataFrame from a string filepath.
    """
    df = pd.read_csv(filepath, index_col='Patient number')
    return df


def make_predictions(df):
    """
    Uses the pycaret best model to make predictions on data in the df dataframe.
    """
    model = load_model('LDA')
    predictions = predict_model(model, data=df)

    # Check the column names
    print(predictions.columns)
    
    # Rename 'prediction_label' to 'Diabetes_prediction' if it exists
    if 'prediction_label' in predictions.columns:
        predictions.rename(columns={'prediction_label': 'Diabetes_prediction'}, inplace=True)
        
        # Replace values in the new column
        predictions['Diabetes_prediction'].replace({1: 'Diabetes', 0: 'No diabetes'}, inplace=True)
        
        return predictions['Diabetes_prediction']
    else:
        raise KeyError("The 'prediction_label' column was not found in the predictions DataFrame")


if __name__ == "__main__":
    df = load_data('new_diabetes_data.csv')
    predictions = make_predictions(df)
    print('predictions:')
    print(predictions)
    print('those are the predictions!')