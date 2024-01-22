from flask import Flask, jsonify, request
from sql import Db

app = Flask(__name__)

@app.route('/api/list', methods=['GET'])
def get_list():
    db = Db()
    data = db.get()
    return jsonify(data), 201

@app.route('/api/list=order', methods=['GET'])
def get_list_by_order():
    db = Db()
    data = db.get("num")
    return jsonify(data), 201

@app.route('/api/list', methods=['POST'])
def create_list():
    db = Db()
    list = [request.json.get('model', ""), request.json.get('num', ""), request.json.get('description', "")]
    db.write(list)
    return jsonify({"list":list}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)