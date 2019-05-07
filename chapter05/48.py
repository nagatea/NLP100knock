#%% [markdown]
# ## 48. 名詞から根へのパスの抽出
# 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ． ただし，構文木上のパスは以下の仕様を満たすものとする．
# * 各文節は（表層形の）形態素列で表現する
# * パスの開始文節から終了文節に至るまで，各文節の表現を"`->``"で連結する
#
#
# 「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．
# ```
# 吾輩は -> 見た
# ここで -> 始めて -> 人間という -> ものを -> 見た
# 人間という -> ものを -> 見た
# ものを -> 見た
# ```

#%%
import common05
data = common05.get_chunk_list()

res = []
for chunks in data:
  for chunk in chunks:
    if '名詞' in [morph.pos for morph in chunk.morphs]:
      chunk_list = []
      tmp_chunk = chunk
      while True:
        chunk_list.append(tmp_chunk)
        if tmp_chunk.dst == -1:
          break
        tmp_chunk = chunks[tmp_chunk.dst]
      if len(chunk_list) > 0:
        morph_list = []
        for chu in chunk_list:
          morph_list.append(''.join([morph.surface for morph in chu.morphs if morph.pos != '記号']))
        res.append(' -> '.join(morph_list))

res[0:50]
