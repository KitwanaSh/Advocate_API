import queue
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q

from .models import Advocates

from .serializers import AdvocateSerializer

@api_view(["GET", "POST"])
def advocate_list(request):
    # Handle the GET request
    if request.method == "GET":
        query = request.GET.get("query")
        if query == None:
            query = ""
        
        # advocates = Advocates.objects.all()
        # User filter method in the query url
        advocates = Advocates.objects.filter(Q(username__icontains=query), Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)

        return Response(serializer.data)
    
    # Handle the POST request
    if request.method == "POST":
        advocate = Advocates.objects.create(
            username = request.data["username"],
            bio = request.data["bio"]
        )

        advocate.save()

        serializer = AdvocateSerializer(advocate, many=False)

        return Response(serializer.data)