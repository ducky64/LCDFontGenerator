class CppGenerator(object):
  def __init__(self, image_src, backend):
    self.image_src = image_src
    self.backend = backend
    
  def generate(self, charset, varname_prefix):
    out = []
    widths = {}
    varnames = {}
    
    for char in charset:
      chardef, varname, width = self.generate_char(char, varname_prefix)
      out.extend(chardef)
      
      widths[char] = width
      varnames[char] = varname
      
    out.append("")
      
    out.append("const uint8_t* %s_CHARS[] = {" % (varname_prefix))
    for char in charset:
      out.append(varnames[char] + ",")
    out.append("};")
    
    out.append("const uint8_t %s_WIDTHS[] = {" % (varname_prefix))
    for char in charset:
      out.append(str(widths[char]) + ",")
    out.append("};")
    
    
    out.append("const uint8_t %s_WIDTH_MAX = %i;" % (varname_prefix,
                                                     max(widths.values())))
          
    return out

  def generate_char(self, char, varname_prefix):
    out = []
    image = self.image_src.get_image(char)
    char_bytes = self.backend.image_to_bytes(image)
    
    varname = varname_prefix + "_CHAR_" + char
    out.append("const uint8_t %s[] = {" % (varname))
    for byte_row in char_bytes:
      line = ""
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
  