from flask import Flask, render_template, request
from weather import Weather, WeatherAPIError  # Import kelas dari weather.py

app = Flask(__name__)
API_KEY = "f812ed05b4acdb9da54426b656f1eb81"

app.secret_key = "346CCC3E68FE2565A6652F33F1F1E"

# Initialize the Weather client with the correct variable name
weather_client = Weather(api_key=API_KEY)  # Inisialisasi objek weather

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error_message = None

    if request.method == "POST":
        city_name = request.form.get("city_name")
        if not city_name:
            error_message = "Nama kota tidak boleh kosong."
        else:
            try:
                # Mengambil data cuaca menggunakan kelas weather
                weather = weather_client.get_weather_by_city(city_name)
            except WeatherAPIError as e:
                error_message = str(e)

    # Ensure the return statement is correctly indented and within the function
    return render_template("index.html", weather=weather, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
