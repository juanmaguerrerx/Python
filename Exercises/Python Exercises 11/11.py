import os
import matplotlib.pyplot as plt
import pandas as pd


archivo_csv = '11-e.csv'
dataframe = pd.read_csv(archivo_csv)

print(dataframe.head())

plt.plot(dataframe['Month'], dataframe['Sevilla'], label='Sevilla')
plt.plot(dataframe['Month'], dataframe['Huelva'], label='Huelva')

plt.xlabel('Month')
plt.ylabel('Número de Ciudades')
plt.title('Gráfica de Ciudades en Sevilla y Huelva por Mes')
plt.legend()
plt.show()
