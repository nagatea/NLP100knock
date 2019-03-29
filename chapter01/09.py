#%% [markdown]
# ## 09. Typoglycemia
# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
# ### 方針
# * 先頭と末尾はtmpで保持
# * `shuffle`みたいな関数ないかなあ
#   * randomにあるらしい
#   * `shuffle`は破壊的メソッドなので`sample`を使う

#%%
import random

def typoglycemia(string: str):
  word_list = string.split()
  if len(word_list) <= 4:
    return string
  head = word_list[0]
  tail = word_list[-1]
  rand = random.sample(word_list[1:-1], len(word_list)-2)
  return ' '.join(list(head) + rand + list(tail))

req = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typoglycemia(req)
