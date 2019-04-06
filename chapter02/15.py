#%% [markdown]
# ## 15. 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
# ### 方針
# * 14の逆

#%%
import common02

n = common02.get_argv_n()
hightemp = common02.get_hightemp()
print(''.join(hightemp[len(hightemp)-n:]))

#%%
unix = common02.unix_run(f'tail -n {n} hightemp.txt')
print(unix)