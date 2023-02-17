import pandas as pd
import matplotlib.pyplot as plt

def conversion(df, date_start, date_end):

    df['date_end'] = pd.to_datetime(df['date_end'])
    mask = (df['date_end'] >= date_start) & (df['date_end'] <= date_end)
    df = df.loc[mask]
    df = df.loc[df['is_upselling'] == 0]                                    # Los que no son upselling
    df = df.drop(df[df['destination']== '(not set)'].index)                 #elimina destination -> (not set)
    df = df.drop(df[df['agent'] == 'admingv'].index)                         #elimina el agent -> admingv
    df = df.drop(df[df['agent'] == 'arvin@grandvoyage.com'].index)           #elimina el agent -> arvin
    df = df.drop(df[df['agent'] == 'tech@grandvoyage.com'].index)            #elimina el agent -> tech
    df = df.drop(df[df['agent'] == 'sara@grandvoyage.com'].index)                         #elimina el agent -> admingv
    df = df.drop(df[df['agent'] == 'dircom@grandvoyage.com'].index)                         #elimina el agent -> admingv
    df = df.drop(df[df['agent'] == 'jea@grandvoyage.com'].index)                   #elimina el agent -> admingv
    df = df.drop(df[df['agent'] == 'alessandra@grandvoyage.com'].index)                   #elimina el agent -> admingv
    df = df.drop(df[df['agent'] == 'False'].index)                         #elimina el agent -> admingv

    destination_list = df['destination'].unique().tolist()                  #todos los elementos de 'destination'
    destination_list.sort()                                                 #ordenados alfabeticamente
    df['agent'] = df['agent'].str.replace('@grandvoyage.com', '', regex=True)           #Elimina @grandvoyage de la columna agente
    df['agent'] = df['agent'].str.capitalize()                              #Pone en mayúscula la primera letra
    agent_list = df['agent'].unique().tolist()                              #todos los elementos de 'agent'
    agent_list.sort()                                                       #ordenados alfabeticamente
    won = df.loc[df['status'] == 'won']                                     #estados won en 2022
    lost = df.loc[df['status'] == 'lost']                                   #estados lost en 2022

    min_lead = 10

    result = pd.DataFrame(columns=agent_list)                                 #crea la tabla de resultado

    for k in destination_list:                                              #por cada destino
        destination_won = won[won['destination'] == k]                      # destino won
        destination_lost = lost[lost['destination'] == k]                   #destino lost
        for j in agent_list:                                                #por cada agente 
            won_agent = destination_won[destination_won['agent'] == j]      #agente won
            lost_agent = destination_lost[destination_lost['agent'] == j]   #agente lost
            total_agent = won_agent.shape[0] + lost_agent.shape[0]          #numero total de leads
            if total_agent > min_lead:
                porcentaje = (won_agent.shape[0]/total_agent)*100           #calcula el porcentaje
            else:
                porcentaje = 0
            result.loc[k, j] = round(porcentaje,1)                          #agrega el porcentaje a la tabla
            
    result.to_csv('./gv/tables/agent_conversion_destination.csv')


    promedio = round(result.mean(axis=1),1)

    for i in agent_list:
        plt.figure(figsize=(25, 16))
        plt.title(f'Conversión de Lead por destino de {i}' + ' del ' + str(date_start) + ' a ' + str(date_end), fontsize=20)
        plt.xlabel('Destino', fontsize=15)
        plt.ylabel('Conversion (%)', fontsize=15)
        plt.xticks(rotation=90)
        plt.bar(destination_list, result[i], color='#FFA62B', label=f'{i}')
        plt.stem(destination_list, promedio, label='Promedio')
        plt.ylim(0,50)
        plt.legend(loc='upper right')
        for x, y in zip(destination_list, promedio):
            label = "{:.1f}".format(y)
            plt.annotate(label, # this is the text
                        (x,y), # this is the point to label
                        textcoords="offset points", # how to position the text
                        xytext=(0,10), # distance from text to points (x,y)
                        ha='center') # horizontal alignment can be left, right or center
        archivo = f'conversion_{i}.png'
        plt.savefig('gv/graficos/'+ archivo)
        plt.close()
    
    
    

df = pd.read_csv('./gv/data/bi_deal(2021a).csv')
date_start = '2022-01-01'
date_end = '2023-01-31'

conversion(df, date_start, date_end)