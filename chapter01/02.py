#%% [markdown]
# ## 02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
# ### 方針
# * for文で要素同士を結合していくのがいいのかな
#   * 同じ文字数だからできる

#%%
police_car = "パトカー"
taxi = "タクシー"
res = ""
for i in range(len(police_car)):
  res += police_car[i]
  res += taxi[i]
res