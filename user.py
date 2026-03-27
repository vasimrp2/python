# To fetch the data from user table which is active
from flask import Flask, jsonify
import mysql.connector
from collections import OrderedDict

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rtw"
        )

        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, first_name, last_name, email_id,status FROM users WHERE status='active'")
        users = cursor.fetchall()

        cursor.close()
        conn.close()

        result = OrderedDict()
        result['status'] = True
        result['message'] = 'Data fetched successfully'
        result['data'] = users

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

