#%% [markdown]
# ## 26. 強調マークアップの除去
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
# ### 方針
# * `'''強調'''`、`'''''斜体と強調'''''`
# * `re.sub(pattern, repl, string)`

#%%
import re
import common03
data = common03.get_uk_data()['text']
pattern = re.compile(r'\{\{基礎情報.+\}\}', re.M + re.S)
match = pattern.search(data)
base_data = match[0]
pattern = re.compile(r'\|(.+) = (.+)')
res = {}
for match in pattern.finditer(base_data):
  field_data = match.group(2)
  field_data = re.sub(r"'''(.+)'''", r'\1', field_data)
  res[match.group(1)] = field_data
res
