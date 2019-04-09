#%% [markdown]
# ## 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
# ### 方針
# * `Category:(.+)\]\]`

#%%
import re
import common03
data = common03.get_uk_data()['text']

regex = r'Category:(.+)\]\]'
pattern = re.compile(regex)
for match in pattern.finditer(data):
  print(match.group(1))
