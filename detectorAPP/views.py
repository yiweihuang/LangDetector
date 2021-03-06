# Create your views here.
from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException, ParseError

from .serializers import DetectorAppSerializer
import detectorAPP.lang_model as model
from collections import defaultdict

class DetectorAppLang(views.APIView):
    def get(self, request, *args, **kwargs):
        AliveMessage = defaultdict(list)
        AliveMessage['lang'] = "Hello, I am get!"
        results = DetectorAppSerializer(AliveMessage).data
        return Response(results)

    def post(self, request, *args, **kwargs):
        if request.data.get('sentence'):
            sentence = request.data.get('sentence')

            try:
                LDDone = model.LangDetect(sentence)

            except Exception as e:
                raise APIException(e.args[0])
                pass
        else:
            raise ParseError()

        serializer = DetectorAppSerializer(data=LDDone)
        if serializer.is_valid():
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
