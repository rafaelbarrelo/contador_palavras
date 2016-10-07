import re
import requests
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def conta_palavras(url, palavra):
    retorno = 0
    try:
        r = requests.get(url)
        if r.status_code == requests.codes.ok:
            retorno = (len(re.findall(re.escape(palavra), r.text, re.IGNORECASE)))
    except:
        print('Url invalida: ' + url)
        retorno = 0

    return retorno

class Home(Resource):
    def get(self):
        return {'exemplo': '/url/palavra'}


class Contador(Resource):
    def get(self, url, palavra):
        return {palavra: conta_palavras(url, palavra)}

api.add_resource(Home, '/')
api.add_resource(Contador, '/<path:url>/<string:palavra>')

if __name__ == '__main__':
    app.run(debug=True)

