class CppGenerator(object):
  def __init__(self, image_src, backend):
    self.image_src = image_src
    self.backend = backend
    
  def generate(self, charset, varname_prefix):
    out = []
    widths = {}
    varnames = {}
    ord_charset = [ord(char) for char in charset]
    
    out.append("#include <cstdint>")
    out.append("#include <cstddef>")
    out.append("")
    
    out.append("namespace %s {" % (varname_prefix))
    
    for char in charset:
      chardef, varname, width = self.generate_char(char, varname_prefix)
      out.extend(chardef)
      
      widths[ord(char)] = width
      varnames[ord(char)] = varname
      
    out.append("")
      
    out.append("const uint8_t* Chars[] = {")
    for i in range(32, 127):
      if i in ord_charset:
        out.append("  %s,  // '%s' %s" % (varnames[i], chr(i), i))
      else:
        out.append("  NULL,  // '%s' %s" % (chr(i), i))
    out.append("};")
    
    out.append("const uint8_t Widths[] = {")
    for i in range(32, 127):
      if i in ord_charset:
        out.append("  %s, // '%s' %s" % (str(widths[i]), chr(i), i))
      else:
        out.append("  0, // '%s' %s" % (chr(i), i))
    out.append("};")
    
    
    out.append("const uint8_t MaxWidth = %i;" % (max(widths.values())))
    
    out.append("}")
    
    return out

  def generate_char(self, char, varname_prefix):
    out = []
    image = self.image_src.get_image(char)
    char_bytes = self.backend.image_to_bytes(image)
    
    varname = "Char" + str(ord(char))
    out.append("const uint8_t %s[] = { // %s" % (varname, char))
    for byte_row in char_bytes:
      line = "  "
      for byte in byte_row:
        line += "0x" + format(byte, '02x') + ","
      line += "  //"
      for byte in byte_row:
        line += " " + self.byte_to_string(byte)
      out.append(line)
    out.append("};")
    
    width, _ = image.size
    
    return (out, varname, width)
    
  def byte_to_string(self, in_byte):
    out = ""
    for _ in range(8):
      if in_byte & 0x80:
        out += '#'
      else:
        out += '.'
      in_byte <<= 1;
    return out
  