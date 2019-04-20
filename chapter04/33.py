#%% [markdown]
# ## 33. サ変名詞
# サ変接続の名詞をすべて抽出せよ．
# ### 方針
# * pos1がサ変接続になっているもののbaseをリスト化する

#%%
import common04
word_list = common04.get_neko_mecab()
res = [word['base'] for word in word_list if word['pos1'] == 'サ変接続']
res[0:50]
