import nltk
from nltk import CFG

def validate_sentence(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    tokens = sentence.split()
    try:
        parses = list(parser.parse(tokens))
        if parses:
            return "Kalimat valid!", parses
    except Exception:
        return "Parsing gagal. Pastikan kalimat sesuai dengan grammar!", None
    return "Kalimat tidak valid!", None