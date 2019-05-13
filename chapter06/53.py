#%% [markdown]
# ## 53. Tokenization
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．

#%%
import xml.etree.ElementTree as ET

root = ET.parse('nlp.txt.xml')

res = [word.text for word in root.iter('word')]

res
