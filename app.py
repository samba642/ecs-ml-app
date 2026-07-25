from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
return jsonify({"status": "healthy", "service": "ml-inference-api"}), 200

@app.route('/predict', methods=['POST'])
def predict():
data = request.get_json() or {}
# Simulated model prediction logic
return jsonify({"prediction": [0.87], "model_version": "v1.0"}), 200

if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)
