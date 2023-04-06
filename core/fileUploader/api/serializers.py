from rest_framework.serializers import Serializer, FileField



class UploadFileSerializer(Serializer):
    file_uploaded = FileField(max_length=None, allow_empty_file=False )

    class Meta:
        fields = ['file_uploaded']