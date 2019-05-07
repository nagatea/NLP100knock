#%% [markdown]
# ## 47. 機能動詞構文のマイニング
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．46のプログラムを以下の仕様を満たすように改変せよ．
# * 「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
# * 述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
# * 述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
# * 述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）
#
#
# 例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，以下の出力が得られるはずである．
# ```
# 返事をする      と に は        及ばんさと 手紙に 主人は
# ```
# このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
# * コーパス中で頻出する述語（サ変接続名詞+を+動詞）
# * コーパス中で頻出する述語と助詞パターン


#%%
import common05
data = common05.get_chunk_list()
res = []

for chunks in data:
  i = 0
  for chunk in chunks:
    if len(chunk.srcs) > 0 and i > 0:
      if '名詞' in [morph.pos for morph in chunks[i-1].morphs] and 'を' in [morph.surface for morph in chunks[i-1].morphs]:
        zyosi_list = []
        for src in chunk.srcs:
          if '助詞' in [morph.pos for morph in chunks[src].morphs] and not ('を' in [morph.surface for morph in chunks[src].morphs]):
            zyosi_list.append(([morph.base for morph in chunks[src].morphs if morph.pos == '助詞'][0], ''.join([morph.surface for morph in chunks[src].morphs if morph.pos != '記号'])))
        if len(zyosi_list) > 0:
          zyosi_list.sort(key=lambda x: x[0])
          if i < len(chunks):
            res.append(f'{"".join([morph.surface for morph in chunks[i-1].morphs if morph.pos != "記号"] + [morph.surface for morph in chunk.morphs if morph.pos != "記号"])}\t{" ".join([a for (a, b) in zyosi_list])}\t{" ".join([b for (a, b) in zyosi_list])}')
    i += 1

res[0:50]

#%%
with open('47.txt', 'w') as f:
  f.write('\n'.join(res))
