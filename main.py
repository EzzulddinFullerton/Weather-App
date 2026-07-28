import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter city name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI Emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)


    def get_weather(self):
        city = self.city_input.text()
        city = city.replace(" ", "+")
        geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json"


        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()


        try:
            if geocode_data["results"]:
                latitude = geocode_data["results"][0]["latitude"]
                longitude = geocode_data["results"][0]["longitude"]
        except KeyError:
            self.display_error("City not found")
            return
        

        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weather_code&temperature_unit=fahrenheit"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()

            self.display_weather(data)

        except requests.exceptions.RequestException as e:
            self.display_error(f"Error: {e}")
        except requests.exceptions.HTTPError as e:
            self.display_error(f"HTTP Error: {e}")
        except requests.exceptions.ConnectionError as e:
            self.display_error(f"Connection Error: {e}")
        except requests.exceptions.Timeout as e:
            self.display_error(f"Timeout Error: {e}")
        except requests.exceptions.TooManyRedirects as e:
            self.display_error(f"Too Many Redirects Error: {e}")
        

    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 75px;")
        temperature = data["current"]["temperature_2m"]
        self.temperature_label.setText(f"{temperature:.1f}°F")
        weather_description = data["current"]["weather_code"]
        if weather_description == 0 or weather_description == 1:
            self.description_label.setText("Clear Sky")
            self.emoji_label.setText("☀️")
        elif weather_description >= 2 and weather_description <= 3:
            self.description_label.setText("Cloudy")
            self.emoji_label.setText("⛅️")
        elif weather_description == 45 or weather_description == 48:
            self.description_label.setText("Foggy")
            self.emoji_label.setText("⛅️")
        elif weather_description == 51 or weather_description == 53 or weather_description == 55 or weather_description == 56 or weather_description == 57:
            self.description_label.setText("Drizzle")
            self.emoji_label.setText("🌧️")
        elif weather_description == 61 or weather_description == 63 or weather_description == 65 or weather_description == 66 or weather_description == 67:
            self.description_label.setText("Rain")
            self.emoji_label.setText("🌧️")
        elif weather_description == 71 or weather_description == 73 or weather_description == 75 or weather_description == 77 or weather_description == 85 or weather_description == 86:
            self.description_label.setText("Snow")
            self.emoji_label.setText("⛄️")
        elif weather_description == 80 or weather_description == 81 or weather_description == 82:
            self.description_label.setText("Rain Shower")
            self.emoji_label.setText("🌧️")
        elif weather_description == 95 or weather_description == 96 or weather_description == 99:
            self.description_label.setText("Thunderstorm")
            self.emoji_label.setText("⛈️")
        else:
            self.description_label.setText("Unknown Weather")
            self.emoji_label.setText("❓")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())