import numpy as np
import pandas as pd
import sklearn
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import cm as cm
from io import BytesIO
import base64


### Configure Float for pandas dataframes:
pd.options.display.float_format = '${:,.2f}'.format


### Download Dataset as dataframe:
dataset = pd.read_csv('winequality-red.csv')
#, delimiter = ';' 

### Top Rows:
head = dataset.head()


### Columns types:
data_info = dataset.info()


### Describe:
describe = dataset.describe()
describe = describe.iloc[1:,:]  ## ommit count


### Unique quality(our label) values:
values = dataset['quality'].unique()


### Quick stats plots:
plots = sns.pairplot(dataset)


### Counting records for each quality class
from collections import Counter
counter = Counter(dataset['quality'])
counter_df = pd.DataFrame.from_dict(counter, orient='index').reset_index()
counter_df = counter_df.rename(columns={'index': 'Quality', 0: 'Records'})
counter_sort = counter_df.sort_values(by=['Quality'])


### Plot Quality count:
quality_plot = sns.countplot(x='quality', data=dataset)


### Correlations
correlations = dataset.corr()


### Plotting correlation matrix
names = ['f_acid', 'v_acid', 'c_acid', 'r_sug', 'chlor', 'f_s_dx', 't_s_dx', 'density', 'pH', 'sulph', 'alcohol', 'quality']
fig = plt.figure()
ax = fig.add_subplot(111)
cmap = cm.get_cmap("coolwarm", 30)
cax = ax.matshow(correlations, vmin=-1, vmax=1, cmap=cmap)
fig.colorbar(cax)
ticks = np.arange(0,12,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names, fontsize=8)
ax.set_yticklabels(names, fontsize=8)
plt.show()


### OTHER PLOTS:

area = np.pi*3  


### 'sulphates vs quality'
q_sulphates = BytesIO()
plt.scatter(dataset.get("quality"), dataset.get("sulphates"), s=area, alpha=0.5, color='darkgreen')
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
plt.title('Quality vs Sulphates')
plt.xlabel('Quality')
plt.ylabel('Sulphates')
plt.savefig(q_sulphates, format='png')
q_sulphates.seek(0)
plot_q_sulphates = base64.b64encode(q_sulphates.getvalue())


### 'alcohol vs quality'
q_alcohol = BytesIO()
plt.scatter(dataset.get("quality"), dataset.get("alcohol"), s=area, alpha=0.5, color ='darkred')
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
plt.title('Quality vs Alcohol')
plt.xlabel('Quality')
plt.ylabel('Alcohol')
plt.savefig(q_alcohol, format='png')
q_alcohol.seek(0)
plot_q_alcohol = base64.b64encode(q_alcohol.getvalue())


### 'c_acid vs quality'
q_c_acid = BytesIO()
plt.scatter(dataset.get("quality"), dataset.get("citric acid"), s=area, alpha=0.5, color ='magenta')
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
plt.title('Quality vs Citric Acid')
plt.xlabel('Quality')
plt.ylabel('Citric Acid')
plt.savefig(q_c_acid, format='png')
q_c_acid.seek(0)
plot_q_c_acid = base64.b64encode(q_c_acid.getvalue())


### 'fixed acidity vs quality'
q_f_acid = BytesIO()
plt.scatter(dataset.get("quality"), dataset.get("volatile acidity"), s=area, alpha=0.5, color ='darkblue')
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
plt.title('Quality vs Volatile Acidity')
plt.xlabel('Quality')
plt.ylabel('Volatile Acidity')
plt.savefig(q_f_acid, format='png')
q_f_acid.seek(0)
plot_q_f_acid = base64.b64encode(q_f_acid.getvalue())
















