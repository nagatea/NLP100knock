#%%[markdown]
# # 第4章: 形態素解析
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．

# ## 30. 形態素解析結果の読み込み
# 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．


#%%
res = []
with open('neko.txt.mecab') as f:
  for line in f:
    tmp = line.split('\t')
    if tmp[0] == 'EOS\n':
      continue
    surface = tmp[0]
    word = tmp[1].split(',')
    if word[6] == '*\n':
      base = surface
    else:
      base = word[6]
    dic = {
      'surface': surface,
      'base': base,
      'pos': word[0],
      'pos1': word[1]
    }
    res.append(dic)

res[0:20]
