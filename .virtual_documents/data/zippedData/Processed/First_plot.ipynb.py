import pandas as pd


import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


from pandasgui import show
gui  = show (dropped)


ds_02 =  pd.read_csv('merge1-Copy1.csv')


ds_02.keys()


ds_01 =  pd.read_csv('merge1.csv')


ds_01.head()


dropped = ds_02.drop(['Unnamed: 0','tconst','averagerating','numvotes','primary_title','runtime_minutes'], axis=1)


dropped.sort_values(by='start_year', ascending=False)


dropped.keys()


dropped.tail()


plt_x = []
plt_x.extend(dropped['start_year'].tolist())
years = []
[years.append(x)for x in plt_x if x not in years]


years


plt_y = []
plt_y.extend(dropped['genres'].tolist())




#dropped.plot(plt_x,plt_y)
#x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
#genre_01 = [count in 2010, 2011, 2012...]
#genre_02 = [count in 2010, 2011, 2012...]


#working function
for year in years:
    genres = dropped.loc[dropped["start_year"].isin([year])]["genres"]
    dropped.groupby("genres")
    finalGenres = {}
    for genre in genres:
        if type(genre) == str:
            vals = genre.split(",")
            for val in vals:
                if(val in finalGenres):
                    finalGenres[val] = finalGenres[val]+1
                else:
                    finalGenres[val] = 1
    
    print(year,finalGenres)
    print(finalGenres.keys())
    print(finalGenres.items())
    [
        [
            col1Name,col2Name
        ],
        [
            val,val
        ]
        
    ]
    break
    


for year in years:
    
    print("***********",year,"****************")
    genres = dropped.loc[dropped["start_year"].isin([year])]["genres"]
    dropped.groupby("genres")
    finalGenres = {}
    for genre in genres:
        if type(genre) == str:
            vals = genre.split(",")
            for val in vals:
                if(val in finalGenres):
                    finalGenres[val] = finalGenres[val]+1
                else:
                    finalGenres[val] = 1
    output = {"genres":[],"count":[]}
    for elem in finalGenres:
        output["genres"].append(elem)
        output["count"].append(finalGenres[elem])
    df  = pd.DataFrame(output)
    print(df)


x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

Documentary = [2902, 2011, 2012...]
Drama = [count in 2010, 2011, 2012...]
Comedy = [count in 2010, 2011, 2012...]
Crime = [count in 2010, 2011, 2012...]
Thriller = [count in 2010, 2011, 2012...]
Romance = [count in 2010, 2011, 2012...]
Horror = [count in 2010, 2011, 2012...]
Mystery = [count in 2010, 2011, 2012...]
Action = [count in 2010, 2011, 2012...]
History = [count in 2010, 2011, 2012...]
Animation = [count in 2010, 2011, 2012...]
Fantasy = [count in 2010, 2011, 2012...]
Adventure = [count in 2010, 2011, 2012...]
Family = [count in 2010, 2011, 2012...]
Music = [count in 2010, 2011, 2012...]
Biography = [count in 2010, 2011, 2012...]
Musical = [count in 2010, 2011, 2012...]
Sci_Fi = [count in 2010, 2011, 2012...]
Sport = [count in 2010, 2011, 2012...]
News = [count in 2010, 2011, 2012...]
War  = [count in 2010, 2011, 2012...]
Western  = [count in 2010, 2011, 2012...]
Reality_TV= [count in 2010, 2011, 2012...]
Short = [count in 2010, 2011, 2012...]







