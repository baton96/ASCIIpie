import numpy as np
import cv2


def asciipie(input_file, output_file=None, text_mode=False, save=True):
    # Load Font
    font = cv2.FONT_HERSHEY_PLAIN
    (char_width, char_height), char_baseline = cv2.getTextSize(text='$', fontFace=font, fontScale=1, thickness=1)
    ratio = char_height / char_width

    # Prepare Image
    if not save:
        nparr = np.fromstring(input_file.stream.read(), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    else:
        img = cv2.imread(input_file)
    img_width, img_height, _ = img.shape
    new_width = img_width / char_width
    if text_mode:
        new_width = 160
    new_height = (new_width * img_height) / (ratio * img_width)
    new_width, new_height = int(new_width), int(new_height)
    new_size = (new_width, new_height)
    img = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Image -> ASCII
    chars = np.asarray(list('_~/Y7XK0A9P6ER8B$'))
    normalized_img = (grayscale - grayscale.min()) / (grayscale.max() - grayscale.min())
    stretched_img = normalized_img * (chars.size - 1)
    img_mask = stretched_img.astype(int)
    lines = [''.join(r) for r in chars[img_mask]]

    # Text output
    if text_mode:
        text = '\n'.join(lines)
        if save:
            output_file = output_file or 'output.txt'
            with open(output_file, 'w') as f:
                f.write(text)
        return text

    # ASCII -> Image
    new_height = int((char_height + char_baseline) * len(lines))
    new_width = char_width * len(lines[0])
    new_size = (new_height, new_width, 3)
    output = np.zeros(new_size, dtype='uint8')
    for (i, j) in np.ndindex(img.shape[:2]):
        r, g, b = img[(i, j)]
        color = (int(r), int(g), int(b))
        output = cv2.putText(
            img=output,
            text=lines[i][j],
            org=(char_width * j, (char_height + char_baseline) * i + char_height),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color=color
        )
    if save:
        output_file = output_file or 'output.png'
        cv2.imwrite(output_file, output)
    _, output = cv2.imencode('.png', output)
    return output
