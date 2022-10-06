import os

import cv2
import time

import numpy as np


def taking_photos(camera_idx, rate, images_dir):
    cap = cv2.VideoCapture(camera_idx)

    images = np.zeros((100, 480, 640, 3))
    for i in range(100):
        ret, frame = cap.read()
        images[i] = frame
        time.sleep(1/rate)
    cap.release()

    for i in range(len(images)):
        cv2.imwrite(f"{images_dir}/0{i:0>3}.jpg", images[i])


def show():
    images_name = os.listdir('./image_set/')
    images_name.sort(key=lambda x: int(x[:-4]))
    for i in range(100):
        image_name = images_name[i]
        image = cv2.imread(f'./image_set/{image_name}')
        cv2.imshow('image', image)
        cv2.waitKey(0)


if __name__ == '__main__':
    images_dir = './data/image1'
    rate = 30
    camera_idx = 0
    # 连续拍摄，获取数据集
    taking_photos(camera_idx, images_dir, rate)


