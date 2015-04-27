from PIL import Image

class TxtImageSource(object):
  def __init__(self, txt_filename, width, height):
    self.chars = {}
    
    with open(txt_filename) as f:
      self.chars.update(self.lines_to_chars(f.readlines(), width, height))
      
  def lines_to_chars(self, lines, width, height):
    out = {}
    current_key = None
    current_im = None
    current_pix = None
    current_y = 0
    for line in lines:
      if line.startswith('!'):
        if current_key and current_im:
          out[current_key] = current_im
        current_key = line[1:-1]
        current_im = Image.new('1', (width, height))
        current_pix = current_im.load()
        current_y = 0
      else:
        current_x = 0
        for pix_char in line:
          if pix_char == ' ':
            current_pix[current_x, current_y] = 0
          elif pix_char == 'x':
            current_pix[current_x, current_y] = 1
          elif pix_char == '\r' or pix_char == '\n':
            pass
          else:
            assert False
          current_x += 1
        current_y += 1
    return out
  
  def get_image(self, key):
    return self.chars[key]
