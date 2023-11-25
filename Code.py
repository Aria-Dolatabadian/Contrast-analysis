import pandas as pd
# Read CSV File into Python
df = pd.read_csv('sample_data.csv')
#Contrast Analysis
from scipy import stats
# Perform pairwise t-tests for all combinations of groups
groups = df['Group'].unique()
for i in range(len(groups)):
    for j in range(i + 1, len(groups)):
        group_i = df[df['Group'] == groups[i]]['Variable']
        group_j = df[df['Group'] == groups[j]]['Variable']
        t_stat, p_value = stats.ttest_ind(group_i, group_j)
        # Print results
        print(f'T-test between Group {groups[i]} and Group {groups[j]}:')
        print(f'T-statistic: {t_stat}')
        print(f'P-value: {p_value}')
        print('\n')
#Visualize the Results with Different Colors
import matplotlib.pyplot as plt
import seaborn as sns
# Boxplot for visualizing the contrast with different colors for each group
plt.figure(figsize=(10, 8))
sns.boxplot(x='Group', y='Variable', data=df, palette='Set3', hue='Group')
plt.title('Contrast Analysis')
plt.xlabel('Group')
plt.ylabel('Variable')
plt.show()
