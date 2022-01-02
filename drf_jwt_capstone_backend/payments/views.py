from django.conf import settings
from rest_framework.response import Response
import stripe
from drf_jwt_capstone_backend.local_settings import *
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import redirect

stripe.api_key = STRIPE_SECRET_KEY

class StripeCheckoutView(APIView):
    def post(self, request):

        customAmount = request.data["unit_amount"]

        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        'price_data': {
                            'currency': 'usd',
                            'product_data': {
                                'name': 'Your Order',
                            },
                            "unit_amount": customAmount,
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url= settings.SITE_URL + '/?success=true&session_id={CHECKOUT_SESSION_ID}',
                cancel_url= settings.SITE_URL + '/?canceled=true',
            )
            return redirect(checkout_session.url)
        
        except:
            return Response(
                {'error': 'Something went wrong when creating stripe checkout session'},
                status = status.HTTP_500_INTERNAL_SERVER_ERROR
            )

       
