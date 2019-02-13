from algorithms.utils import read_image
import pytesseract
import subprocess


def run_ocr_tesseract(image_name):
    image = read_image(image_name)
    return pytesseract.image_to_string(image, lang="tesseract")


def run_ocr_kraken(image_name):
    shell_script = 'kraken -i ' + image_name + ' /tmp/kraken_result binarize segment ocr -m kraken.mlmodel'
    subprocess.run([shell_script], shell=True)
    f = open("/tmp/kraken_result", "r")
    text = f.read()
    f.close()
    return text


def run_ocr_ocropus(image_name):
    image = read_image(image_name)
    return pytesseract.image_to_string(image, lang="vie")
