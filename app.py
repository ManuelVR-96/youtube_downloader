from flask import Flask
from download import download
from flask_cors import CORS
from flask import Flask, jsonify
from flask import send_file




app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/ping')
def ping():
    yt = download('https://www.youtube.com/watch?v=Esdj9wlBOaI&ab_channel=FaztCode')
    #response = jsonify(str(yt.streams.first().download()))
    response = send_file('./viento.mp4', filename=yt.title)
    # response = jsonify({"saludo":"hola"})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)

    