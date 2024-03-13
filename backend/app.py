from flask import Flask, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import statistics
import math

app = Flask(__name__)
CORS(app)

# MongoDB configuration
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "khub"

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db["task"]

# Calculate IQR
def calculate_iqr(values):
    values_sorted = sorted(values)
    n = len(values_sorted)
    q1_index = int(n * 0.25)  # Index for the first quartile
    q3_index = int(n * 0.75)  # Index for the third quartile
    q1 = values_sorted[q1_index]
    q3 = values_sorted[q3_index]
    iqr = q3 - q1
    return iqr

@app.route('/api/khub/<statistic>', methods=['GET'])
def get_all_statistics2(statistic):
    try:
        valid_statistics = ['mean', 'median', 'mode', 'standard_deviation', 'variance', 'interquartilerange']

        if statistic not in valid_statistics:
            return jsonify({'message': 'Invalid statistic type'})

        data = list(collection.find({}, {'Maths': 1, 'Physics': 1, '_id': 0}))
        attributes = ['Maths', 'Physics']

        result = {}

        for attribute in attributes:
            values = [item[attribute] for item in data if isinstance(item[attribute], (int, float)) and not math.isnan(item[attribute])]

            if values:
                if statistic == 'mean':
                    result[attribute] = round(statistics.mean(values), 4)
                elif statistic == 'median':
                    result[attribute] = round(statistics.median(values), 4)
                elif statistic == 'mode':
                    try:
                        result[attribute] = statistics.mode(values)
                    except statistics.StatisticsError:
                        result[attribute] = None
                elif statistic == 'standard_deviation':
                    result[attribute] = round(statistics.stdev(values), 4)
                elif statistic == 'variance':
                    result[attribute] = round(statistics.variance(values), 4)
                elif statistic == 'interquartilerange':
                    result[attribute] = round(calculate_iqr(values), 4)
            else:
                result[attribute] = None

        response = jsonify(result)
        return response

    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
