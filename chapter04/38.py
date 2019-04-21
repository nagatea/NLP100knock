#%% [markdown]
# ## 38. ヒストグラム
# 単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
### 方針
# * 36を流用
# * `plt.hist()`でヒストグラム作成

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
count_list = [word[1] for word in words]
count_list

#%%
import numpy as np
import matplotlib.pyplot as plt

plt.hist(np.array(count_list))

#%% [markdown]
# 10以下が多すぎて図の意味をなしていないので、10以下でもう一回計算

#%%
count_list = [count for count in count_list if count <= 10]
plt.hist(np.array(count_list))
