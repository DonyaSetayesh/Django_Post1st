from django.urls import path
from .apis import Food, Order,Person


app_name = 'shop'
urlpatterns = [

    path('api/v1/items/<int:id>', Food.as_view(), name= "get_food_singelton"),
    path('api/v1/items', Food.as_view(), name= "new_food"),
    path('api/v1/orders/', Order.get_order_collection, name= "get_order_collection"),
    path('api/v1/persons/', Person.as_view(), name= "post_person_information"),
]
