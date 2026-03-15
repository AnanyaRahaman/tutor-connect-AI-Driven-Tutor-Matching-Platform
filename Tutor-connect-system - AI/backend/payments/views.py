import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"


@api_view(["POST"])
def create_checkout_session(request):

    session = stripe.checkout.Session.create(

        payment_method_types=["card"],

        line_items=[{

            "price_data":{

                "currency":"usd",

                "product_data":{

                    "name":"Tutoring Session"

                },

                "unit_amount":5000

            },

            "quantity":1

        }],

        mode="payment",

        success_url="http://localhost:3000/success",

        cancel_url="http://localhost:3000/cancel"

    )

    return Response({"id":session.id})