#%% [markdown]
# ## 34. 「AのB」
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．
# ### 方針
# * 配列の$i$,$i+1$,$i+2$で「名詞、の、名詞」となってるのを配列に追加していく

#%%
import common04
word_list = common04.get_neko_mecab()

res = []
for i in range(len(word_list)-2):
  word1 = word_list[i]
  word2 = word_list[i+1]
  word3 = word_list[i+2]
  if word1['pos'] == '名詞' and word2['surface'] == 'の' and word3['pos'] == '名詞':
    res.append(word1['surface'] + word2['surface'] + word3['surface'])

res[0:50]
