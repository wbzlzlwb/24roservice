# from skimage.measure import compare_ssim
from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2
import numpy as np
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("original")
    parser.add_argument("modified")
    return parser.parse_args()


def main():
    args = parse_args()
    imageA = cv2.imread(args.original)
    imageB = cv2.imread(args.modified)
    # if needed resize images using cv2.resize()
    # cv2.imshow("Original", imageA)
    # cv2.imshow("Modified", imageB)
    # cv2.waitKey(0)
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print(f"SSIM: {score}")
    thresh = cv2.threshold(
                 diff, 0, 200, 
                 cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU
             )[1]
    cnts, _ = cv2.findContours(
                thresh, 
                cv2.RETR_EXTERNAL, 
                cv2.CHAIN_APPROX_SIMPLE
              )
    for c in cnts:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.drawContours(imageB, [c], -1, (0, 0, 255), 2)
    cv2.imshow("Original", imageA)
    cv2.imshow("Modified", imageB)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()