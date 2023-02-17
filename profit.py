import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def profit(df, date_start, date_end):
    df['date_end'] = pd.to_datetime(df['date_end'])
    mask = (df['date_end'] >= date_start) & (df['date_end'] <= date_end)
    df = df.loc[mask]
    won = df.loc[df['status'] == 'won']                                     #estados won en 2022
    won['Month'] = won['date_end'].dt.month                               #agrega una columna mes
    won['Year'] = won['date_end'].dt.year                                 #agrega una colmna año
    
    plt.figure(figsize=(25, 16))
    plt.style.use('fivethirtyeight') 
    plt.title('TTV' + ' del ' + str(date_start) + ' a ' + str(date_end))
    plt.tick_params(axis='x', labelsize=7)	
    plt.ylabel('Value [M]')

    ax = won.groupby(['Year', 'Month'])['value'].sum().plot(kind='bar', color='#7AC8AE')
    plt.xlabel('Año, Mes')
    plt.xticks(rotation=40)

    for p in ax.patches:
        ax.annotate(format(p.get_height(), '.0f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')

    plt.savefig('gv/graficos/profit.png')
    plt.show()
    plt.close()

df = pd.read_csv('./gv/data/bi_deal(2021a).csv')

## La fecha límite de inicio es 2019-01-01

date_start = '2022-01-01'
date_end = '2023-01-31'

profit(df, date_start, date_end)