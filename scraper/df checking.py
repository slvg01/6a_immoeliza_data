import pandas as pd


dfhouse = pd.read_csv('data/raw_data/data_set_RAW_HOUSES.csv')
dfapartment = pd.read_csv('data/raw_data/data_set_RAW_APARTMENTS.csv')
dfhouse.drop_duplicates(inplace=True)
print(dfhouse.shape)

dfapartment.drop_duplicates(inplace=True)
print(dfapartment.shape)

dfall = pd.DataFrame()
dfall = pd.concat(dfhouse)
dfall = pd.concat(dfapartment)
dfall.to_excel('data_set_RAW_ALL')