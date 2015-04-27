from PIL import Image, ImageFont, ImageDraw

class PilTruetypeSource(object):
  def __init__(self, font_filename, font_size, width, height, draw_height):
    self.font = ImageFont.truetype(font_filename, font_size)
    
    self.width = width
    self.height = height
    self.draw_height = draw_height
    
  def get_image(self, key):
    if self.width is not None:
      width = self.width
    else:
      width, _ = self.font.getsize(key)
      
    image = Image.new('1', (width, self.height))
    draw = ImageDraw.Draw(image)
    draw.text((0, self.draw_height), key, font=self.font, fill=255)

    if self.width is None:
      # For variable sizing, also crop out the excess
      left_crop = 0
      for x in range(width):
        if not self.image_col_clear(image, x):
          left_crop = x
          break
        
      right_crop = width
      for x in reversed(range(width)):
        if not self.image_col_clear(image, x):
          right_crop = x
          break
          
      print((left_crop, right_crop))
      image = image.crop((left_crop, 0, 
                          right_crop+1, self.height))

    return image

  def image_col_clear(self, im, x):
    _, height = im.size
    for y in range(height):
      if im.getpixel((x, y)) > 0:
        return False
    return True