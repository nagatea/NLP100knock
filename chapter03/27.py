#%% [markdown]
# ## 27. 内部リンクの除去
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ（参考: マークアップ早見表）．
# ### 方針
# * `[[内部リンク]]`
# * `re.sub()`
# * 最短一致にしないといけないっぽい

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
  field_data = re.sub(r"\[\[.+\|(.*?)\]\]", r'\1', field_data)
  field_data = re.sub(r"\[\[(.*?)\]\]", r'\1', field_data)
  res[match.group(1)] = field_data
res
