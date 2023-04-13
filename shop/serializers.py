from rest_framework import serializers
from .models import Food, Customer, Order,Person, PhoneNumber, Email,Student,PostalAddress


class FoodSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Food
        fields = ['name', 'price']
        

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ['firstname', 'lastname', 'phone_number']
        
class OrderSerializer(serializers.ModelSerializer):
    food = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    
    class Meta: 
        model = Order
        fields = ['food', 'customer']
    
    def get_food(self, obj):
        return obj.food.name
    
    def get_customer(self, obj):
        return obj.customer.__str__()
        




class PersonSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Person
        fields = ('name', 'last_name', 'national_code', 'father_name', 'role', 'password_hash')
        

