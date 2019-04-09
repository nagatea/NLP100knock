#%% [markdown]
# ## 24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ．
# ### 方針
# * `ファイル.+\.[jpg|JPG].+`

#%%
import re
import common03
data = common03.get_uk_data()['text']

regex = r'ファイル:(.+\.(jpg|JPG))'
pattern = re.compile(regex)
for match in pattern.finditer(data):
  print(match.group(1))


#%%
