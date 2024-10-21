from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializers
# Create your views here.

class EmployeeList(APIView):
    def get(self,request):
        emps=Employee.objects.all()
        serializer=EmployeeSerializers(emps, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer=EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Added'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

class EmployeeDetails(APIView):
    def get(self,request,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"message":"Employee Does Not Exist:"},status=status.HTTP_400_BAD_REQUEST)
        
        serializer=EmployeeSerializers(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self,request,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"message":"Employee Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer=EmployeeSerializers(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Complete Employee Details Get Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

    def patch(self,request,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"message":"Employee Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        serializer=EmployeeSerializers(emp, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Employee Get Partially Updated"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self,request,id):
        try:
            emp=Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            return Response({"message":"Employee Does Not Exist"}, status=status.HTTP_400_BAD_REQUEST)
        emp.delete()
        return Response({"message":"Employee Deleted.."}, status=status.HTTP_204_NO_CONTENT)
    