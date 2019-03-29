#%% [markdown]
# ## 05. n-gram
# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
# ### 方針
# * 要するにn文字で分割してリストを返すという認識でいいんだろうか...
# * 与えられたものを一度文字列に戻す作業をする
# * 分割して結果をリストで返す

#%%
def n_gram(req, n: int):
  if type(req) is list:
    req = " ".join(req)
  res = []
  for i in range(len(req)):
    if n*i >= len(req):
      break
    res.append(req[n*i:n*(i+1)])
  return res

#%%
n_gram("I am an NLPer".split(), 2)
#%%
n_gram("I am an NLPer", 2)