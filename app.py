import pickle
from flask import Flask, request, jsonify
from prometheus_client import Counter, Histogram, start_http_server

# Initialize Flask app
app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Define Prometheus metrics
inference_requests = Counter('inference_requests_total', 'Total number of inference requests')
inference_latency = Histogram('inference_latency_seconds', 'Time spent processing inference requests')

# Health check route
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Inference route
@app.route('/predict', methods=['POST'])
@inference_latency.time()  # Measure latency
def predict():
    inference_requests.inc()  # Increment request count
    try:
        # Parse input JSON
        data = request.json
        features = data.get("features")
        if not features:
            return jsonify({"error": "No features provided"}), 400

        # Make prediction
        prediction = model.predict([features])
        return jsonify({"prediction": prediction.tolist()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(8001)  # Prometheus scrapes metrics from port 8001
    # Run Flask app
    app.run(host='0.0.0.0', port=5001)
