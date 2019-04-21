#%% [markdown]
# ## 39. Zipfの法則
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
# ### 方針
# * 36を流用(順位はインデックスの番号)
# * 対数グラフは`plt.xscale('log')`, `plt.yscale('log')`

#%%
import common04
word_list = [word['base'] for word in common04.get_neko_mecab()]
res = {}
for word in word_list:
  if word in res:
    res[word] += 1
  else:
    res[word] = 1

words = sorted(res.items(), key=lambda x:x[1], reverse=True)
index_list = [i+1 for i in range(len(words))]
count_list = [count for (word, count) in words]

#%%
import numpy as np
import matplotlib.pyplot as plt

plt.xscale('log')
plt.yscale('log')
plt.xlabel('index')
plt.ylabel('count')

plt.plot(np.array(index_list), np.array(count_list))
