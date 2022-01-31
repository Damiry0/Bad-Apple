import cv2


def frameCapture(path):
    vidObj = cv2.VideoCapture(path)

    count = 0

    success = 1

    while success:
        success, image = vidObj.read()
        dim = (128,64)
        resizedImage = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)

        cv2.imwrite("frame%d.jpg" % count, resizedImage)

        count += 1


if __name__ == '__main__':
    frameCapture("bad_apple.mp4")
