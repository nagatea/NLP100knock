#%% [markdown]
# ## 19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
# ### 方針
# * `conut()`

#%%
import common02
hightemp = common02.get_hightemp()
col1 = [word.split("\t")[0] for word in hightemp]
word_list = set(col1)
res = []
for word in word_list:
  res.append((word ,col1.count(word)))
res.sort(key=lambda tmp: tmp[1], reverse=True)
res
#%%
# cut -c 1-4 hightemp.txt | sort | uniq -c | sort -r
cut = common02.unix_run('cut -c 1-4 hightemp.txt')
with open('tmp.txt', mode='w') as f:
  f.write(cut)

sort = common02.unix_run(f'sort tmp.txt')
with open('tmp.txt', mode='w') as f:
  f.write(sort)

uniq = common02.unix_run('uniq -c tmp.txt')
with open('tmp.txt', mode='w') as f:
  f.write(uniq)

unix = common02.unix_run('sort -r tmp.txt')
print(unix)