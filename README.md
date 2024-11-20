# Flask ML API with Prometheus Monitoring

This project provides a Flask-based API for serving machine learning models and integrates Prometheus for monitoring metrics such as inference requests and latency.

---

## **Features**
- Serve predictions from a trained machine learning model.
- Monitor key metrics using Prometheus.
- Track requests and latency for better performance insights.

---

## **Getting Started**

### **1. Clone the Repository**
```bash
git clone <repository-url>
cd <repository-directory>
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Running the Flask API Locally**

### **1. Start the Flask API**
Run the application locally:
```bash
python app.py
```

### **2. Test the API**
Send a POST request to the `/predict` endpoint using `curl` or Postman.

#### Example Request (using `curl`):
```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

#### Expected Response:
```json
{
  "prediction": [0]
}
```

---

## **Monitoring with Prometheus**


```

### **1. Start Prometheus**
Run Prometheus using the configuration file:
```bash
prometheus --config.file=prometheus.yml
```

### **2. Access Prometheus Dashboard**
Open your browser and visit [http://localhost:9090](http://localhost:9090). Use the following queries to monitor metrics:
- **Total Inference Requests**:
  ```promql
  inference_requests_total
  ```
- **Latency Distribution**:
  ```promql
  inference_latency_seconds_count
  ```

---

## **Project Structure**
```
.
├── app.py                # Main Flask application
├── model.pkl             # Trained ML model
├── prometheus.yml        # Prometheus configuration
├── requirements.txt      # Python dependencies
```

---

## **Future Enhancements**
- Add model versioning and A/B testing.
- Integrate Grafana for advanced dashboard visualization.
- Set up Kubernetes for scalable deployment.




