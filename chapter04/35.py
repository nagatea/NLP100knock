#%% [markdown]
# ## 35. 名詞の連接
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
# ### 方針
# * 名詞が来たら保持しつづけ、名詞が来なかったら配列につっこむ

#%%
import common04
word_list = common04.get_neko_mecab()

tmp = []
res = []
for word in word_list:
  if word['pos'] == '名詞':
    tmp.append(word['surface'])
  else:
    if not tmp:
      continue
    elif len(tmp) == 1:
      tmp = []
    else:
      res.append(tmp)
      tmp = []

res[0:50]
