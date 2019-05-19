from flask import Flask, request
import json

app = Flask(__name__)

# DB接続
# ローカルでしか接続することを考えていないのでデプロイする場合にはちゃんと書く必要がある
from pymongo import MongoClient, ASCENDING, DESCENDING
client = MongoClient('localhost', 27017)
db = client.nlp100.artist

@app.route('/')
def index():
  return "Welcome to My Web App!!"

@app.route('/search', methods=['GET'])
def get_search():
  # クエリパラメータで受け取る
  # ','で区切ることでOR検索ができる仕様にした
  names = request.args.get('name', default='', type=str).split(',')
  aliases_names = request.args.get('aliases_name', default='', type=str).split(',')
  tags = request.args.get('tag', default='', type=str).split(',')
  
  # mongodb用クエリ作成
  # 全部をORでくっつけている
  db_query = []
  if names[0] != '':
    for name in names:
      db_query.append({'name': name})
  if aliases_names[0] != '':
    for aliases_name in aliases_names:
      db_query.append({'aliases.name': aliases_name})
  if tags[0] != '':
    for tag in tags:
      db_query.append({'tags.value': tag})
  result = db.find({'$or': db_query})
  res = [x for x in result]

  # ObjectIdはそのままだとJSONにパースできないことに注意
  for dic in res:
    dic['_id'] = str(dic['_id'])
  
  return json.dumps(res)

if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=5000)