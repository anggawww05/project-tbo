import streamlit as st
from rules import RULES_CFG

def algortima_cyk(kalimat):
    empty = '\u2205'
    banyak_kata = len(kalimat)
    T = [[" " for j in range(banyak_kata)] for i in range(banyak_kata)]
    # filling_table = [[" " for j in range(banyak_kata)] for i in range(banyak_kata)]
    
    # print(T);

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
    # print(T)
                                
    if "K" in T[0][banyak_kata-1].split():
        print("True")
        st.success("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat VALID")
        st.write('<h3>Filling Table:</h3>', unsafe_allow_html=True)
        st.table(T)
        
    else:
        print("False")
        st.error("Berdasarkan hasil pemeriksaan, kalimat yang diinputkan adalah kalimat TIDAK VALID")
    
        
# algortima_cyk("Kiki tertidur di kampus".split())