#%% [markdown]
# ## 41. 係り受け解析結果の読み込み（文節・係り受け）
# 40に加えて，文節を表すクラス`Chunk`を実装せよ．このクラスは形態素（`Morph`オブジェクト）のリスト（`morphs`），係り先文節インデックス番号（`dst`），係り元文節インデックス番号のリスト（`srcs`）をメンバ変数に持つこととする．さらに，入力テキストのCaboChaの解析結果を読み込み，１文を`Chunk`オブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

#%%
class Morph:
  def __init__(self, surface: str, base: str, pos: str, pos1: str):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1

class Chunk:
  def __init__(self, morphs: list, dst: int, srcs: list):
    self.morphs = morphs
    self.dst = dst
    self.srcs = srcs


res = []
index = -1
morph_list = []
dst_queue = []
chunk_list = []
with open('neko.txt.cabocha') as f:
  for line in f:
    tmp = line.split('\t')
    if tmp[0] == 'EOS\n':
      # EOS
      # 前のやつのChunkを保存
      if len(morph_list) > 0:
        chunk_list.append(Chunk(morph_list, dst, [i for i, d in dst_queue if d == index]))
        morph_list = []
        dst_queue = []
      if len(chunk_list) > 0:
        res.append(chunk_list)
        chunk_list = []
      continue
    if len(tmp) > 1:
      # 単語
      surface = tmp[0]
      word = tmp[1].split(',')
      if word[6] == '*\n':
        base = surface
      else:
        base = word[6]
      morph_list.append(Morph(surface, base, word[0], word[1]))
    else:
      # * 2 -1D 0/2 0.000000
      info = tmp[0].split()
      index = int(info[1])
      if index != 0:
        # 前のやつのChunkを保存
        chunk_list.append(Chunk(morph_list, dst, [i for i, d in dst_queue if d == index-1]))
        morph_list = []
      dst = int(info[2][0:-1])
      dst_queue.append((index, dst))


[[[morph.surface for morph in chunk.morphs], chunk.dst, chunk.srcs] for chunk in res[7]]
