from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database configuration
db_config = {
    'user': os.getenv('MYSQL_USER', 'root'),
    'password': os.getenv('MYSQL_PASSWORD', 'password'),
    'host': os.getenv('MYSQL_HOST', 'mysql'),
    'database': os.getenv('MYSQL_DATABASE', 'test_db')
}

@app.route('/')
def index():
    return 'Request/Response Web app'

@app.route('/data', methods=['GET'])
def get_data():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_table")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
