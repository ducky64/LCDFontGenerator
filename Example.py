from TxtImageSource import TxtImageSource
from PilTruetypeSource import PilTruetypeSource

from VerticalBitArrayBackend import VerticalBitArrayBackend

from CppGenerator import CppGenerator

gen = CppGenerator(TxtImageSource("5x7.txt", 5, 7), VerticalBitArrayBackend())
generated = gen.generate("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", "FONT_5X7") 

with open("Font5x7.h", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    
gen = CppGenerator(PilTruetypeSource("arial.ttf", 20, None, 16, -3), VerticalBitArrayBackend())
generated = gen.generate("0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_'abcdefghijklmnopqrstuvwxyz", "FONT_ARIAL") 
with open("FontArial16.h", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    
gen = CppGenerator(PilTruetypeSource("arial.ttf", 43, None, 32, -8), VerticalBitArrayBackend())
generated = gen.generate(""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz""", "FONT_ARIAL") 
with open("FontArial32.h", 'w') as f:
  for line in generated:
    f.write(line + '\n')
    