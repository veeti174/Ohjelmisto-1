from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/<int:luku>')
def onkoAlkuluku(luku):
    onAlku = True   #alkuoletus: saatu luku on alkuluku

    if luku < 2:
        onAlku = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            onAlku = False
            break

    # Tulostetaan saadut vastaukset web-sivulle
    vastaus ={
        "Number" : {luku}, "isPrime" : "en tiiiä"
    }
    #  palauta vastaus web-sivulle
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    #localhost