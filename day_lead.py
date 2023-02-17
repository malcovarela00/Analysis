import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

def DayLead(df, date_start, date_end):
    df['date_end'] = pd.to_datetime(df['date_end'])
    mask = (df['date_end'] >= date_start) & (df['date_end'] <= date_end)
    df = df.loc[mask]
    
    df['dia'] = df['date_end'].dt.dayofweek
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    
    y = df.groupby('dia').count()['gv_id']
    print(y)
    plt.figure(figsize=(25, 16))
    plt.bar(dias, y)
    plt.title('Cantidad de leads por día de la semana del ' + date_start + ' a ' + date_end)
    plt.xlabel('Día de la semana')
    plt.ylabel('Cantidad de leads')
    plt.savefig('gv/graficos/day_lead.png')
    plt.show()
