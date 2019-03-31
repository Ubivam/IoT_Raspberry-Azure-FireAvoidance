import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")  # Load data

# Scatterplot with matplotlib
for is_smoker in tips.smoker.unique():
    is_smoker_data = tips.query('smoker == @is_smoker')
    plt.scatter(is_smoker_data['total_bill'], is_smoker_data['tip'], edgecolors='w', label=f'{is_smoker}')
plt.legend(title='Smoker')

# Scatterplot with Seaborn
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, scatter_kws={'edgecolors': 'w'}, fit_reg=False)
plt.show()