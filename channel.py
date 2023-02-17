import pandas as pd
import matplotlib.pyplot as plt

def channel(df, date_start, date_end):
    
    df['date_end'] = pd.to_datetime(df['date_end'])
    mask = (df['date_end'] >= date_start) & (df['date_end'] <= date_end)
    df = df.loc[mask]
    result = pd.DataFrame(df["channel"].value_counts())
    print(result)
    result.plot(kind='pie', subplots=True, figsize=(25, 15))
    plt.title('Lead por canal' + ' del ' + str(date_start) + ' a ' + str(date_end))
    plt.savefig('./gv/graficos/channel_lead.png')
    plt.show()
    result.to_csv('gv/tables/channel.csv')


df = pd.read_csv('./gv/data/bi_deal(2021a).csv')
date_start = '2022-01-01'
date_end = '2023-01-31'

channel(df, date_start, date_end)