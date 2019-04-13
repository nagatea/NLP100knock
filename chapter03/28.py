#%% [markdown]
# ## 28. MediaWikiマークアップの除去
# 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
# ### 方針
# * `[外部リンク]`の除去
# * `{{lang|**|内容}}`の除去
# * `<br />`の除去
# * `<ref> <ref /> </ref>`の除去

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
  field_data = re.sub(r"\[(.*?)\]", r' \1', field_data)
  field_data = re.sub(r"\{\{lang\|..\|(.*?)\}\}", r'\1', field_data)
  field_data = re.sub(r"<br ?/>", '', field_data)
  field_data = re.sub(r"</?ref.*?>", '', field_data)
  res[match.group(1)] = field_data
res
