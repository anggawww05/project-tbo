import nltk
from nltk import CFG

def validate_sentence(input_sentence, grammar_rules):
    words = input_sentence.split()
    chart_parser = nltk.ChartParser(grammar_rules)
    
    parsed_results = None
    try:
        parsed_results = list(chart_parser.parse(words))
    except Exception:
        return "Parsing error. Ensure the sentence follows the grammar!", None
    
    if parsed_results:
        return "Valid sentence!", parsed_results
    return "Sentence is not valid according to the grammar.", None
