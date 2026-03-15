from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Message


@api_view(["POST"])
def send_message(request):

    Message.objects.create(

        sender_id=request.data["sender"],
        receiver_id=request.data["receiver"],
        text=request.data["text"]

    )

    return Response({"status":"sent"})