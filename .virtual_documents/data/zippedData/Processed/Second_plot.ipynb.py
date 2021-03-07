import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")



df_01 = pd.read_csv('plot_02.csv')


df_01.head()


df_01.keys()


df_01.drop(['Unnamed: 0'], axis =1)


sorted_datetime = df_01['release_date'] = pd.to_datetime(df_01.release_date)


data = df_01.sort_values(by='release_date', ascending = True)


data


def clean_currency(x):
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)

data['domestic_gross'] = data['domestic_gross'].apply(clean_currency).astype('float')



data_01 = data[data.domestic_gross > 0]


data_01.head()


data_02 = data_01.sort_values(by='release_date', ascending = True)


data_02.head()


data_02['release_date'].dt.month
data_02['months'] = data_02['release_date'].dt.month
data_02.head()





data_02.plot(kind="scatter", x = 'months' , y = 'domestic_gross')
plt.xlabel("Month of mov release")
plt.ylabel("US Gross (mil)")
plt.title("Monetarily Successful Release Dates")
#plt.text(word, fontsize=9)
#plt.annotate()
#error bar?


#y = pd.to_datetime(data_02["release_date"], format='get_ipython().run_line_magic("m').apply(lambda", " x: x.strftime('%m'))")


#data_03 = data_02['release_date'].apply(lambda x: x.strftime('get_ipython().run_line_magic("m'))", "")






