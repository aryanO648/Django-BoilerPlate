from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OwnerRelation,RenterRelation

class OwnerRelationApiView(APIView):
    def post(self,request):
        data = request.data
        owner_relation_obj = OwnerRelation(owner_name = data["owner_name"], owner_id = data["owner_id"])
        owner_relation_obj.save()
        message = "data inserted"
        status = 201
        response_data = {
            "message":message,
            "status":status,
            "method":"Post"
        }
        return Response(response_data)
    def get(self, request):
        all_objects_owner_obj_value = OwnerRelation.objects.all().values()
        response_data = {
            "message":"Entry fetched",
            "status":200,
            "method":"get",
            "data":all_objects_owner_obj_value
        }
        return Response(response_data)

class RenterRelationApiView(APIView):
    def post(self,request):
        data = request.data
        owner_relation = OwnerRelation.objects.get(owner_id=data["owner_relation"])
        renter_relation_obj = RenterRelation(renter_name = data["renter_name"], owner_relation = owner_relation, date_of_arrival = data["date_of_arrival"])
        renter_relation_obj.save()
        message = "data inserted"
        status = 201
        response_data = {
            "message":message,
            "status":status,
            "method":"Post"
        }
        return Response(response_data)
    def get(self, request):
        all_objects_renter_obj_value = RenterRelation.objects.all().values()
        response_data = {
            "message":"Entry fetched",
            "status":200,
            "method":"get",
            "data":all_objects_renter_obj_value

        }
        return Response(response_data)

    