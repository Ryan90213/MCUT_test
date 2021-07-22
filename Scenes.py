def Scenes():
    import cv2
    import os
    import random as rm

#-----------------------------------------------------#

    ready = cv2.imread('Ready.jpg')
    array_of_img = []
    replay=0

#-----------------------------------------------------#

    def read_directory(directory):
        for file in os.listdir("./" + directory):
            img = cv2.imread(directory + "/" + file)
            array_of_img.append(img)

#-----------------------------------------------------#

    read_directory("project01")
    lend = len(array_of_img)

#-----------------------------------------------------#

    while replay<10:
        ptr = rm.randint(0,lend-1)

        event=0     #狀態信號,休息
        cv2.namedWindow('picture', cv2.WINDOW_NORMAL)
        cv2.imshow('picture', ready)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

        event=1     #狀態信號,顯示
        cv2.namedWindow('picture', cv2.WINDOW_NORMAL)
        cv2.imshow('picture',array_of_img[ptr])
        cv2.waitKey(5000)
        cv2.destroyAllWindows()

        replay+=1

# -----------------------------------------------------#