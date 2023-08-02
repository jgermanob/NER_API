import spacy
from spacy import displacy

nlp = spacy.load('es_core_news_sm')

"""
Función get_ner para obtención de entidades nombradas de un texto.
Entrada:
    - Texto crudo de entrada
Salida:
    - Dicionario que contiene los siguientes campos:
        1) 'oracion': contiene el texto de crudo de entrada
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