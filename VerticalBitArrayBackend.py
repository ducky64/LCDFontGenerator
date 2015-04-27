class VerticalBitArrayBackend(object):
  def __init__(self, grey_threshold=0.5):
    self.grey_threshold = grey_threshold
    
  def image_to_bytes(self, image):
    out = []
    width, height = image.size
    for x in range(width):
      col = []
      curr_byte = 0
      for y in range(height):
        if (y % 8 == 0) and y != 0:
          col.append(curr_byte)
          curr_byte = 0
        
        grey = image.getpixel((x, y))
        if grey > self.grey_threshold:
          bit = 1
        else:
          bit = 0
        curr_byte |= bit << (y % 8)
      col.append(curr_byte)
      out.append(col)
    return out
  