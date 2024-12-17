import requests
import pandas as pd
import numpy as np

response = requests.get("https://coderbyte.com/api/challenges/logs/user-info-csv")
csv_as_text = response.content.decode('utf-8')
list_of_csv = csv_as_text.split('\n')
fin = []
for index, value in enumerate(list_of_csv) :
    fin.append(value.split(','))
fin = np.array(fin)
frame = pd.DataFrame(columns = [str(fin[0,0]).lower(), str(fin[0,1]).lower(), str(fin[0,2]).lower()])
for i in range(1,len(fin)):
    frame.loc[len(frame.index)] = [fin[i,0],fin[i,1],fin[i,2]]
frame = frame.sort_values(by='email')
json_data = pd.DataFrame.to_json(frame,orient="records")
print(json_data)