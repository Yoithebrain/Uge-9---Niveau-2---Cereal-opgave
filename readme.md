# Project Name

A simple API that gets data from a CSV file, it can also fetch the pictures within the pictures folder

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>

2. Navigate to the project directory:
    cd project-directory

3. Create a virtual environment (optional but recommended):
    python -m venv venv

4. Activate the virtual environment:
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate

5. Install the dependencies:
    pip install -r requirements.txt

## Usage
1. Go to src directory:
    Run app.py
2. Make request in either browser or via cURL:
    curl -X GET 'http://localhost:5000/products?calories=120'
3. To add data, send a json object with your request:
    curl -X POST -H "Content-Type: application/json" -d "{\"calories\":\"200\",\"carbo\":\"100\",\"cups\":\"2\",\"fat\":\"10\",\"fiber\":\"20\",\"mfr\":\"E\",\"name\":\"Test\",\"potass\":\"100\",\"protein\":\"0\",\"rating\":\"10.900.670\",\"shelf\":\"4\",\"sodium\":\"1\",\"sugars\":\"2\",\"type\":\"C\",\"vitamins\":\"0\",\"weight\":\"10\"}" http://localhost:5000/data
    ### Example object:
        {
    "calories":"200",
    "carbo":"100",
    "cups":"2",
    "fat":"10",
    "fiber":"20",
    "mfr":"E",
    "name":"Test",
    "potass":"100",
    "protein":"0",
    "rating":"10.900.670",
    "shelf":"4",
    "sodium":"1",
    "sugars":"2",
    "type":"C",
    "vitamins":"0",
    "weight":"10"
        }
