#%% [markdown]
# ## 11. タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
# ### 方針
# * `str.replace`

#%%
import common02
hightemp = common02.get_hightemp()
res = [word.replace("\t", " ") for word in hightemp]
print(''.join(res))

#%%
unix = common02.unix_run('sed s/\t/\x20/g hightemp.txt')
print(unix)