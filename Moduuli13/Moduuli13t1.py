from flask import Flask

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def onkoAlku(luku):

    onAlkuLuku = True       # alkuoletus: saatu luku on alkuluku

    if luku < 2:
        onAlkuLuku = False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            # luku oli jaollinen muullakin kuin 1 ja itsellään
            # -> EI ole alkuluku
            onAlkuLuku = False
            break               # lopettaa for-toistolauseen

    vastaus = {
        "Number" : luku,
        "isPrime" : onAlkuLuku
    }

    # palautetaan data selaimelle
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)