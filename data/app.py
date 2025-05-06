from flask import Flask, request, jsonify
from ebay_api import buscar_productos_ebay

app = Flask(__name__)

@app.route("/buscar", methods=["GET"])
def buscar():
    producto = request.args.get("producto")
    if not producto:
        return jsonify({"error": "Falta el parámetro 'producto'"}), 400

    resultados = buscar_productos_ebay(producto)
    return jsonify({"resultados": resultados})

if __name__ == "__main__":
    app.run(debug=True, port=8000)
