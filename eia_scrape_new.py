import pandas as pd 

url = "https://www.eia.gov/electricity/annual/html/epa_11_01.html"

eia_table = pd.read_html(url)

#print(eia_table)
print(eia_table[1])
#print(eia_table[0])

eia_table[1].to_csv('/new/eia_new.csv', index=False)

