from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TuitionRequest
from .serializers import TuitionSerializer


@api_view(["GET"])
def tutor_requests(request):

    requests = TuitionRequest.objects.all()

    serializer = TuitionSerializer(requests,many=True)

    return Response(serializer.data)