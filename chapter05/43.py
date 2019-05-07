#%% [markdown]
# ## 43. 名詞を含む文節が動詞を含む文節に係るものを抽出
# 名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

#%%
import common05
data = common05.get_chunk_list()
res = []
for chunks in data:
  for chunk in chunks:
    if len(chunk.srcs) > 0:
      for src in chunk.srcs:
        if ('名詞' in [morph.pos for morph in chunks[src].morphs]) and ('動詞' in [morph.pos for morph in chunk.morphs]):
          res.append(f'{"".join([morph.surface for morph in chunks[src].morphs if morph.pos != "記号"])}\t{"".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])}')

res[0:50]
