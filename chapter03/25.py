#%% [markdown]
# ## 25. テンプレートの抽出
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．

#%%
import re
import common03
data = common03.get_uk_data()['text']

#%%
regex = r'\{\{基礎情報.+\}\}'
pattern = re.compile(regex, re.M + re.S)
match = pattern.search(data)
base_data = match[0]
regex = r'\|(.+) = (.+)'
pattern = re.compile(regex)
res = {}
for match in pattern.finditer(base_data):
  res[match.group(1)] = match.group(2)
res
