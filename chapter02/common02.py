import subprocess
import sys

def get_hightemp():
  path = './hightemp.txt'
  with open(path) as f:
    hightemp = f.readlines()
  return hightemp

def unix_run(args):
  res = subprocess.run(args.split(), stdout = subprocess.PIPE)
  return res.stdout.decode('utf8')

def get_argv_n():
  if sys.argv[1].isdecimal():
    n = int(sys.argv[1])
  else:
    # 引数が存在しない場合は5を代入(jupyter notebook用)
    n = 5
  return n