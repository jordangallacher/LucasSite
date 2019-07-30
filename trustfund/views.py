from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def payment_done(request):
  return render(request, 'trustfund/done.html')


@csrf_exempt
def payment_cancelled(request):
  return render(request, 'trustfund/cancelled.html')



def payment_process(request):
    host = request.get_host()
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": "10.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url":  'http://{}{}'.format(host, reverse('payment')),  #'paypal-ipn'
        "return_url":  'http://{}{}'.format(host, reverse('done')),
        "cancel_return":  'http://{}{}'.format(host, reverse('cancelled')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "trustfund/payment.html", context)

