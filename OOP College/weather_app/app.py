from flask import Flask, render_template, request, flash
import requests

app = Flask(__name__)
app.secret_key = "346CCC3E68FE2565A6652F33F1F1E"

API_KEY = "f812ed05b4acdb9da54426b656f1eb81"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error_message = None

    if request.method == "POST":
        city_name = request.form.get("city_name")
        try:
            # URL API Open WeatherMap
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric&lang=id"
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

            # Parse data cuaca
            weather = response.json()

        except requests.exceptions.HTTPError as http_err:  # Corrected here
            error_message = f"HTTP Error: {http_err}"
        except requests.exceptions.ConnectionError:  # Corrected here
            error_message = "Gagal terhubung ke server. Silakan cek koneksi internet Anda."
        except requests.exceptions.Timeout:  # Corrected here
            error_message = "Permintaan ke server waktu habis. Silakan coba lagi nanti."
        except requests.exceptions.RequestException as req_err:  # Corrected here
            error_message = f"Terjadi kesalahan: {req_err}"
        except Exception as e:
            error_message = f"Kesalahan tak terduga: {e}"

    return render_template("index.html", weather=weather, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)
