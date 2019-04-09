import json

def get_uk_data():
  data = {}
  with open('jawiki-country.json') as f:
    for line in f:
      data = json.loads(line)
      if data['title'] == 'イギリス':
        break
  return data