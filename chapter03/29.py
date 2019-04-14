#%% [markdown]
# ## 29. 国旗画像のURLを取得する
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
# ### 方針
# * 国旗のファイル名は国旗画像に格納されている
# * [ここ](https://www.mediawiki.org/wiki/API:Imageinfo)に書いてある例にそって取得する

#%%
import re
import common03
data = common03.get_uk_data()['text']

regex = r'\|国旗画像 = (.+)'
pattern = re.compile(regex)
file_name = pattern.search(data).group(1)
# file_name = file_name.replace(" ", "_")
file_name

#%%
import requests
S = requests.Session()
URL = "https://ja.wikipedia.org/w/api.php"
PARAMS = {
    "action":"query",
    "format":"json",
    "prop": "imageinfo",
    "titles": f"File:{file_name}",
    "iiprop" : "url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

DATA['query']['pages']['-1']['imageinfo'][0]['url']
