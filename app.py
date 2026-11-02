from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)

# ---- Presyo per sqm kada probinsya (illustrative lang, hindi totoong market data) ----
PROVINCES = {
    'Metro Manila': 120000,
    'Cebu': 70000,
    'Davao': 60000,
    'Cavite': 55000,
    'Laguna': 55000,
    'Rizal': 50000,
    'Bulacan': 48000,
    'Pampanga': 45000,
    'Batangas': 42000,
    'Iloilo': 40000,
    'Baguio': 65000,
    'Other province': 30000,
}

# ---- Gawa ng dataset ----
np.random.seed(42)
n = 300

chosen_provinces = np.random.choice(list(PROVINCES.keys()), n)
price_per_sqm = np.array([PROVINCES[p] for p in chosen_provinces])

df = pd.DataFrame({
    'floor_area_sqm': np.random.randint(20, 300, n),
    'bedrooms': np.random.randint(1, 6, n),
    'bathrooms': np.random.randint(1, 4, n),
    'age_years': np.random.randint(0, 40, n),
    'distance_to_cbd_km': np.round(np.random.uniform(0.5, 50, n), 1),
    'price_per_sqm': price_per_sqm,
})

df['price_php'] = (
    df['floor_area_sqm'] * df['price_per_sqm']
    + df['bedrooms'] * 150_000
    - df['age_years'] * 20_000
    - df['distance_to_cbd_km'] * 15_000
    + np.random.normal(0, 300_000, n)
).clip(lower=500_000)

X = df.drop('price_php', axis=1)
y = df['price_php']

# ---- I-train ang Random Forest ----
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)


@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        selected_province = request.form['province']
        sample_input = pd.DataFrame([{
            'floor_area_sqm': float(request.form['floor_area_sqm']),
            'bedrooms': int(request.form['bedrooms']),
            'bathrooms': int(request.form['bathrooms']),
            'age_years': int(request.form['age_years']),
            'distance_to_cbd_km': float(request.form['distance_to_cbd_km']),
            'price_per_sqm': PROVINCES[selected_province],
        }])
        predicted_price = model.predict(sample_input)[0]
        prediction = f"₱{predicted_price:,.0f}"

    return render_template('index.html', prediction=prediction, provinces=PROVINCES.keys())


if __name__ == '__main__':
    app.run(debug=True)