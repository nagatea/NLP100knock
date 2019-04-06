#%% [markdown]
# ## 17. １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
# ### 方針
# * 1列目の`list`をそのまま`set`に変換する

#%%
import common02
hightemp = common02.get_hightemp()
col = [word.split("\t")[0] for word in hightemp]
print(set(col))

#%%
tmp = common02.unix_run('sort col1.txt')
with open('tmp.txt', mode='w') as f:
  f.write(tmp)
res = common02.unix_run('uniq tmp.txt')
print(res)