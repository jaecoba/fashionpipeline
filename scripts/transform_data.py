import pandas as pd

def transform_data(data):
    # Reset index to convert date index to a column
    data.reset_index(inplace=True)
    
    # Rename columns to be more user-friendly
    data.rename(columns={'date': 'Date'}, inplace=True)
    
    # Convert date to a standard format
    data['Date'] = pd.to_datetime(data['Date']).dt.strftime('%Y-%m-%d')
    
    return data

# Example: Transform previously fetched data
if __name__ == "__main__":
    data = pd.read_csv('data/trend_data.csv')
    transformed_data = transform_data(data)
    
    # Save the transformed data for review
    transformed_data.to_csv('data/transformed_trend_data.csv', index=False)
    print(transformed_data.head())
