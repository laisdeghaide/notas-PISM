import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
from string import ascii_uppercase

df = pd.read_csv('notas_PISM.csv')
print(df.loc[df['Nome'] == "VITOR LACERDA HERINGER"])
