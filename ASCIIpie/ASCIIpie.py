import numpy as np
import cv2

# Load Font
(char_width, char_height), char_baseline = cv2.getTextSize(
    text='$',
    fontFace=cv2.FONT_HERSHEY_PLAIN,
    fontScale=1,
    thickness=1
)
ratio = char_height / char_width


def asciipie_file(input_file, output_file=None):
    img = cv2.imread(input_file)
    output = asciipie(img)
    cv2.imwrite(output_file, output)


def asciipie_bytes(input_file):
    bytes_string = input_file.stream.read()
    bytes_array = np.fromstring(bytes_string, np.uint8)
    img = cv2.imdecode(bytes_array, cv2.IMREAD_COLOR)
    output = asciipie(img)
    _, output = cv2.imencode('.png', output)
    output = output.tobytes()
    return output


def asciipie(img):
    # Prepare Image
    img_height, img_width, _ = img.shape
    new_width = img_width / char_width
    new_height = (new_width * img_height * ratio) / img_width - char_baseline // 2
    new_width, new_height = int(new_width), int(new_height)
    new_size = (new_width, new_height)
    img = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Image -> ASCII
    chars = np.asarray(list('Y7XK0A9P6ER8B$'))
    normalized_img = (grayscale - grayscale.min()) / (grayscale.max() - grayscale.min())
    stretched_img = normalized_img * (chars.size - 1)
    img_mask = stretched_img.astype(int)
    lines = [''.join(r) for r in chars[img_mask]]

    # ASCII -> Image
    new_height = int((char_height + char_baseline // 2) * len(lines))
    new_width = char_width * len(lines[0])
    new_size = (new_height, new_width, 4)
    output = np.zeros(new_size, dtype=np.uint8)
    for (i, j) in np.ndindex(img.shape[:2]):
        r, g, b = img[(i, j)]
        color = (int(r), int(g), int(b), 255)
        output = cv2.putText(
            img=output,
            text=lines[i][j],
            org=(char_width * j, (char_height + char_baseline // 2) * i + char_height),
            fontFace=cv2.FONT_HERSHEY_PLAIN,
            fontScale=1,
            color=color,
            thickness=2
        )
    return output
