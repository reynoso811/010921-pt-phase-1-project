import pandas as pd
import numpy as np


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
    


df = pd.DataFrame()
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
    frame = pd.DataFrame(output)
    frame["year"]=year
    df  = df.append(frame) 
    


df.head()


df.pivot(columns="genres", index="year", values="count").T.sort_values(by=[2019],ascending=False).T.plot(kind="bar", stacked=True)
plt.legend(ncol=5)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5),
         fancybox=True, shadow=True, ncol=5)
plt.xlabel("Movie release year")
plt.ylabel("Genre count")
plt.title("Most popular genre")


x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

Documentary = [2902, 1853, 1943, 2027, 2154, 2106, 2095, 2018, 1512, 401]
Drama = [2902, 3096, 3175, 3497, 3529, 3629, 3523, 3483, 3054, 900]
Comedy = [1606, 1759, 1826, 1895, 1987, 1951, 2013, 1914, 1786, 553]
Crime = [424, 466, 473, 507, 524,  538, 591, 532, 431, 125]
Thriller = [672, 713, 798, 936, 976, 1019, 1025, 956, 861, 261]
Romance = [642, 637, 653, 774, 842, 799, 769, 690, 615, 168]
Horror = [646, 699, 827, 810, 899, 885, 953, 961, 790, 204]
Mystery = [239, 275, 290, 323, 365, 374, 396, 395, 310, 72]
Action = [691, 692, 691, 717, 773, 807, 858, 854, 701, 204]
History = [274, 277, 352, 377, 428, 352, 277, 246, 202, 40]
Animation = [150, 199, 167, 169, 191, 196, 196, 210, 204, 61]
Fantasy = [188, 216, 210, 470, 240, 257, 275, 244, 214, 61]
Adventure = [313, 371, 371, 464, 454, 462, 467, 435, 373, 107]
Family = [299, 314, 364, 470, 466, 415, 353, 349, 299, 83]
Music = [193, 230, 249, 224, 272, 238, 173, 197, 154, 38]
Biography = [341, 382, 396, 521, 603, 499, 401, 334, 249, 83]
Musical = [82, 81, 80, 82, 77, 70, 87, 75, 71, 16]
Sci_Fi = [196, 200, 208, 260, 253, 271, 252, 281, 220, 65]
Sport = [93, 124, 104, 142, 156, 141, 149, 124, 115, 31]
News = [62, 124, 86, 104, 127, 90, 22, 10, 5, 2]
War  = [90, 99, 82, 71, 108, 103, 95, 99, 81, 25]
Western  = [25, 30, 31, 27, 39, 28, 24, 37, 33, 6]
Reality_TV= [3, 0, 1, 3, 1, 4, 2, 1, 2, 0]



plt.bar(x,Documentary,0.4,label="Documentary")
plt.bar(x,Drama,0.4,label="Drama")
plt.bar(x,Comedy,0.4,label="Comedy")
plt.bar(x,Crime,0.4,label="Crimes")
plt.bar(x,Thriller,0.4,label="Thriller")
plt.bar(x,Romance,0.4,label="Romance")
plt.bar(x,Horror,0.4,label="Horror")
plt.bar(x,Mystery,0.4,label="Mystery")
plt.bar(x,Action,0.4,label="Action")
plt.bar(x,History,0.4,label="History")
plt.bar(x,Animation,0.4,label="Animation")
plt.bar(x,Fantasy,0.4,label="Fantasy")
plt.bar(x,Adventure,0.4,label="Adventure")
plt.bar(x,Family,0.4,label="Family")
plt.bar(x,Music,0.4,label="Music")
plt.bar(x,Biography,0.4,label="Biography")
plt.bar(x,Musical,0.4,label="Musical")
plt.bar(x,Sci_Fi,0.4,label="Sci_Fi")
plt.bar(x,Sport,0.4,label="Sport")
plt.bar(x,News,0.4,label="News")
plt.bar(x,War,0.4,label="War")
plt.bar(x,Western,0.4,label="Western")
plt.bar(x,Reality_TV, 0.4,label="Reality_TV")

plt.xlabel("Movie release year")
plt.ylabel("Genre count")
plt.title("Most popular genre")
plt.legend()

#plt.bar(make graph bigger, yerr=?)
#hide the legend.legend?


Drama = [count in 2010, 2011, 2012...]



