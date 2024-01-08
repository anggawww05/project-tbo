import streamlit as st

from parsing_cyk import algortima_cyk

def tampilan_web():
    st.set_page_config(layout='centered', page_title="Parsing Kalimat Baku Bahasa Indonesia", menu_items={
        'About': f"""
        ## "Final Project Teori Bahasa dan Otomata"
        ##### Parsing kalimat baku bahasa Indonesia menggunakan algoritma CYK
        Oleh Kelompok 3 Kelas E :\n 
        I Ngurah Komang Agus Suryadiyatmika. S 		(2208561031)\n
        I Kadek Revan Aditya Prawira 				(2208561050)\n
        Devon Vivian Gunawan 	    				(2208561081)\n
        I Putu Aditya Pradana    					(2208561124)\n
        GitHub:
        """
    })
            
    st.write(f"<h1 style='text-align:center; '>Parsing Kalimat Baku Bahasa Indonesia</h1>", unsafe_allow_html=True)
    st.write(f"<h5 style='text-align:center; '>Menggunakan Algoritma CYK | Mata Kuliah Teori Bahasa dan Otmata</h5>", unsafe_allow_html=True)
    st.write(f"<p style='text-align:center; '>---- Kelompok 3 Kelas E -----</p>", unsafe_allow_html=True)
    
    input_kalimat = st.text_input('Masukkan Kalimat Anda :')
    list_string = input_kalimat.split(' ')
    
    button_click = st.button('Check', type='primary')

    if button_click:
        if len(list_string) <= 1: #list_string sudah berupa array, dengan index masing" adalah kata dari kalimat yang diinput
            st.error("Kalimat Tidak Boleh Kosong atau Hanya 1 kata!")
        elif input_kalimat != '':
            st.write('<h3>Hasil Parsing: </h3>', unsafe_allow_html=True)
            algortima_cyk(input_kalimat.split())




