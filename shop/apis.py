from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Food as food_model
from .models import Order as order_model
from .serializers import FoodSerializer,OrderSerializer
from .serializers import PersonSerializer


class Food(APIView):
    def get(self, request, id):
        foodqs = food_model.objects.get(id= id)
        serialized = FoodSerializer(foodqs)
        return Response(serialized.data, status.HTTP_200_OK)
        
    
    def post(self, request):
        data = request.data
        if data: 
            serialized = FoodSerializer(data=data)
            if serialized.is_valid():
                return Response(serialized.data, status.HTTP_201_CREATED)
            return Response({"erorr":"data is invalid"}, status.HTTP_400_BAD_REQUEST )
        return Response({"erorr":"empty payload"},status.HTTP_400_BAD_REQUEST )
        
class Order(APIView):
    @api_view(['GET'])
    def get_order_collection(request):
        qs = order_model.objects.all()
        serialized = OrderSerializer(instance=qs, many=True)
        return Response(serialized.data, status.HTTP_200_OK)
 
class Person(APIView):    
    def post(self, request):
        data = request.data
        if data: 
            serialized = PersonSerializer(data=data)
            if serialized.is_valid():
                serialized.save()
                return Response(serialized.data, status.HTTP_201_CREATED)
            return Response({"erorr":"data is unvalid",'details':serialized.errors}, status.HTTP_400_BAD_REQUEST )
        return Response({"erorr":"empty payload"},status.HTTP_400_BAD_REQUEST )
              