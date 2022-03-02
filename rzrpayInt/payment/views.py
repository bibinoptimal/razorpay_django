from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views import View
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
# Create your views here.


class Payment(View):
    def get(self, request):

        currency = 'INR'
        amount = 29900  # Rs. 29900

        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                           currency=currency,
                                                           payment_capture='0'))

        # order id of newly created order.
        razorpay_order_id = razorpay_order['id']
        callback_url = 'paymenthandler/'

        # we need to pass these details to frontend.
        context = {}
        context['razorpay_order_id'] = razorpay_order_id
        context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
        context['razorpay_amount'] = amount
        context['currency'] = currency
        context['callback_url'] = callback_url
        return render(request, 'payment.html', context={'data': context})

    def post(self, request):
        if request.method == 'POST':
            data = {}
            data['first_name'] = request.POST['first_name']
            data['last_name'] = request.POST['last_name']
            data['payment_status'] = request.POST['payment_status']

            print(data)
        return JsonResponse({'response': data})
