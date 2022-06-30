import json
import requests
import pandas as pd
from string import ascii_uppercase

urls = []
for c in ascii_uppercase:
  urls.append("http://www4.vestibular.ufjf.br/{0}/notaspism2_aposrevisao/{1}.html".format(2022,c))


df2 = pd.DataFrame(columns=['Nome', 'Inscricao', 'Pontos_PISM1', 'Pontos_PISM2', 'Pontos_Totais'])
for url in urls:
    html = requests.get(url).text   

    data = html.split('var testdata = ')[1].split('</script>')[0].replace(';', '')
    d = json.loads(data)

    records = []
    for student in d['data']:
        row = [student['nome'],
               student['inscricao'], 
               student['modulosPISM'][0]['notaTotal'],
               student['modulosPISM'][1]['notaTotal'],
               student['totalPontos']]
        records.append(row)

        df = pd.DataFrame(records, columns=['Nome', 'Inscricao', 'Pontos_PISM1', 'Pontos_PISM2', 'Pontos_Totais'])

    df2 = pd.concat([df, df2])

df2 = df2.sort_values(by='Pontos_Totais', ascending=False)

print(df2)

df2.to_csv("notas_PISM.csv", index=False)
