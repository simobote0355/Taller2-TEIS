from flask import Flask, jsonify, render_template
from utils.pokeneas import get_pokenea
from utils.container import get_container_id

app = Flask(__name__)

@app.route("/info")
def info_pokenea():
    pokenea = get_pokenea()  
    contenedor_id = get_container_id()
    pokenea["contenedor_id"] = contenedor_id

    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor": pokenea["contenedor_id"]
    })

@app.route("/img")
def img_pokenea():
    pokenea = get_pokenea()
    contenedor_id = get_container_id()
    pokenea["contenedor_id"] = contenedor_id

    return render_template("pokeneas.html",
                           nombre = pokenea["nombre"],
                           image = pokenea["imagen"],
                           frase = pokenea["frase"],
                           contenedor = pokenea["contenedor_id"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
