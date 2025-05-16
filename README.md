# Fraud Management System (Flask API)

## Overview
This Flask-based service simulates real-time transaction monitoring, applies rule-based and ML classification, and returns fraud cases.

## API Endpoint

### POST /fraud/run
- **Description**: Runs the fraud pipeline.
- **Body**:
  ```json
  { "n": 1000 }
