import streamlit as st
import pandas as pd
import random

# Título
st.title("🎬 Recomendador de Películas según tu emoción")

# Emociones
emociones = [
    "Alegría", "Tristeza", "Enojo", "Miedo", "Justicia",
    "Nostálgia", "Romance", "Intriga", "Ternura"
]

# Cargar Excel
peliculas = pd.read_excel('pensamiento (2).xlsx')

# Selección de emoción
emocion_seleccionada = st.selectbox("¿Cómo te sientes hoy?", emociones)

if emocion_seleccionada:
    lista_peliculas = peliculas[peliculas["EMOCIÓN"] == emocion_seleccionada]["PELÍCULAS"].tolist()
    random.shuffle(lista_peliculas)

    st.subheader(f"Películas para cuando sientes: {emocion_seleccionada}")

    # Mostrar 3 cada vez
    if "index" not in st.session_state:
        st.session_state.index = 0

    if st.button("Mostrar recomendaciones"):
        fin = st.session_state.index + 3
        subset = lista_peliculas[st.session_state.index:fin]

        if subset:
            for peli in subset:
                st.write("🍿", peli)
            st.session_state.index = fin
        else:
            st.write("❤️ ¡Ya no hay más recomendaciones!")
