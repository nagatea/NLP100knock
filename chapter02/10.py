#%% [markdown]
# # 第2章 UNIXコマンドの基礎
# hightemp.txtは，日本の最高気温の記録を「都道府県」「地点」「℃」「日」のタブ区切り形式で格納したファイルである．以下の処理を行うプログラムを作成し，hightemp.txtを入力ファイルとして実行せよ．さらに，同様の処理をUNIXコマンドでも実行し，プログラムの実行結果を確認せよ．
# ## 10. 行数のカウント
# 行数をカウントせよ．確認にはwcコマンドを用いよ．
# ### 方針
# * データをリストに格納してリストの要素数をカウントする

#%%
import common02
hightemp = common02.get_hightemp()

#%%
res = len(hightemp)
print(res)

#%%
unix = common02.unix_run('wc -l hightemp.txt')
print(unix)


#%%
