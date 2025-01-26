from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Load the marks data from the JSON file
def load_marks_data():
    # Get the path to the JSON file in the `api` subfolder
    json_file_path = os.path.join(os.path.dirname(__file__), 'q-vercel-python.json')
    
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data

marks_data = load_marks_data()

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    marks = []
    for name in names:
        student = next((item for item in marks_data if item["name"] == name), None)
        if student:
            marks.append(student["marks"])
        else:
            marks.append(None)
    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)