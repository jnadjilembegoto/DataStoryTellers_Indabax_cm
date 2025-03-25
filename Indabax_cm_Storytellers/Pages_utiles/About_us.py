import streamlit as st
from PIL import Image
from Photos.photo_link import main_dir




def about_us_page():
    
    st.title("À propos de nous")
    st.write("""
    La Data Stotytellers Team est constitué de Cinq élèves ingénieurs statisticiens économistes en formation à l'ISSEA.
             
    """)
    st.markdown('---')
    dylan = Image.open(main_dir("dylan.jpg"))
    dylan = dylan.resize((200,300))
    st.markdown(
        f"""
        ##### AZABMO TAZO Dilane 
        """,
        unsafe_allow_html=True,
    )
    col_im,col_ad=st.columns(2)
    with col_im:
        st.image(dylan,use_column_width=False)
    with col_ad:
        st.markdown(
        f"""
        - 📧 Email:  <student.dilane.tazo@issea-cemac.org> ou <dilanetazo007@gmail.org>
        - Linkedin:  https://www.linkedin.com/in/dilane-tazo
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')

    mpolah = Image.open(main_dir("mpolah.jpg"))
    mpolah = mpolah.resize((200,300))
    st.markdown(
        f"""
        ##### MPOLAH SOH Natacha Flaire
        """,
        unsafe_allow_html=True,
    )
    col_im,col_ad=st.columns(2)
    with col_im:
        st.image(mpolah,use_column_width=False)
    with col_ad:
        st.markdown(
        f"""
        - 📧 Email:  <fortunempolah@gmail.com>
        - Linkedin:  http://www.linkedin.com/in/flaire-natacha-mpolah-soh-75b324268
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')

    nadji = Image.open(main_dir("nadji.jpg"))
    nadji = nadji.resize((200,300))
    st.markdown(
        f"""
        ##### NADJILEM BEGOTO
        """,
        unsafe_allow_html=True,
    )
    col_im,col_ad=st.columns(2)
    with col_im:
        st.image(nadji,use_column_width=False)
    with col_ad:
        st.markdown(
        f"""
        - 📧 Email:  <jnadjilembegoto@gmail.com> ou <student.begoto.nadjilem@issea-cemac.org>
        - Linkedin:  https://www.linkedin.com/in/bégoto-nadjilem-192b8617b
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')
     

    tbc = Image.open(main_dir("tbc.jpg"))
    tbc = tbc.resize((200,300))
    st.markdown(
        f"""
        ##### TEYANBAYE BERTORNGAÏ Christian
        """,
        unsafe_allow_html=True,
    )
    col_im,col_ad=st.columns(2)
    with col_im:
        st.image(tbc,use_column_width=False)
    with col_ad:
        st.markdown(
        f"""
        - 📧 Email:  <teyanchrist@gmail.com> ou <student.christian.teyanbaye@issea-cemac.org>
        - Linkedin:  https://www.linkedin.com/in/christian-teyanbaye-berto
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')

    
    tiao = Image.open(main_dir("tiao.jpg"))
    tiao = tiao.resize((200,300))
    st.markdown(
        f"""
        ##### TIAO Eliasse
        """,
        unsafe_allow_html=True,
    )
    col_im,col_ad=st.columns(2)
    with col_im:
        st.image(tiao,use_column_width=False)
    with col_ad:
        st.markdown(
        f"""
        - 📧 Email:  <eliassetiao@gmail.com>
        - Linkedin:  https://www.linkedin.com/in/eliasse-tiao-781523309/
        """,
        unsafe_allow_html=True,
    )
    st.markdown('---')

    
