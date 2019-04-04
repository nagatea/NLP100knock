#%% [markdown]
# ## 13. col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
# ### 方針
# * `zip`でタプルを作って結合

#%%
with open('col1.txt') as f:
  col1 = f.read().split("\n")
with open('col2.txt') as f:
  col2 = f.read().split("\n")

res =["\t".join(words) for words in list(zip(col1, col2))]
print("\n".join(res))


#%%
import common02
unix = common02.unix_run('paste col1.txt col2.txt')
print(unix)