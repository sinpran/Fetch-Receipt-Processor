from flask import Flask, request, jsonify
import uuid
from typing import Dict
import utils

app = Flask(__name__)

RECEIPT_TRACKER: Dict[str, str] = {}

@app.route("/receipts/<id>/points", methods=["GET"])
def getPoints(id: str) -> Dict[str, int]:
    try:
        points = RECEIPT_TRACKER.get(id, 0)
        if not points:
            return jsonify({"Error": "No receipts found"}), 204
        return jsonify({"points": points}), 200
    except:
        return jsonify({"Error": "Invalid Request"}), 400


@app.route("/receipts/process", methods=["POST"])
def processReceipts() -> Dict[str, str]:
    try:
        receipt = request.get_json()
        receipt_id = str(uuid.uuid4())
        points = utils.get_total_receipt_points(receipt)
        RECEIPT_TRACKER[receipt_id] = points
        return jsonify(id=receipt_id), 201
    except:
        return jsonify({"Error": "Invalid Request"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
