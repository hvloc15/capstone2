from django.conf.urls import url
from api.views import OCR, UploadImage

urlpatterns = [
    url(r'^tesseract|kraken|ocropus/',OCR.as_view(), name='ocr'),
    url(r'^upload/',UploadImage.as_view(), name='upload'),
]
