#%% [markdown]
# ## 18. 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
# ### 方針
# * `list.sort()`
# * キーに`split("\t")[2]`(3カラム目)を指定

#%%
import common02
hightemp = common02.get_hightemp()
hightemp.sort(reverse=True, key=lambda temp: temp.split("\t")[2])
print(''.join(hightemp))

#%%
unix = common02.unix_run('sort -k 3 -r hightemp.txt')
print(unix)