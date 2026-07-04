# Temperatura do Dia - Venda de Sorvetes - Exercícios de previsões

import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np


st.header('Temperatura do Dia - Venda de Sorvetes')

temp = pd.read_csv('dados.csv')

st.line_chart(temp, x = 'temperatura', y= 'qtdeVendas')
modelo_sorveteria = LinearRegression() 
modelo_sorveteria.fit(temp[['qtdeVendas']], temp['temperatura'])



temp_sorvete = st.number_input('Temperatura do Dia', value = 0)
n = np.array(temp_sorvete)
qtde_final = modelo_sorveteria.predict([[temp_sorvete]])
print(qtde_final)


st.metric(f'Você venderia ' ,f'{min(qtde_final[0], 200.0):.1f} Sorteves ')