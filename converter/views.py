import logging

import requests
from django.http import JsonResponse
from rest_framework.decorators import (api_view, permission_classes,
                                       throttle_classes)
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle


@api_view(['GET', 'POST'])
@throttle_classes([UserRateThrottle])
@permission_classes((IsAuthenticated, ))
def converter(request):
    converted_amount = None
    try:
        data = {
            "from": request.GET.get('from'),
            "to": request.GET.get('to'),
            "amount": request.GET.get('amount')
        }
        params = {
            'currency': data['from'],
        }
        res = requests.get(
            'https://api.coinbase.com/v2/exchange-rates', params=params, stream=True)
        to = data['to']
        rate = (res.json()['data']['rates'][to])
        converted_amount = (float(data['amount'])*float(rate))
        return JsonResponse({"converted_amount:": converted_amount})
    except Exception as e:
        logging.info(e)
    return JsonResponse({"converted_amount:": converted_amount})
