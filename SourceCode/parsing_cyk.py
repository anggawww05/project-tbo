import streamlit as st
from rules import RULES_CFG

class LeftCornerParser:
    def __init__(self, rules):
        self.rules = rules
        self.table = []

    def parse(self, tokens):
        self.table = [[[] for _ in range(len(tokens) + 1)] for _ in range(len(tokens))]
        for i, token in enumerate(tokens):
            for lhs, rhs in self.rules.items():
                if rhs == [token]:
                    self.table[i][i + 1].append(lhs)
        for length in range(2, len(tokens) + 1):
            for start in range(len(tokens) - length + 1):
                end = start + length
                for mid in range(start + 1, end):
                    for lhs, rhs in self.rules.items():
                        if len(rhs) == 2 and rhs[0] in self.table[start][mid] and rhs[1] in self.table[mid][end]:
                            self.table[start][end].append(lhs)
        return 'S' in self.table[0][len(tokens)]

parser = LeftCornerParser(RULES_CFG)

def main():
    st.title("Left Corner Parser")
    input_string = st.text_input("Enter a string to parse:")
    if input_string:
        tokens = input_string.split()
        if parser.parse(tokens):
            st.success("The string is accepted by the grammar.")
        else:
            st.error("The string is not accepted by the grammar.")

if __name__ == "__main__":
    main()
