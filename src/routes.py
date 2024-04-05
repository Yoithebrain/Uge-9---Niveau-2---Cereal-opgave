# routes are defined in this file

# Imports
from flask import jsonify, request, abort
import pandas as pd
import csv

# Function to read products from CSV file
def read_products_from_csv(file_path):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Split the column names
    columns = list(df.keys())[0].split(';')

    # Split the values for each row and create dictionaries
    products = []
    for row in df.values:
        values = row[0].split(';')
        product = {}
        for i, column in enumerate(columns):
            product[column] = values[i]
            products.append(product)
    #print(products[0:1])

    # Convert DataFrame to a list of dictionaries
    #products = df.to_dict('records')

    return products


# Function to filter products based on parameters
def filter_products(products, params):
    
    filtered_products = []
    for product in products:
        matches_all_criteria = True
        for key, value in params.items():
            if '>' in key:
                column, condition = key.split('>')
                if column in product:
                    if float(product[column]) <= float(condition):
                        matches_all_criteria = False
                        break
                else:
                    matches_all_criteria = False
                    break
            elif '<' in key:
                column, condition = key.split('<')
                if column in product:
                    if float(product[column]) >= float(condition):
                        matches_all_criteria = False
                        break
                else:
                    matches_all_criteria = False
                    break
            elif product.get(key) != value:
                matches_all_criteria = False
                break
        if matches_all_criteria:
            filtered_products.append(product)
    return filtered_products



# Configure routes
def configure_routes(app):
    
    @app.route('/data', methods=['GET'])
    def get_route():
        return "Hello world"

    @app.route('/data', methods=['POST'])
    def post_route():
        data = request.json  # Get JSON data from the request
        file_path = 'C://Users//KOM//Documents//Uge 9 - Niveau 2 - Cereal opgave//Data//Cereal.csv'  # Update with your file path
    
        # Write the data to the CSV file, overwriting existing content
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data.values())
    
        return jsonify({'message': 'Data overwritten successfully'}), 201
    
    @app.route('/products', methods=['GET'])
    def get_products():
        file_path = 'C://Users//KOM//Documents//Uge 9 - Niveau 2 - Cereal opgave//Data//Cereal.csv'  # Adjust the file path accordingly
        products = read_products_from_csv(file_path)
        #print(products[0:10])
        params = request.args.to_dict()
        print(params)
        if params:
            filtered_products = filter_products(products, params)
            print(filtered_products)
            return jsonify(filtered_products)
        else:
            return jsonify(products)
    
    # Define the route for deleting a row from the CSV file
    @app.route('/delete_row', methods=['DELETE'])
    def delete_row():
        file_path = 'C://Users//KOM//Documents//Uge 9 - Niveau 2 - Cereal opgave//Data//Cereal.csv'  # Path to your CSV file

        # Parse the row index from the request parameters
        row_index = request.args.get('row_index', type=int)

        # Read the existing data from the CSV file
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

        # Check if the row index is valid
        if row_index < 0 or row_index >= len(rows):
            return jsonify({'message': 'Invalid row index'}), 400

        # Remove the row at the specified index
        del rows[row_index]

        # Write the modified data back to the CSV file
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        return jsonify({'message': 'Row deleted successfully'}), 200