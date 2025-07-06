# weather_visualization.py

import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ========== CONFIG ========== #
API_KEY = 'add41e2f02a0f3d3b3c808de115a056d'  # Replace with your actual OpenWeatherMap API key
cities = ['Ranchi', 'Mumbai', 'Kolkata', 'Chennai', 'Bengaluru']

# ========== DATA COLLECTION ========== #
temperatures = []
humidities = []

for city in cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    try:
        temperatures.append(data['main']['temp'])
        humidities.append(data['main']['humidity'])
    except KeyError:
        print(f"Could not fetch data for {city}. Response: {data}")
        temperatures.append(None)
        humidities.append(None)

# ========== VISUALIZATION ========== #
sns.set(style="whitegrid")

# --- Temperature Plot --- #
plt.figure(figsize=(10, 5))
sns.barplot(x=cities, y=temperatures, palette="coolwarm")
plt.title("Current Temperature in Indian Cities")
plt.ylabel("Temperature (°C)")
plt.xlabel("City")
plt.tight_layout()
plt.savefig("temperature_plot.png")
plt.show()

# --- Humidity Plot --- #
plt.figure(figsize=(10, 5))
sns.barplot(x=cities, y=humidities, palette="Blues")
plt.title("Current Humidity in Indian Cities")
plt.ylabel("Humidity (%)")
plt.xlabel("City")
plt.tight_layout()
plt.savefig("humidity_plot.png")
plt.show()

# ========== END ========== #
print("Weather data visualization completed successfully.")
