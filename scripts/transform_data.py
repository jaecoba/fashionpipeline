import pandas as pd

def transform_data(data):
    # Reset index to convert date index to a column
    if 'isPartial' in data.columns:
        data = data.drop('isPartial', axis=1)
    return data

# Example: Transform previously fetched data
if __name__ == "__main__":
    data = pd.read_csv('data/trend_data.csv')
    transformed_data = transform_data(data)
    
    # Save the transformed data for review
    transformed_data.to_csv('data/transformed_trend_data.csv', index=False)
    #print(transformed_data.head())
