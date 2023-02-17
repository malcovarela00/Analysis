import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def TopDestination(df, date_start, date_end):
    df['date_end'] = pd.to_datetime(df['date_end'])
    mask = (df['date_end'] >= date_start) & (df['date_end'] <= date_end)
    df = df.loc[mask]
    
    won = df.loc[df['status'] == 'won']
    won['Month'] = won['date_end'].dt.month
    won['Year'] = won['date_end'].dt.year
    
    max_destination = 9

    destination_list = won.groupby(['destination'])['value'].sum()
    destination_list = destination_list.sort_values(ascending=False)
    destination_list = destination_list.head(max_destination)

    print(destination_list)
    
    plt.figure(figsize=(25, 16))
    plt.bar(destination_list.index, destination_list.values)
    plt.tick_params(axis='x', labelsize=10)	
    plt.title('Top ' + str(max_destination) + ' Destinos' + ' del ' + str(date_start) + ' a ' + str(date_end))
    plt.xlabel('Destinos')
    plt.ylabel('Value [M]')
    plt.savefig('./graficos/top_destination.png')
    plt.show()
    plt.close()
    
    
    top_destinations = destination_list[:max_destination].index
    y = won[won['destination'].isin(top_destinations)].groupby(['destination', 'Month'])['value'].sum().reset_index()
    plt.figure(figsize=(25,16))
    for i in range(0, len(top_destinations)):
        plt.subplot(3, 3, i+1)
        df_destination = y[y['destination']==top_destinations[i]]
        plt.bar(df_destination['Month'], df_destination['value'], align='center', color='#F9A364')
        plt.xticks(np.arange(1,13))
        plt.title('Destino ' + str(top_destinations[i]) + ' del ' + str(date_start) + ' a ' + str(date_end))
        plt.xlabel('Mes')
        plt.ylabel('Value')
    plt.tight_layout()
    plt.savefig('./graficos/top_destination_year.png')
    plt.show()
