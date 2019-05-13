#%% [markdown]
# ## 54. 品詞タグ付け
# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．

#%%
import xml.etree.ElementTree as ET
root = ET.parse('nlp.txt.xml')

res = []
for token in root.iter('token'):
  words = list(map(lambda i: token[i].text, [0,1,4]))
  res.append('\t'.join(words))

res

#%%
with open('54.txt', 'w') as f:
  f.write('\n'.join(res))
