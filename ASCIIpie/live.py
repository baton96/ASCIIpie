from ASCIIpie import asciipie
import cv2

vid = cv2.VideoCapture(0)
while True:
    _, frame = vid.read()
    asciipied = asciipie(frame)
    cv2.imshow('ASCIIpie', asciipied)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
