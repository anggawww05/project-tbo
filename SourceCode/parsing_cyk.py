import streamlit as st
from rules import RULES_CFG


def algortima_cyk(kalimat):
    banyak_kata = len(kalimat)
    
    # ✅ Corrected initialization: Use empty lists instead of " "
    T = [[[] for _ in range(banyak_kata)] for _ in range(banyak_kata)]
    
    # ✅ Step 1: Filling the diagonal with terminal symbols
    for j in range(banyak_kata):
        for LHS, rule in RULES_CFG.items():
            for RHS in rule:
                if len(RHS) == 1 and RHS[0] == kalimat[j]:    
                    T[j][j].append(LHS)  # ✅ Corrected: use append() instead of +=
    
    # ✅ Step 2: Filling the upper triangle of the table
    for j in range(banyak_kata):
        for i in range(j, -1, -1):
            for k in range(i, j):
                for LHS, rule in RULES_CFG.items():
                    for RHS in rule:
                        # ✅ Check if both RHS parts exist in the table
                        if len(RHS) == 2 and RHS[0] in T[i][k] and RHS[1] in T[k+1][j]:
                            T[i][j].append(LHS)  # ✅ Corrected: use append() instead of +=
    
    # ✅ Step 3: Check if the start symbol "K" is in the top-right cell
    if "K" in T[0][banyak_kata-1]:
        st.success("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat VALID")
        st.write('<h3>Filling Table:</h3>', unsafe_allow_html=True)
        st.table(T)
    else:
        st.error("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat TIDAK VALID")
        st.table(T)
