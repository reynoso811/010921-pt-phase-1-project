import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic("matplotlib", " inline")




df_01 = pd.read_csv('third_graph')


df_01.head()


sorted1 = df_01.sort_values(by=['domestic_gross'], ascending=True)
sorted1.head()
sorted1.shape


na = sorted1.dropna()
na.describe()


largest = na.nlargest(50,'domestic_gross')
largest.head()





largest.plot(kind = 'bar', y = 'domestic_gross' , x = 'studio', figsize = (10,8) )
plt.style.use('seaborn')
plt.legend()
plt.title('test')
plt.xlabel("Studios")
plt.ylabel("US Gross (mil)")



