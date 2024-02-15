from django.shortcuts import render
from .models import OwnerRegisterModel
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class OwnerRegisterApiView(APIView):
    def post(self,request):
        message =""
        status = 200
        data = request.data 
        if len(str(data["phone"])) != 10:
            message = "phone incorrect"
            status = 400
        if  "@" not in data["email"]:
            message = "email incorrect"
            status = 400
        else:
            owner_register_model_obj = OwnerRegisterModel(name = data["name"], email = data["email"], phone = data["phone"], password = data["password"])
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
        all_objects_owner_obj_value = OwnerRegisterModel.objects.all().values()
        # for obj in all_objects_owner_obj:
        #     print(obj.name)
        print("all objects == >>>", all_objects_owner_obj_value)
        response_data = {
            "message":"Entry fetched",
            "status":200,
            "method":"get",
            "data":all_objects_owner_obj_value

        }
        return Response(response_data)
    
    def put(self, request):
        data = request.data
        id = data["id"]
        object_needd_to_update = OwnerRegisterModel.objects.get(id = id)
        object_needd_to_update.name = data["name"]
        object_needd_to_update.email = data["email"]
        object_needd_to_update.phone = data["phone"]
        object_needd_to_update.password = data["password"]
        object_needd_to_update.save()

        return Response({
            "message": "data updated"
        })
    def patch(self, request):
        data = request.data
        id = data["id"]
        object_needd_to_update = OwnerRegisterModel.objects.get(id = id)
        if data["name"]:
            object_needd_to_update.name = data["name"]
        
        object_needd_to_update.save()

        return Response({
            "message": "data updated"
        })
    
    def delete(self, request):
        query_data = int(request.GET.get("id"))
        OwnerRegisterModel.objects.get(id = query_data).delete()
        return Response({
            "message": "data deleted"
        })





    
class GetOnwerById(APIView):
    def get(self,request):
        reqId= int(request.GET.get("id"))
        
        
        all_objects_owner_obj_value = OwnerRegisterModel.objects.filter(id =reqId).values()
        # for i in all_objects_owner_obj_value:
        #     #print(i)
        #     if i['id']==reqId:
        #         a=i
        response_data = {
            "message":"Entry fetched",
            "status":200,
            "method":"get",
            "data":all_objects_owner_obj_value

        }
        return Response(response_data)
    def put(self,request):
        data = request.data
        

    