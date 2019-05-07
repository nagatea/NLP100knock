#%% [markdown]
# # 第5章: 係り受け解析
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．
# ```
# $ cabocha -f1 neko.txt > neko.txt.cabocha
# ```
# ## 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラス`Morph`を実装せよ．このクラスは表層形（`surface`），基本形（`base`），品詞（`pos`），品詞細分類1（`pos1`）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文を`Morph`オブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

#%%
class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1


res = []
index = -1
morph_list = []
with open('neko.txt.cabocha') as f:
  for line in f:
    tmp = line.split('\t')
    if tmp[0] == 'EOS\n':
      continue
    if len(tmp) > 1:
      surface = tmp[0]
      word = tmp[1].split(',')
      if word[6] == '*\n':
        base = surface
      else:
        base = word[6]
      morph_list.append(Morph(surface, base, word[0], word[1]))
    else:
      if int(tmp[0].split()[1]) > index:
        index = int(tmp[0].split()[1])
      else:
        res.append(morph_list)
        morph_list = []
        index = -1

res[3]

#%%
[morph.surface for morph in res[3]]
