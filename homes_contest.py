# https://skills.yourlearning.ibm.com/activity/MDL-456?planId=PLAN-D8E7C82C1D76&sectionId=SECTION-B&planIdFromParentTab=PLAN-D8E7C82C1D76&sectionIdFromParentTab=SECTION-A&planIdForChildTab=PLAN-D8E7C82C1D76
#https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
# https://www.youtube.com/watch?v=QBRY5Nm-Q60
# https://www.youtube.com/watch?v=8xUher8-5_Q

import pandas as pd 
df = pd.read_csv("train.csv").dropna()

print(df.head())
print(df.describe())

#GOAL FOR TODAY: finish the IBM course and then start researching for the Kaggle competition and then get an output (train 1 model)
#also make notes on the methods of model evaluation 