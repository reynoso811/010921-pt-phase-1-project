# Assign unique variables and read in files

df_04 = pd.read_csv('../imdb.title.basics.csv.gz')
df_07 = pd.read_csv('../imdb.title.ratings.csv.gz')


df_04.shape


df_07.shape


#Visualize the data

df_04.head()


#Visualize the data

df_07.head()


merge_01 = pd.merge(df_07,df_04)


merge_01.shape


# Merged visualization

merge_01.head()


# After succesfully merging I export this new merge to a .csv file in my Processed folder

# merge_01.to_csv('../data/zippedData/Processed/merge1.csv')


# I will be using the Pandas lybrary for my data manipulation and analysis

import pandas as pd

# I will be importing the Matplotlib library for my ploting purposes

import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")


ds_01 =  pd.read_csv('merge1.csv')


ds_01.head()


# Drop unnecessary columns


dropped = ds_01.drop(['Unnamed: 0','tconst','averagerating','numvotes','primary_title','runtime_minutes'], axis=1)


# Using the Pandas sort function I sort by the start year column

dropped.sort_values(by='start_year', ascending=False)


# A unique list of years. To match Genre year count to. 

plt_x = []
plt_x.extend(dropped['start_year'].tolist())
years = []
[years.append(x)for x in plt_x if x not in years]


years


# With this for loop I was able to accomplish several things. 
# In order to be able to plot which movie genre has the highest count. A new list of said counts is needed.
# Due to some movies having multiple genres. A filter was needed to only count movies with single genres.
# This new count was then transformed into a Pandas Data Frame
    

df = pd.DataFrame()
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
    output = {"genres":[],"count":[]}
    for elem in finalGenres:
        output["genres"].append(elem)
        output["count"].append(finalGenres[elem])
    frame = pd.DataFrame(output)
    frame["year"]=year
    df  = df.append(frame) 

df.head()    


# Create plot

plot_1 = df.pivot(columns="genres", index="year", values="count").T.sort_values(by=[2019],ascending=False).T.plot(kind="bar", stacked=True, figsize = (10,8))

plt.legend(ncol=5)
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.5),
         fancybox=True, shadow=True, ncol=5)

plt.xlabel("Movie Release Year")
plt.ylabel("Genre Count")
plt.title("Most Popular Genre")

plt.savefig('analysis_1.png')


df_01 = pd.read_csv('../tn.movie_budgets.csv.gz')


# Visualize the data

df_01.head()


# Show number of rows, columns

df_01.shape


plot_02 = df_01.drop(['id', 'movie','production_budget', 'worldwide_gross'], axis = 1)


df_01 = pd.read_csv('plot_02.csv')


df_01.head()


#Convert to Pandas datetime

sorted_datetime = df_01['release_date'] = pd.to_datetime(df_01.release_date)


# Sorting by release date

data = df_01.sort_values(by='release_date', ascending = True)


# This function removes the dollar signs and commas

def clean_currency(x):
    if isinstance(x, str):
        return(x.replace('$', '').replace(',', ''))
    return(x)

# The above function is called onto the desired column

data['domestic_gross'] = data['domestic_gross'].apply(clean_currency).astype('float')



# Sorted by greater than zero

data_01 = data[data.domestic_gross > 0]


# Sort once again 

data_02 = data_01.sort_values(by='release_date', ascending = True)


# Pull the month from the release date column and create a new months column

data_02['release_date'].dt.month
data_02['months'] = data_02['release_date'].dt.month
data_02.head()


data_02.shape


# Create Plot

data_02.plot(kind="scatter", x = 'months' , y = 'domestic_gross', figsize=(10, 8))

plt.xlabel("Month of Movie Release")
plt.ylabel("U.S. Gross (mm)")
plt.title("Monetarily Successful Release Dates")

plt.savefig('analysis_2.png')


df_0_1 = pd.read_csv('../bom.movie_gross.csv.gz')


df_0_1.head()


df_001 = pd.read_csv('third_graph')


# Drop unnecessary columns

data_g = df_0_1.drop(['title','foreign_gross', 'year'], axis=1)


data_g.head()


# Sort by domestic gross

sorted1 = df_0_1.sort_values(by=['domestic_gross'], ascending=True)
sorted1.head()
sorted1.shape


# Remove Nan values

na = sorted1.dropna()


# Filter top 50

largest = na.nlargest(50,'domestic_gross')
largest.head()


# Create Plot

largest.plot(kind = 'bar', y = 'domestic_gross' , x = 'studio', figsize = (10,8) )

plt.style.use('seaborn')
plt.legend()
plt.title('Top 50 Studios')
plt.xlabel("Studios")
plt.ylabel("U.S. Gross (mm)")

plt.savefig('analysis_3.png')
