#%% [markdown]
# ## 14. 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
# ### 方針
# * `sys.argv`で引数を受け取る
# * `str.isdecimal()`で数字かどうか判定できる(jupyter notebook用)
# * それをhightempに適用

#%%
import common02

n = common02.get_argv_n()
hightemp = common02.get_hightemp()
print(''.join(hightemp[0:n]))

#%%
unix = common02.unix_run(f'head -n {n} hightemp.txt')
print(unix)