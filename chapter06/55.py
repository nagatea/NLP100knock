#%% [markdown]
# ## 55. 固有表現抽出
# 入力文中の人名をすべて抜き出せ．

#%%
import xml.etree.ElementTree as ET
root = ET.parse('nlp.txt.xml')

res = []
for token in root.iter('token'):
    if token[5].text == "PERSON":
        res.append(token[0].text)

res
