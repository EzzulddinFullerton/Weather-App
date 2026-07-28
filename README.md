---

# ☀️ PyQt5 Weather App

A clean, modern desktop weather application built with **Python**, **PyQt5**, and the **Open-Meteo API**. This application fetches real-time weather data based on city names without requiring an API key.

---

## 🚀 Features

* **City Search**: Search weather conditions for any city worldwide using geocoding.
* **Real-Time Data**: Displays current temperature in Fahrenheit along with visual weather descriptions.
* **Emoji Status**: Maps WMO weather codes to dynamic emojis (☀️, 🌧️, ❄️, etc.).
* **Custom Styled UI**: Styled using Qt CSS for a clean, bold layout.
* **No API Key Required**: Built entirely on the free, open-source Open-Meteo API.

---

## 🛠️ Prerequisites & Requirements

Make sure you have **Python 3.x** installed on your system. You will also need the following Python packages:

* `PyQt5` (For the Graphical User Interface)
* `requests` (For making API calls)

---

## 📦 Installation & Setup

1. **Clone the repository**:
```bash
git clone https://github.com/EzzulddinFullerton/Weather-App.git
cd repo-name

```


2. **Install required dependencies**:
```bash
pip install PyQt5 requests

```


3. **Run the application**:
```bash
python main.py

```

---

## 📡 API Usage

This project uses the following free endpoints provided by **Open-Meteo**:

* **Geocoding API**: Converts city names into latitude and longitude coordinates.
* **Forecast API**: Retrieves current temperature (`temperature_2m`) and WMO weather codes (`weather_code`).

---

## 📜 License

This project is open-source and available under the MIT License.
