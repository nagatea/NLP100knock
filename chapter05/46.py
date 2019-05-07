#%% [markdown]
# ## 46. 動詞の格フレーム情報の抽出
# 45のプログラムを改変し，述語と格パターンに続けて項（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．45の仕様に加えて，以下の仕様を満たすようにせよ．
# * 項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
# * 述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる
#
#
# 「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える． この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
# ```
# 始める  で      ここで
# 見る    は を   吾輩は ものを
# ```


#%%
import common05
data = common05.get_chunk_list()
res = []

for chunks in data:
  for chunk in chunks:
    if len(chunk.srcs) > 0:
      if '動詞' in [morph.pos for morph in chunk.morphs]:
        dousi = [morph.base for morph in chunk.morphs if morph.pos == '動詞'][0]
        zyosi_list = []
        for src in chunk.srcs:
          if ('助詞' in [morph.pos for morph in chunks[src].morphs]):
            zyosi_list.append(([morph.base for morph in chunks[src].morphs if morph.pos == '助詞'][0], ''.join([morph.surface for morph in chunks[src].morphs if morph.pos != '記号'])))
        if len(zyosi_list) > 0:
          zyosi_list.sort(key=lambda x: x[0])
          res.append(f'{dousi}\t{" ".join([a for (a, b) in zyosi_list])}\t{" ".join([b for (a, b) in zyosi_list])}')

res[0:50]

#%%
with open('46.txt', 'w') as f:
  f.write('\n'.join(res))
