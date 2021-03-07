import pandas as pd


df_01 = pd.read_csv('../data/zippedData/bom.movie_gross.csv.gz')


df_04 = pd.read_csv('../data/zippedData/imdb.title.basics.csv.gz')


df_07 = pd.read_csv('../data/zippedData/imdb.title.ratings.csv.gz')


df_11 = pd.read_csv('../data/zippedData/tn.movie_budgets.csv.gz')


df_09 = pd.read_csv('../data/zippedData/rotten_tomatoes_movies.csv.gz')


df_01.head()


df_01.shape


df_04.head()


df_04.shape


df_07.head()


df_07.shape


merge_01 = pd.merge(df_07,df_04)


merge_01.head()


merge_01.shape


merge_01.to_csv('../data/zippedData/Processed/merge1.csv')


df_01 = pd.read_csv('../data/zippedData/bom.movie_gross.csv.gz')


df_01.head()


data_g = df_01.drop(['title','foreign_gross', 'year'], axis=1)


data_g.head()


data_g.to_csv('../data/zippedData/Processed/third_graph.csv')



