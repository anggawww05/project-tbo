RULES_CFG = {
    "K": [["S", "P"], ["S", "P", "O"], ["S", "P", "Ket"], ["S", "P", "O", "Ket"], ["S", "P", "Pel"], ["S", "P", "O", "Pel"], ["S", "P", "O", "Pel", "Ket"]],
    "S": [["NP"]],
    "NP": [["Pronoun", "Det"], ["Noun"], ["Pronoun"]],
    "P": [["VP"]],
    "VP": [["Adv", "Verb"], ["Verb"], ["Prep", "VP"], ["Adv", "VP"]],
    "O": [["NP"]],
    "Ket": [["PP"]],
    "PP": [["PP", "NP"], ["Prep"]],
    "Pel": [["NP"], ["Adjp"]],
    "Adjp": [["Adjp", "Adv"], ["Adj"]],
    "Pronoun": [["Ia"], ["anake"], ["adinne"]],
    "Noun": [["roko"], ["paon"], ["wastra"], ["tukad"], ["buku"], ["warung"], ["i meme"], ["putu agus"], ["nyoman"], ["nasi"]],
    "Verb": [["melali"], ["mablanja"], ["nyakan"], ["ngumbah"], ["melajah"], ["meliang"], ["medaar"]],
    "Adj": [["seleg"], ["liu"]],
    "Adv": [["pisan"], ["sesai"], ["jagi"]],
    "Prep": [["di"]],
    "Det": [["ento"]]
}
