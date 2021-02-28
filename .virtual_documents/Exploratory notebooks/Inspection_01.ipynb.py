import pandas as pd


df_01 = pd.read_csv('../data/zippedData/bom.movie_gross.csv.gz')


df_01


df_02 = pd.read_csv('../data/zippedData/imdb.name.basics.csv.gz')


df_02.head()
#Not helpful


df_03 = pd.read_csv('../data/zippedData/imdb.title.akas.csv.gz')


df_03.head()
#title_id to title


df_04 = pd.read_csv('../data/zippedData/imdb.title.basics.csv.gz')


df_04.head()
#tconst with a title


df_04.info


df_05 = pd.read_csv('../data/zippedData/imdb.title.crew.csv.gz')


df_05.head()
#Not useful


df_05.info


df_06 = pd.read_csv('../data/zippedData/imdb.title.principals.csv.gz')


df_06
#not really helpfull


#526 is also in 06 from 07
df_06[(df_06.tconst=="tt10356526")]


df_06.info


df_07 = pd.read_csv('../data/zippedData/imdb.title.ratings.csv.gz')


df_07.head()
#useful, match tcost key with movie title too?
#averagerating as a score


df_07.shape


df_07.keys()


df_07["tconst"]


#tconstRatings = df_07['tconst']
df_06.loc[df_06['tconst'].isin(tconstRatings)]




df_08 = pd.read_csv('../data/zippedData/rotten_tomatoes_critic_reviews.csv.gz')


df_08.head()
#useful, review_score


df_08.shape


df_09 = pd.read_csv('../data/zippedData/rotten_tomatoes_movies.csv.gz')


df_09.head()
#very useful


df_09.shape


df_10 = pd.read_csv('../data/zippedData/tmdb.movies.csv.gz')


df_10.head()
#different score / rating


df_10.shape


df_11 = pd.read_csv('../data/zippedData/tn.movie_budgets.csv.gz')


df_11.head()


df_11.shape



