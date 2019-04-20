#%% [markdown]
# ## 32. 動詞の原形
# 動詞の原形をすべて抽出せよ．
# ### 方針
# * posが動詞になっているもののsurfaceをリスト化する

#%%
import common04
word_list = common04.get_neko_mecab()
res = [word['base'] for word in word_list if word['pos'] == '動詞']
res[0:50]
