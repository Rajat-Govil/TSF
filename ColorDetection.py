import cv2 as cv

image = cv.imread('/Users/rajatgovila/Desktop/flowers.jpeg')

img = cv.resize(image, (750, 600))                          # resize the image
cv.imshow('flowersresized', img)


def draw_fn(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]

        b = int(b)
        g = int(g)
        r = int(r)
        text = 'B = ' + str(b) + ',  G = ' + str(g) + ',  R = ' + str(r)

        cv.rectangle(img, (120, 20), (600, 60), (255, 255, 255), thickness=cv.FILLED)
        cv.putText(                                         # prints the colored text
            img,
            text,
            (120, 55),
            cv.FONT_HERSHEY_DUPLEX,
            1, (b, g, r), 2)
        cv.imshow('flowersresized', img)


cv.setMouseCallback('flowersresized', draw_fn)
cv.waitKey(0)
cv.destroyAllWindows()
