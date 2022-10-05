from copy import deepcopy

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Coin
from .serializer import CoinSerializer


class CoinApiView(APIView):
    def get(self, request):
        coins = Coin.objects.all()
        serializer = CoinSerializer(coins, many=True)
        resp = {
            'data': serializer.data
        }
        return Response(resp)

    def post(self, request):
        try:
            coin_objs = [Coin(**data) for data in request.data]
            bulk_update_or_create = Coin.objects.bulk_update_or_create(coin_objs, ['name', '_1h', '_24h', '_7d',
                                                                                   'market_cap', 'volume24h', 'supply',
                                                                                   'price', 'code', 'img'],
                                                                       match_field='id')

            return Response({'msg':'Data Successfully Updated'})
        except Exception as e:
            return Response({'error': str(e)})
