#%% [markdown]
# ## 51. 単語の切り出し
# 空白を単語の区切りとみなし，50の出力を入力として受け取り，1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．

#%%
res = []
with open('50.txt') as f:
  for line in f:
    line = line.strip()
    res = res + line.split(' ')

res

#%%
with open('51.txt', 'w') as f:
  f.write('\n'.join(res))
