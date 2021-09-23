from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route('/modelo/holamundo', methods=['GET'])
@cross_origin()
def ScreamingallDiary():
    return jsonify({"respuesta": "Hola Mundo"})

def main():
    app.run(host= "0.0.0.0", port="4050", debug=True)

if __name__ == '__main__':
    try:
        main()

    except KeyboardInterrupt:
        print("Saliendo")
        exit()