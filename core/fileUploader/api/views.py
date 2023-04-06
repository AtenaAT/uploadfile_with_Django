from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadFileSerializer
# --------------------------------------------------


class UploadViewSet(ViewSet):

    serializer_class = UploadFileSerializer

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        content_type = file_uploaded.content_type
        response = "you have uploaded a {} file".format(content_type)
        return Response(response)