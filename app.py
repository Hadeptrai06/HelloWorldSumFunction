from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import datetime

app = Flask(__name__)
CORS(app)  # Cho phép truy cập từ frontend

@app.route('/sum', methods=['POST'])
def sum_numbers():
    data = request.get_json()
    a = data.get('a', 0)
    b = data.get('b', 0)
    return jsonify({'sum': a + b})

@app.route('/tinhTuoi', medthods=['POST'])
def tinhTuoi():
    data = request.get_json()
    namSinh = data.get('namSinh', 0)
    tuoi = datetime.datetime.now().year - namSinh
    return jsonify({'tuoi': tuoi})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)