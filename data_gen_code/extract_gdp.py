import pandas as pd

data = pd.read_csv('gdp-per-capita-worldbank.csv')

val = 'GDP per capita, PPP (constant 2017 international $)'
idx = 'Entity'
year = 'Year'

data = data[[idx, year, val]]

data2 = pd.DataFrame(data={idx : [], val : []})
for i, row in data.iterrows():
	if int(row[year]) != 2020:
		continue
	#print(row[[idx,val]])
	data2 = data2.append(row[[idx, val]])
data2.to_csv('gdp.csv',index=False)
