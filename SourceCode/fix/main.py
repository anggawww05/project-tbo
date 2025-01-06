import nltk
from nltk import CFG
import streamlit as st
from cfg import create_cfg
from parsing import validate_sentence

def main():
    st.title("Parsing Kalimat Bahasa Bali")

    sentence = st.text_input("Masukkan kalimat:", "")

    grammar = create_cfg()

    if st.button("Validasi"):
        if sentence.strip():
            result, parses = validate_sentence(sentence, grammar)
            st.write(result)
            if parses:
                st.subheader("Derivasi:")
                for tree in parses:
                    st.text(tree)
        else:
            st.warning("Mohon masukkan kalimat terlebih dahulu!")

if __name__ == "__main__":
    main()
