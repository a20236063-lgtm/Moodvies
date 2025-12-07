import streamlit as st
import pandas as pd
import random
st.title("🎬 Moodvies")
st.subheader("Películas según tu estado de ánimo 🤍")
@st.cache_data
def cargar_datos():
    return pd.read_excel("pensamiento (2).xlsx")
peliculas = cargar_datos()
st.write("¿Cómo te sientes hoy?")
emociones = peliculas["EMOCIÓN"].unique().tolist()
emocion = st.selectbox("Elige una emoción:", emociones)
key_lista = f"lista_{emocion}"
key_mostrar = f"mostrar_{emocion}"
key_inicio = f"inicio_{emocion}"
if key_lista not in st.session_state:
    st.session_state[key_lista] = []
if key_mostrar not in st.session_state:
    st.session_state[key_mostrar] = False
if st.button("Confirmar emoción"):
    lista = peliculas[peliculas["EMOCIÓN"] == emocion]["PELÍCULAS"].tolist()
    random.shuffle(lista)
    st.session_state[key_lista] = lista
    st.session_state[key_mostrar] = True
    st.session_state[key_inicio] = False
if not st.session_state[key_mostrar]:
    st.stop()
st.write("Muy bien, tienes estas recomendaciones de películas para ti:")
lista_restante = st.session_state[key_lista]
if len(lista_restante) == 0:
    st.write("Listo, esas han sido todas las recomendaciones ❤️")
    st.stop()
recomendadas = lista_restante[:3]
st.session_state[key_lista] = lista_restante[3:]
for peli in recomendadas:
    st.write("•", peli)
st.write("¿Quieres otras recomendaciones?")
col1, col2 = st.columns(2)
with col1:
    if st.button("Sí"):
        st.write("Aquí tienes más:")
with col2:
    if st.button("No"):
        st.write("Me alegra que hayas encontrado tu película ideal. Mucha suerte 🍿✨")
        st.session_state[key_lista] = []
