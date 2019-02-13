from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from api.serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from algorithms.utils import read_opencv_image
from api.renderer import ApiJSONRenderer
from algorithms.ocr_algorithms import run_ocr_tesseract, run_ocr_kraken, run_ocr_ocropus


class OCR(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (ApiJSONRenderer,)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file_serializer.save()

        function_name = request.path.split('/')[2]

        func = getattr(self, function_name)
        text = func(image_name=file_serializer.data)

        return Response({"message":text}, status=status.HTTP_200_OK)

    def tesseract(self, image_path):
        return run_ocr_tesseract(image_path)

    def kraken(self, image_path):
        return run_ocr_kraken(image_path)

    def ocropus(self, image_path):
        return run_ocr_ocropus(image_path)

    def get(self, request):
        return Response({"message":"OK"}, status=status.HTTP_200_OK)


class UploadImage(APIView):
    parser_classes = (MultiPartParser, FormParser)
    renderer_classes = (ApiJSONRenderer,)

    def post(self, request):
        file_serializer = ImageSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)
        file_serializer.save()
        return Response({"message":file_serializer.data}, status=status.HTTP_200_OK)

    def get(self, request):
        return Response({"message": "OK"}, status=status.HTTP_200_OK)
