import cv2


# lets define the function for mouse event
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # this is the event for left click of mouse

        print(x * 2, ',', y * 2)  # it will print the x,y coordinates

        strxy = str(x * 2) + ',' + str(y * 2)

        cv2.putText(img, "IVAN DUARTE ORTIZ", (x * 2, y * 2), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 1)

        porcentaje = 50

        altura = int(img.shape[0] * porcentaje / 100)

        ancho = int(img.shape[1] * porcentaje / 100)

        tamaño = (ancho, altura)

        escalado = cv2.resize(img, tamaño, interpolation=cv2.INTER_AREA)

        cv2.imshow('image', escalado)


img = cv2.imread('Diploma 2020-2021.png', cv2.IMREAD_UNCHANGED)

scale_percent = 50

height = int(img.shape[0] * scale_percent / 100)

width = int(img.shape[1] * scale_percent / 100)

dsize = (width, height)

resized = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)

cv2.imshow("image", resized)

cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()
