from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route('/ser', methods=['POST'])
def ser_eval():
    data = request.get_json(force=True)
    if not data or 'nodes' not in data or 'prob' not in data:
        return jsonify({"error": "Expecting JSON with 'nodes' and 'prob'"}), 400

    try:
        H = sum(x.get('energy', 0) for x in data['nodes'])
    except Exception as e:
        return jsonify({"error": f"Invalid nodes format: {e}"}), 400

    try:
        S = -sum(p * math.log(p) for p in data['prob'] if p > 0)
    except Exception as e:
        return jsonify({"error": f"Invalid prob format: {e}"}), 400

    return jsonify({"H": H, "S": S})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
