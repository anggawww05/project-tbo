RULES_CFG = {
    "K": [["S", "P"], ["NP", "VP"]],  # Top-level rule allows S P or direct NP VP
    "S": [["NP"]],  # S explicitly maps to NP
    "P": [["VP"]],  # P explicitly maps to VP
    "NP": [["Pronoun", "Det"], ["Pronoun"], ["Noun"]],  # Define NP with variations
    "VP": [["Adv", "Verb"], ["Verb"], ["Adv", "VP"], ["Prep", "VP"]],  # Define VP
    "X1": [["P", "O"], ["P", "Ket"], ["P", "Pel"], ["P", "X2"]],
    "X2": [["O", "Ket"], ["O", "Pel"], ["O", "X3"]],
    "X3": [["Pel", "Ket"]],
    "O": [["NP"]],
    "Ket": [["PP"]],
    "PP": [["Prep", "NP"], ["Prep"]],  # Fixed rule for PP (prep phrases)
    "Pel": [["NP"], ["Adjp"]],
    "Adjp": [["Adj", "Adv"], ["Adj"]],
    "Pronoun": [["Ia"], ["anake"], ["adinne"]],
    "Noun": [["roko"], ["paon"], ["wastra"], ["tukad"], ["buku"], ["warung"], ["i meme"], ["putu agus"], ["nyoman"], ["nasi"]],
    "Verb": [["melali"], ["mablanja"], ["nyakan"], ["ngumbah"], ["melajah"], ["meliang"], ["medaar"]],
    "Adj": [["seleg"], ["liu"]],
    "Adv": [["pisan"], ["sesai"], ["jagi"]],
    "Prep": [["di"]],
    "Det": [["ento"]]
}
