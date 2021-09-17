from PIL import Image, ImageDraw, ImageFont
from collections import defaultdict
import numpy as np


def weighted_chars():
    font = ImageFont.load_default()
    weights = defaultdict(list)
    for i in range(32, 127):
        weights[np.mean(font.getmask(chr(i)))] += [chr(i)]
    return np.asarray([v[0] for v in weights.values()])


def asciipie(input_file, output_file='output.png'):
    # Load Font
    font = ImageFont.load_default()
    char_width, char_height = font.getsize('A')
    ratio = char_height / char_width

    # Load Image
    img = Image.open(input_file).convert('L')
    img_width, img_height = img.size
    size = (img_width, int(img_height / ratio))
    img = np.array(img.resize(size))

    # Image -> ASCII
    chars = np.asarray(list(' .,-;*?vIJV7&%#A@80$'))
    normalized_img = (img - img.min()) / (img.max() - img.min())
    stretched_img = normalized_img * (chars.size - 1)
    img_mask = stretched_img.astype(int)
    lines = [''.join(r) for r in chars[img_mask]]

    # ASCII -> Image
    image_height = int(char_height * len(lines))
    image_width = font.getsize(lines[0])[0]
    image = Image.new('L', (image_width, image_height), 0)
    draw = ImageDraw.Draw(image)
    for i, line in enumerate(lines):
        draw.text((0, char_height * i), line, 255)
    image.save(output_file)
