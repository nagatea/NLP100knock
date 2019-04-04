#%% [markdown]
# ## 12. 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
# ### 方針
# * タブで`split`して1番目のデータをcol1に、2番目のデータをcol2に

#%%
import common02

hightemp = common02.get_hightemp()
col1 = [word.split("\t")[0] for word in hightemp]
col2 = [word.split("\t")[1] for word in hightemp]
with open('col1.txt', mode='w') as f:
  f.write('\n'.join(col1))
with open('col2.txt', mode='w') as f:
  f.write('\n'.join(col2))

#%%
unix1 = common02.unix_run('cat col1.txt')
unix2 = common02.unix_run('cat col2.txt')
print(unix1)
print(unix2)