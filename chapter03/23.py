#%% [markdown]
# ## 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
# ### 方針
# * `=`の数でセクションレベルを判断する

#%%
import re
import common03
data = common03.get_uk_data()['text']

regex = r'(=?=?==)([^=]*)===?=?'
pattern = re.compile(regex)
res = [(match.group(2), len(match.group(1)) -1) for match in pattern.finditer(data)]
res
