from algorithms.utils import read_image
import pytesseract


def tesseract(image_name):
    image = read_image(image_name)
    return pytesseract.image_to_string(image, lang="tesseract")


def kraken(inmemory_image):
    image = read_opencv_image(inmemory_image)
    return pytesseract.image_to_string(image, lang="eng")


def ocropus(image_name):
    image = read_image(image_name)
    return pytesseract.image_to_string(image, lang="vie")
