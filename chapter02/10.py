#%% [markdown]
# # 第2章 UNIXコマンドの基礎
# ## 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
# ### 方針
# * データをリストに格納してリストの要素数をカウントする

#%%
import common02
hightemp = common02.get_hightemp()

#%%
res = len(hightemp)
print(res)

#%%
unix = common02.unix_run('wc -l hightemp.txt')
print(unix)


#%%
