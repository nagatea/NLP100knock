#%% [markdown]
# ## 37. 頻度上位10語
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
# ### 方針
# * 36を流用
# * `plt.bar()`で棒グラフ作成

#%%
import common04
word_list = [word['base'] for word in common04.get_neko_mecab()]
res = {}
for word in word_list:
  if word in res:
    res[word] += 1
  else:
    res[word] = 1

famous_words = sorted(res.items(), key=lambda x:x[1], reverse=True)[0:10]

#%%
import matplotlib.pyplot as plt
font = {'family':'AppleGothic'}
plt.rc('font', **font)

word_list = []
count_list = []
for (word, count) in famous_words:
  word_list.append(word)
  count_list.append(count)

plt.bar(word_list, count_list)
