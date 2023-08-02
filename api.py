from flask import Flask, request, jsonify
import traceback
import sys
from ner import get_ner

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Lectura de json de la petición POST
        json_ = request.json
        # Almacenamiento de las oraciones de entrada en una lista
        texts = json_['oraciones']
        # Lista para guardar los diccionarios de salida
        outputs = []

        """
        Ciclo for para obtener las entidades nombradas de cada texto de entrada.
        La función get_ner devuelve un diccionario con la estructura {'oracion':text, 'entidades':{'entidad': etiqueta}}
        Se devuelve un json de salida con la siguiente estructura: {'resultado':{'oracion':text, 'entidades':{'entidad':etiqueta}}}
        """
        for text in texts:
            ner_text = get_ner(text)
            outputs.append(ner_text)

        return jsonify({'resultado':outputs})
    
    except:
        # Manejo de excepciones para errores durante la ejecución
        return jsonify({'trace': traceback.format_exc()})

if __name__ == '__main__':
    try:
        # Puerto espcificado en línea de comando
        port = int(sys.argv[1])
    except:
        # Puerto por defecto por el corre el API
        port = 23456
    
    app.run(port=port, debug=True)