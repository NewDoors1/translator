# -*- coding: utf-8 -*-
"""translator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C6q4cCycF7C-eglstn_ZdjYIxo_qpOWp
"""

pip install translate

from translate import Translator
s = Translator(from_lang="english", to_lang = "portuguese")

res = s.translate("go")
print(res)