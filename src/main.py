import pandas as pd

def read_products_from_csv(file_path):
    # Read the CSV file into a DataFrame, skipping the second row
    df = pd.read_csv(file_path)

    # Extract column names and data
    columns_str = df.columns[0]
    data_str = df.iloc[0, 0]

    # Split column names and data
    columns = columns_str.split(';')
    data_list = [data_str.split(';')]

    # Create DataFrame
    df = pd.DataFrame(data_list, columns=columns)

    # Convert DataFrame to a list of dictionaries
    products = df.to_dict('records')

    return products



my_file = read_products_from_csv('C://Users//KOM//Documents//Uge 9 - Niveau 2 - Cereal opgave//Data//Cereal.csv')

print(my_file[0:10][0])