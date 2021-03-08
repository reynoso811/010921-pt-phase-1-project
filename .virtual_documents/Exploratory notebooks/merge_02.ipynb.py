import pandas as pd


df_01 = pd.read_csv('../data/zippedData/tn.movie_budgets.csv.gz')
df_02 = pd.read_csv('../data/zippedData/imdb.title.basics.csv.gz')


df_01.head()


df_01.shape


df_02.head()


df_02.shape


df_01.keys()


plot_02 = df_01.drop(['id', 'movie','production_budget', 'worldwide_gross'], axis = 1)


plot_02.head()


plot_02.to_csv('../data/zippedData/Processed/plot_02.csv')



