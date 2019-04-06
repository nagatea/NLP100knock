#%% [markdown]
# ## 16. ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
# ### 方針
# * 行数を取ってきてNで割り、結果の行数分ファイルを作成する

#%%
import common02
hightemp = common02.get_hightemp()
n = len(hightemp) // common02.get_argv_n() + 1
for i in range(n):
  res = hightemp[n*i:n*(i+1)]
  with open(chr(97+i), mode='w') as f:
    f.write(''.join(res))

#%%
common02.unix_run('split -l 5 hightemp.txt')