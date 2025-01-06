import streamlit as st
from parsing_cyk import algortima_cyk

st.set_page_config(layout='centered', page_title="Parsing Kalimat Baku Bahasa Bali", menu_items={
    'About': f"""
    ## "Final Project Teori Bahasa dan Otomata"
    ##### Dengan algoritma CYK
    Oleh Kelompok 1 Kelas C :\n 
    Mirza Ali Fahlevi (2308561003)\n
    I Dewa Ayu Agung Rai Ratna Karang (2308561021)\n
    I Putu Andika Arsana Putra (2308561063)\n
    Anak Agung Gede Angga Putra Wibawa (2308561099)\n
    GitHub:
    """
})

def tampilan_web():
    st.write(f"<h1 style='text-align:center; color:yellow;'>Parsing Kalimat Bahasa Bali</h1>", unsafe_allow_html=True)
    st.write(f"<h5 style='text-align:center;'>Dengan Algoritma CYK</h5>", unsafe_allow_html=True)
    st.write(f"<p style='text-align:center;'>Kelompok 1 Kelas C</p>", unsafe_allow_html=True)
    
    st.write("---")
    
    input_kalimat = st.text_input('Masukkan Kalimat Bahasa Bali:', placeholder='Masukkan kalimat bahasa bali')
    list_string = input_kalimat.split()  

    button_click = st.button('Check', type='primary', key='centered_button')
    st.markdown(
        """
        <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if button_click:
        if len(list_string) <= 1:
            st.error("Kalimat Tidak Boleh Kosong atau Hanya 1 kata!")
        else:
            st.write('<h3>Hasil Parsing: </h3>', unsafe_allow_html=True)
            result = algortima_cyk(list_string)
            st.write(result)


if __name__ == "__main__":
    tampilan_web()
