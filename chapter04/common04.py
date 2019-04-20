def get_neko_mecab():
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
  return res