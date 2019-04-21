#%% [markdown]
# ## 36. 単語の出現頻度
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
# ### 方針
# * ~~単語を全部`set`につっこんで、`set`の要素ごとに`count()`を走らせる~~
#   * めちゃ遅そう
#   * 遅かった
# * wordが存在したらcountを+1、なかったら新しく追加

#%%
import common04
word_list = [word['base'] for word in common04.get_neko_mecab()]
res = {}
for word in word_list:
  if word in res:
    res[word] += 1
  else:
    res[word] = 1

sorted(res.items(), key=lambda x:x[1], reverse=True)[0:50]
