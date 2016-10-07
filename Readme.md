# Contador de Palavras

Api Flask que recebe uma URL e uma palavra e retorna a quantidade de palavras na URL.

### Para executar
```sh
$ mkdir contador_palavras
$ cd contador_palavras
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python contador.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
```

###### Endpoint
http://127.0.0.1:5000/ `<url>` / `<palavra>`

###### Retorno
{ `<palavra>`: `quantidade` }

### Exemplo de utilização
http://127.0.0.1:5000/_http://rafael.barrelo.com.br_/_rafael_

`{ "rafael" : 8 }`

> Busca a quantidade de 'rafael' em http://rafael.barrelo.com.br, e retorna um `json` com a palavra e a quantidade.

---