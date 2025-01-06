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

def algortima_cyk(kalimat):

    banyak_kata = len(kalimat)
    T = [[" " for j in range(banyak_kata)] for i in range(banyak_kata)]
    
    for j in range(0, banyak_kata):
        for LHS, rule in RULES_CFG.items():
            for RHS in rule:
                if len(RHS) == 1 and RHS[0] == kalimat[j]:    
                    T[j][j] += LHS + " "

    for j in range(0, banyak_kata):
        for i in range(j, -1, -1):
            for k in range(i, j):
                for LHS, rule in RULES_CFG.items():
                    for RHS in rule:
                        if len(RHS) == 2 and RHS[0] in T[i][k].split() and RHS[1] in T[k+1][j].split():
                            T[i][j] += LHS + " "
                                
    if "K" in T[0][banyak_kata-1].split():
        # print("True")
        st.success("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat VALID")
        st.write('<h3>Filling Table:</h3>', unsafe_allow_html=True)
        st.table(T)
        
    else:
        # print("False")
        st.error("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat TIDAK VALID")
        st.table(T)

