#%% [markdown]
# ## 52. ステミング
# 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，単語と語幹をタブ区切り形式で出力せよ． Pythonでは，Porterのステミングアルゴリズムの実装としてstemmingモジュールを利用するとよい．

#%%
import snowballstemmer
stemmer = snowballstemmer.stemmer('english')

res = []
with open('51.txt') as f:
  for line in f:
    word = line.strip()
    res.append(f'{word} {stemmer.stemWord(word)}')

res
