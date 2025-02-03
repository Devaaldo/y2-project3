import requests

class WeatherAPIError(Exception):
    """Exception untuk error API OpenWeatherMap."""
    def __init__(self, message="Gagal mendapatkan data dari API OpenWeatherMap"):
        super().__init__(message)

class Weather:
    """Kelas untuk mengelola data cuaca menggunakan API OpenWeatherMap."""
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def get_weather_by_city(self, city_name):
        """Mengambil data cuaca berdasarkan nama kota."""
        params = {
            "q" : city_name,
            "appid" : self.api_key,
            "units" : "metric",
            "lang" : "id" #Bahasa Indonesia
        }
        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status() # Memunculkan HTTPError jika status kode bukan 200
            data = response.json()
            if data.get("cod") != 200:
                raise WeatherAPIError(f"Error dari API: {data.get('message')}")
            return data
        except requests.exceptions.RequestException as e:
            raise WeatherAPIError(f"Kesalahan koneksi: {e}")
        except Exception as e:
            raise WeatherAPIError(f"Kesalahan tak terduga: {e}")
    
    return render_template("index.html", weather=weather, error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)