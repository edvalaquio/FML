import pandas as pd
import numpy as np

dataset = pd.read_csv("classifier_data_0.csv")
dataset.head(10)

sample = dataset['owner'].value_counts().to_frame().reset_index()
# # sample
sample = sample[sample['owner'] > 300][sample['owner'] < 900].reset_index().drop(['level_0', 'owner'], axis=1).rename(columns={'index':'owner'})

sample = sample['owner'].values.tolist()

dataset = dataset[dataset['owner'].isin(sample)].reset_index().drop(['index'], axis=1)
dataset.to_csv('triage.csv', sep=',', encoding='utf-8')