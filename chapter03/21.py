#%% [markdown]
# ## 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．
# ### 方針
# * `.+Category:.+`

#%%
import re
import common03
data = common03.get_uk_data()['text']

regex = r'.+Category:.+'
pattern = re.compile(regex)
match = pattern.findall(data)
print('\n'.join(match))
