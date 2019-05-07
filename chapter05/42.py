#%% [markdown]
# ##42. 係り元と係り先の文節の表示
# 係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．

#%%
import common05

data = common05.get_chunk_list()
res = []
for chunks in data:
  for chunk in chunks:
    if len(chunk.srcs) > 0:
      for src in chunk.srcs:
        res.append(f'{"".join([morph.surface for morph in chunks[src].morphs if morph.pos != "記号"])}\t{"".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])}')

res[0:50]
