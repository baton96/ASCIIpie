from PIL import Image, ImageDraw, ImageFont
import numpy as np


def asciipie_with_color(input_file, output_file='output.png'):
    font = ImageFont.load_default()
    char_width, char_height = font.getsize('A')
    ratio = char_height / char_width

    img = Image.open(input_file).convert('RGB')
    img_width, img_height = img.size
    size = (int(img_width * ratio), img_height)
    arr = np.array(img.resize(size))

    img_new = Image.new(
        'RGB',
        (int(char_width * img_width * ratio), char_height * img_height),
        0
    )
    draw = ImageDraw.Draw(img_new)
    for (i, j) in np.ndindex(arr.shape[:2]):
        draw.text((char_width * j, char_height * i), '@', '#%02x%02x%02x' % tuple(arr[(i, j)]))
    img_new = img_new.resize(img.size)
    img_new.save(output_file)

