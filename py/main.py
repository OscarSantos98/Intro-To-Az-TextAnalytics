import requests
import json
import os
import pandas as pd

API_endpoint = os.environ.get('AZ_TXT_ANALYTICS_ENDPOINT')
url = os.path.join(API_endpoint,'text/analytics/v3.1/sentiment')
key = os.environ.get('AZ_TXT_ANALYTICS_KEY')

# POST
print("POST request")

data = {
  "documents": [
    {
      "language": "en",
      "id": "1",
      "text": "Hello world. This is some input text that I love."
    },
    {
      "language": "fr",
      "id": "2",
      "text": "Bonjour tout le monde"
    },
    {
      "language": "es",
      "id": "3",
      "text": "La carretera estaba atascada. Había mucho tráfico el día de ayer."
    },
    {
      "language": "it",
      "id": "4",
      "text": "Ciao, mi è piaciuto molto mangiare in questo ristorante."
    },
    {
      "language": "en",
      "id": "5",
      "text": "I want to eat"
    },
    {
      "language": "it",
      "id": "6",
      "text": "Non sono d'accordo con i prezzi"
    },
    {
      "language": "es",
      "id": "7",
      "text": "Ese parque es mi lugar favorito."
    },
    {
      "language": "en",
      "id": "8",
      "text": "that hospital has a terrible service."
    },
    {
      "language": "en",
      "id": "9",
      "text": "The book was so bad."
    },
    {
      "language": "fr",
      "id": "10",
      "text": "le service était horrible"
    }
  ]
}

stringOfJsonData = json.dumps(data)
print(stringOfJsonData)

# Request
response = requests.post(url = url, headers={"content-type":"application/json", "Ocp-Apim-Subscription-Key": key}, json = data)
print("statusCode: ", response.status_code)

# Handler
if response.status_code == 200:
	print(response.text)
elif response.status_code == 401:
  print("API_key incorrecta")
elif response.status_code == 404:
  print("API_endpoint incorrecto")
else:
	print(response.reason)

response_dict = json.loads(response.text)
if "error" in response_dict:
  quit()

print()

# List documents
for doc in response_dict["documents"]:

    for field in doc:
        print(field, end=': ')
        print(doc[f"{field}"])

    print()

# Create filter function
def filter(response_dict, sentiment):

    flag = 0
    sentiments = dict()
    result = []
    for doc in response_dict["documents"]:

        for dict_key in doc:

            if dict_key == "id":
                current_id = doc[dict_key]
                continue

            if doc[dict_key] == sentiment:

                sentiments["id"] = int(current_id)
                sentiments[f"{dict_key}"] = data['documents'][int(current_id)-1]['text']
                flag = 1

        if flag:
            #print(sentiments)
            s = dict(sentiments)
            result.append(s)

        flag = 0

    return result

# Use filter function for each sentiment
positive = filter(response_dict, 'positive')
neutral = filter(response_dict, 'neutral')
negative = filter(response_dict, 'negative')
print(positive)
print()
print(neutral)
print()
print(neutral)

# Create pandas DataFrames
pos_df = pd.DataFrame(positive)
neu_df = pd.DataFrame(neutral)
neg_df = pd.DataFrame(negative)
print(pos_df)
print(neu_df)
print(neg_df)

# Create data folder if not exists
if not os.path.exists(os.path.join(os.getcwd(),'data')):
  
  os.makedirs(os.path.join(os.getcwd(),'data'))
  print("Folder creado exitósamente")

# Create csv files and put them into data folder
pos_df.to_csv("data/positives.csv")
neu_df.to_csv("data/neutrals.csv")
neg_df.to_csv("data/negatives.csv")