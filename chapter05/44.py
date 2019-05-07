#%% [markdown]
# ## 44. 係り受け木の可視化
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
# ### 参考
# * [PyGraphvizをmacOSにインストールする](https://qiita.com/ryoppippi/items/f484eb995ff1e913dd44)
# * [PyGraphviz Tutorial](http://pygraphviz.github.io/documentation/pygraphviz-1.5/tutorial.html)

#%%
import common05
import pygraphviz as pgv
data = common05.get_chunk_list()

G = pgv.AGraph()

chunks = data[7]

for chunk in chunks:
  node = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
  if len(node) > 0:
    G.add_node(node)
  if len(chunk.srcs) > 0:
    for src in chunk.srcs:
      a = "".join([morph.surface for morph in chunks[src].morphs if morph.pos != "記号"])
      b = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
      if len(a) > 0 and len(b) > 0:
        G.add_edge(a, b)


#%%
G.layout(prog='dot')
G.draw('44.png')

#%%
import matplotlib.pyplot as plt
im = plt.imread('./44.png')
plt.imshow(im)
