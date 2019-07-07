from TxtImageSource import TxtImageSource
from PilTruetypeSource import PilTruetypeSource

from VerticalBitArrayBackend import VerticalBitArrayBackend

from CppGenerator import CppGenerator

printable_ascii_set = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
reduced_char_set = """ ABCDEFGHIJKLMNOPQRSTUVWXYZ+-.:;<=>?0123456789"""
gen = CppGenerator(TxtImageSource("5x7.txt", 5, 7), VerticalBitArrayBackend())
generated = gen.generate(reduced_char_set, "Font5x7Data")
with open("Font5x7.cpp", 'w') as f:
  for line in generated:
    f.write(line + '\n')

gen = CppGenerator(TxtImageSource("3x5.txt", 3, 5), VerticalBitArrayBackend())
generated = gen.generate(reduced_char_set, "Font3x5Data")
with open("Font3x5.cpp", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    
gen = CppGenerator(PilTruetypeSource("arial.ttf", 20, None, 24, -3), VerticalBitArrayBackend())
generated = gen.generate(printable_ascii_set, "FontArial16Data")
with open("FontArial16.cpp", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    
gen = CppGenerator(PilTruetypeSource("arial.ttf", 43, None, 40, -8), VerticalBitArrayBackend())
generated = gen.generate(printable_ascii_set, "FontArial32Data")
with open("FontArial32.cpp", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    