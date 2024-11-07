import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/joku-juttu')
def pritn_joku_juttu():
    return 'Siinä sulle joku kolmas juttu!'

@app.route('/sum')
def calculate_sum():
    #print(request.args.get('num2'))
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
    except ValueError:
        return 'Parameter error: use numbers!'
    except TypeError:
        return 'Parameter(s) missing'
    return {
        "function": "calculate sum of two values",
        "result":num1+ num2
    }

# "mock data" ns, tekstidata
names = ['Aku', 'Iines', 'Hannu', 'Heluna']

#lähetetään kaikki nimet json muodossa
@app.route('/names')
def get_names():
        return {"names": names}

@app.route('/names/<id>')
def get_name(id):
    try:
        result = {"id": id, "name": names[int(id)]}
    except IndexError:
        #status-koodin vaihtaminen vaatii oma response-olion luonnin
        res_body = {"error": "not found"}
        # muutetaan sanakkiraja -> json-muotoinen merkkijono
        res_body = json.dumps(res_body)
        response = Response(status=404, responses=res_body,
                            content_Type="application/json")
        return response
    return result

# yleinen virheenkäsittelu 404 virheille
@app.errorhandler(404)
def not_found(error):
    #print(error)
    #print(request.path)
    res_body = {"requested route": request.path, "error": "not found"}
    # muutetaan sanakkiraja -> json-muotoinen merkkijono
    res_body = json.dumps(res_body)
    response = Response(status=404, responses=res_body,
                        content_Type="application/json")
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, port=3000)
