#%% [markdown]
# ## 06. 集合
# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
# ### 方針
# * bi-gramは05の関数を使う
# * listをsetに変換したら楽にできそう

#%%
req1 = "paraparaparadise"
req2 = "paragraph"
X = set(n_gram(req1, 2))
Y = set(n_gram(req2, 2))
print(X)
print(Y)
#%%
# 和集合
X | Y
#%%
# 積集合
X & Y
#%%
# 差集合
X - Y
