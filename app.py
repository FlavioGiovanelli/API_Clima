import requests
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY = "API CENSURADA"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route("/clima", methods=["GET"])
def get_weather():
    cidade = request.args.get("cidade")
    if not cidade:
        return jsonify({"erro": "Informe uma cidade."}), 400
    
    params = {"q": cidade, "appid": API_KEY, "units": "metric", "lang": "pt"}
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code != 200:
        return jsonify({"erro": "Não foi possível obter os dados."}), response.status_code
    
    data = response.json()
    clima = {
        "cidade": data["name"],
        "temperatura": data["main"]["temp"],
        "descricao": data["weather"][0]["description"],
        "umidade": data["main"]["humidity"],
        "vento": data["wind"]["speed"]
    }
    
    return jsonify(clima)

if __name__ == "__main__":
    app.run(debug=True)

