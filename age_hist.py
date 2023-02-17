import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def age(df):
    
    df['fecha_nac'] = pd.to_datetime(df['date_birth'], errors = 'coerce')
    df['fecha_nac'] = pd.to_datetime(df['fecha_nac'])
    df['Año'] = df['fecha_nac'].dt.year
    ahora = 2022
    df['Edad'] = (ahora - df['Año'])
    df = df.drop(df[df['Edad']<1].index)
    df = df.drop(df[df['Edad']>95].index)
    df = df.dropna(subset='Edad')

    df.to_csv('./data/travel_traveller_age.csv')

    bins = np.arange(df['Edad'].min(), df['Edad'].max() + 1, 1)
    promedio = 'Promedio ' + str(round(df['Edad'].mean(),2))
    plt.figure(figsize=(25, 16))
    plt.hist(df['Edad'], bins = bins, edgecolor = 'black')
    plt.xlabel('Edad')
    plt.ylabel('Cantidad de viajeros')
    plt.title('Viajeros por Edad')
    plt.axvline(df['Edad'].mean(), color='b', linestyle='dashed', linewidth=2, label= promedio )
    plt.legend()
    plt.savefig('./graficos/histograma_edad.png')
    plt.show()
