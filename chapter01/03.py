#%% [markdown]
# ## 03. 円周率
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
# ### 方針
# * `split(" ")`してイテレートして文字数を出す
#   * カンマとかドットも文字数としてカウントされるけどいいんだろうか

#%%
req = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
res = []
for word in req.split(" "):
  res.append(len(word))
res