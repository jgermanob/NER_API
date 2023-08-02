"""
Script auxiliar para obtención de entidades nombradas utilizando la biblioteca 
SpaCy u el modelo en español 'es_core_news_sm'
"""

import spacy
from spacy import displacy

nlp = spacy.load('es_core_news_sm')

"""
Función para obtención de entidades nombradas de un texto.
Entrada:
    - Texto crudo de entrada
Salida:
    - Dicionario que contiene los siguientes campos:
        1) 'oracion': contiene el texto crudo de entrada
        2) 'entidades': contiene un diccionario con todas las entidades nombradas 
                        presentes en el texto con el formato 'entidad':etiqueta.
"""
def get_ner(text):
    ners = {}
    doc = nlp(text)
    for entity in doc.ents:
        ners[entity.text] = entity.label_
    
    output_dict = {'oracion':text, 'entidades':ners}

    return output_dict