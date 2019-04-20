#%% [markdown]
# ## 31. 動詞
# 動詞の表層形をすべて抽出せよ．
# ### 方針
# * posが動詞になっているもののsurfaceをリスト化する
 
#%%
import common04
word_list = common04.get_neko_mecab()
res = [word['surface'] for word in word_list if word['pos'] == '動詞']
res[0:50]
