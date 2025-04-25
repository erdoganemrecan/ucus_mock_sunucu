
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/ucus-bilgisi", methods=["GET"])
def ucus_bilgisi():
    kalkis = request.args.get("from")
    varis = request.args.get("to")
    tarih = request.args.get("date")

    with open("mock_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    sonuc = [ucus for ucus in data if ucus["Kalkış"] == kalkis and ucus["Varış"] == varis and ucus["Tarih"] == tarih]
    return jsonify(sonuc)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
