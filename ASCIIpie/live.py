import numpy as np
import cv2

font = cv2.FONT_HERSHEY_PLAIN
(char_width, char_height), char_baseline = cv2.getTextSize(text='$', fontFace=font, fontScale=1, thickness=1)
ratio = char_height / char_width
chars = np.asarray(list('_~/Y7XK0A9P6ER8B$'))

vid = cv2.VideoCapture(0)
while True:
    _, img = vid.read()
    img_width, img_height, _ = img.shape
    new_width = img_width / char_width
    new_height = (new_width * img_height) / (ratio * img_width)
    new_width, new_height = int(new_width), int(new_height)
    new_size = (new_width, new_height)
    img = cv2.resize(img, new_size, interpolation=0)
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    normalized_img = (grayscale - grayscale.min()) / (grayscale.max() - grayscale.min())
    stretched_img = normalized_img * (chars.size - 1)
    img_mask = stretched_img.astype(int)
    lines = [''.join(r) for r in chars[img_mask]]

    new_height = int((char_height + char_baseline) * len(lines))
    # new_width = char_width * len(lines[0])
    (new_width, _), _ = cv2.getTextSize(text=lines[0], fontFace=font, fontScale=1, thickness=1)
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
    cv2.imshow('ASCIIpie', np.array(output))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
