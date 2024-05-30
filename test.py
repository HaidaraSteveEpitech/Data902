import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello, Streamlit!')

st.write("Voici un exemple d'application Streamlit.")

# Création d'un DataFrame
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

# Affichage du DataFrame
st.write(df)

# Ajout d'un widget interactif
if st.button('Say hello'):
    st.write('Hello!')

# Affichage d'un graphique
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
