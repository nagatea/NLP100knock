#%% [markdown]
# ## 04. 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
# ### 方針
# 1. 単語に分ける
# 1. 1文字または2文字切り出す
# 1. 単語番号への連想配列を作る

#%%
req = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_word = [1, 5, 6, 7, 8, 9, 15, 16, 19]
res = {}
i = 0
for word in req.split(" "):
  i += 1
  if i in one_word:
    tmp = word[0]
  else:
    tmp = word[0:2]
  res[tmp] = i
res