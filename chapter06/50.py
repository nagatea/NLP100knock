#%% [markdown]
# # 第6章: 英語テキストの処理
# 英語のテキスト（nlp.txt）に対して，以下の処理を実行せよ．

# ## 50. 文区切り
# (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

#%%
import re
pattern = re.compile(r'(^.*?[\.|;|:|\?|!])\s([A-Z].*)', re.MULTILINE + re.VERBOSE + re.DOTALL)
res = []
with open('nlp.txt') as f:
  for line in f:
    line = line.strip()
    while len(line) > 0:
      match = pattern.match(line)
      if match:
        res.append(match.group(1))
        line = match.group(2)
      else:
        res.append(line)
        line = ''

res

#%%
with open('50.txt', 'w') as f:
  f.write('\n'.join(res))
