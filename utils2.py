from urllib.request import urlretrieve
import cv2 as cv

def download_save_image(url, filename):
    """download and save image"""

    urlretrieve(url, filename)
    
def display_images(images, titles):
    """"""
    for img, title in zip(images, titles):
        cv.imshow(title, img)

    cv.waitKey(0)
    cv.destroyAllWindows()

