import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------- SETTINGS -----------------------
API_KEY = "f1cce9649e88c83028cca25a440193a1"  # Replace with your actual API key
CITY = "Solapur"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ----------------------- FETCH DATA -----------------------
response = requests.get(URL)
data = response.json()

if response.status_code != 200 or 'list' not in data:
    print("Error: Check API key or city name.")
    exit()

# ----------------------- EXTRACT DATA -----------------------
weather_data = []
for entry in data['list']:
    weather_data.append({
        'datetime': entry['dt_txt'],
        'temperature': entry['main']['temp'],
        'humidity': entry['main']['humidity'],
        'weather': entry['weather'][0]['main']
    })

df = pd.DataFrame(weather_data)

# ----------------------- VISUALIZATION -----------------------
sns.set(style="whitegrid")

# Temperature over time
plt.figure(figsize=(12,6))
sns.lineplot(x='datetime', y='temperature', data=df, marker='o', color='orange')
plt.xticks(rotation=45)
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()

# Humidity over time
plt.figure(figsize=(12,6))
sns.lineplot(x='datetime', y='humidity', data=df, marker='o', color='blue')
plt.xticks(rotation=45)
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date and Time')
plt.ylabel('Humidity (%)')
plt.tight_layout()
plt.show()

# Weather type frequency
plt.figure(figsize=(10,6))
sns.countplot(x='weather', data=df, palette='viridis')
plt.title(f'Weather Type Frequency for {CITY}')
plt.xlabel('Weather Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()