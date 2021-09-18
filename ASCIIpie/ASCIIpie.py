from PIL import Image, ImageDraw, ImageFont
from collections import defaultdict
import numpy as np


def weighted_chars():
    font = ImageFont.load_default()
    weights = defaultdict(list)
    for i in range(32, 127):
        weights[np.mean(font.getmask(chr(i)))] += [chr(i)]
    return np.asarray([v[0] for v in weights.values()])


def asciipie(input_file, output_file=None, keep_color=True, output_format='png'):
    # Load Font
    font = ImageFont.load_default()
    char_width, char_height = font.getsize('A')
    ratio = char_height / char_width

    # Prepare Image
    img = Image.open(input_file)
    img_width, img_height = img.size
    if output_format == 'txt':
        chars_per_line = 160
        new_height = int((chars_per_line * img_height) / (ratio * img_width))
        new_size = (chars_per_line, new_height)
    else:
        new_size = (img_width, int(img_height / ratio))
    img = img.resize(new_size)
    grayscale = np.array(img.convert('L'))

    # Image -> ASCII
    chars = np.asarray(list(' .,-;*?vIJV7&%#A@80$'))
    normalized_img = (grayscale - grayscale.min()) / (grayscale.max() - grayscale.min())
    stretched_img = normalized_img * (chars.size - 1)
    img_mask = stretched_img.astype(int)
    lines = [''.join(r) for r in chars[img_mask]]
    if output_format == 'txt':
        output_file = output_file or 'output.txt'
        with open(output_file, 'w') as f:
            f.write('\n'.join(lines))
        return

    # ASCII -> Image
    new_height = int(char_height * len(lines))
    new_width = font.getsize(lines[0])[0]
    new_size = (new_width, new_height)
    mode = 'RGB' if keep_color else 'L'
    output = Image.new(mode, new_size, 0)
    draw = ImageDraw.Draw(output)
    if keep_color:
        color = np.array(img.convert('RGB'))
        for (i, j) in np.ndindex(color.shape[:2]):
            draw.text((char_width * j, char_height * i), lines[i][j], '#%02x%02x%02x' % tuple(color[(i, j)]))
    else:
        for i, line in enumerate(lines):
            draw.text((0, char_height * i), line, 255)
    output_file = output_file or 'output.png'
    output.save(output_file)
