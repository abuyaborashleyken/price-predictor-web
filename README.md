# House Price Estimator

A small Flask web application that estimates a property's price in Philippine pesos from its location and property details. It trains a scikit-learn Random Forest model on synthetic data when the app starts.

> **Note:** The model uses illustrative, synthetic data and approximate province price-per-square-meter values. Estimates are for learning purposes only and are not actual market valuations.

## Features

- Select a province or area.
- Enter floor area, bedrooms, bathrooms, property age, and distance to the city center.
- Get an estimated price in PHP.

Supported locations: Metro Manila, Cebu, Davao, Cavite, Laguna, Rizal, Bulacan, Pampanga, Batangas, Iloilo, Baguio, and Other province.

## Requirements

- Python 3.9 or later
- Flask
- NumPy
- pandas
- scikit-learn

## Run locally

From the project directory, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install Flask numpy pandas scikit-learn
```

Start the application:

```powershell
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

The development server runs with Flask debug mode enabled. Do not use it as-is for a production deployment.

## Project structure

```text
.
├── app.py
├── static/
│   └── style.css
└── templates/
    └── index.html
```
