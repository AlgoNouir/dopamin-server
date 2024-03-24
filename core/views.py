from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from models.main.category import CategoryModel
from models.main.item import ItemModel



class CategorySerializer(serializers.ModelSerializer):
    
    name = serializers.CharField()
    
    class Meta:
        model = CategoryModel
        fields = "__all__"

class ItemModelSerializer(serializers.ModelSerializer):

    name = serializers.CharField()
    price = serializers.IntegerField()
    desc = serializers.CharField()
    category_id = serializers.IntegerField()
    
    class Meta:
        model = ItemModel
        fields = "__all__"


class MainData(APIView):
    
    def get(self, request):
        
        data = ItemModel.objects.all()
        data = ItemModelSerializer(data, many=True).data
        
        category = CategoryModel.objects.all()
        category = CategorySerializer(category, many=True).data
        
        response = {
            "data": data,
            "category": category,
        }
        
        return Response(response, status=status.HTTP_200_OK)