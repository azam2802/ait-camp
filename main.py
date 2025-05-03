from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

clientsDictonary = {"Munara": 4000, "Timur": 5000, "Daiyrbek": 600, "Emil": 2000}
pincodes = {"Munara": 1234, "Timur": 2345, "Daiyrbek": 3456, "Emil": 4567}
history = []

@app.route('/transfer', methods=["POST"])
def transferDictionary():
    data = request.get_json()
    toClient = data.get("to")
    amount = data.get("amount")
    fromClient = data.get("from")
    pincode = data.get("pincode")
    
    if fromClient not in clientsDictonary or toClient not in clientsDictonary:
        print("Пользователь не найден")
        return jsonify({"error": "Пользователь не найден"}), 400
    if fromClient == toClient:
        print("Невозможно перевести самому себе")
        return jsonify({"error": "Невозможно перевести самому себе"}), 400
    if int(pincode) != pincodes.get(fromClient):
        print("Неверный пин-код")
        return jsonify({"error": "Неверный пин-код"}), 400
    if int(amount) <= 0:
        print("Невозможно перевести сумму <= 0")
        return jsonify({"error": "Невозможно перевести сумму <= 0"}), 400
    if clientsDictonary.get(fromClient) < int(amount):
        print("Недостаточно средств")
        return jsonify({"error": "Недостаточно средств"}), 400
    clientsDictonary[fromClient] -= int(amount)
    clientsDictonary[toClient] += int(amount)
    history.append({
        "from": fromClient,
        "to": toClient,
        "amount": amount,
        "date": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })
    
    print(clientsDictonary)
    
    return jsonify(clientsDictonary), 200

@app.route('/clients', methods=["GET"])
def get_clients():
    return jsonify(clientsDictonary), 200

@app.route('/history', methods=["GET"])
def get_history():
    return jsonify(history), 200