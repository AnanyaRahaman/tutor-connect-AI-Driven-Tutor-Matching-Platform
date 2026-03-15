from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(["POST"])
def register(request):

    username = request.data["username"]
    email = request.data["email"]
    password = request.data["password"]

    user = User.objects.create_user(

        username=username,
        email=email,
        password=password

    )

    return Response({"message":"user created"})