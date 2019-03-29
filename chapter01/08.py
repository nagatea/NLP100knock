#%% [markdown]
# ## 08. 暗号文
# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

# * 英小文字ならば(219 - 文字コード)の文字に置換
# * その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．

# ### 方針
# * 問題文に書いてあることをやる
# * ASCIIの番号に変換してくれる`ord`というものがあるらしい
# * 復号は`chr`

#%%
def cipher(string):
  res = []
  for char in list(string):
    code_num = ord(char)
    if (code_num >= 96 and code_num <= 122):
      code_num = 219 - code_num
    res.append(chr(code_num))
  return ''.join(res)

#%%
cipher("abcdeABCDE12345")
#%%
cipher(cipher("abcdeABCDE12345"))