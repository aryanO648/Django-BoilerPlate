from django.shortcuts import render
from .models import RegisterModel
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import renterSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
class RegisterApiView(APIView):
    def post(self,request):
        message =""
        status = 200
        data = request.data 
        if len(str(data["phone"])) != 10:
            message = "phone incorrect"
            status = 400
        else:
            owner_register_model_obj = RegisterModel(name = data["name"], phone = data["phone"], password = data["password"], room = data["room"], price = data["price"])
            owner_register_model_obj.save()
            message = "data inserted"
            status = 201


        print(data)
        response_data = {
            "message":message,
            "status":status,
            "method":"Post"
        }

        return Response(response_data)
    
    def get(self, request):
        response_data = {
            "message":"Entry fetched",
            "status":200,
            "method":"get"

        }
def info(request):
    s = RegisterModel.objects.get(id = 1)
    se = renterSerializer(s)
    json_data = JSONRenderer().render(se.data)
    return Response(json_data, content_type='application/json')


