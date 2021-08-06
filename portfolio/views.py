from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render
from .models import Project

# API Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ProjectAPI
from .serializer import ProjectAPISerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def index(request):
    title = "Ramsa | Full Stack Dev. "
    return render(request, 'index.html', {"title": title })

def about(request):
    title = " Ramsa | About"
    return render(request, 'about.html', {"title": title})

def projects(request):
    title = 'Ramsa | Projects'
    show_case = Project.objects.all()
    return render(request, 'projects.html', {"title": title, "show_case": show_case})


# HTTP Error 400
# def error_404(request):
#         data = {}
#         return render(request, 'fourOwfour.html', data)


# def error_500(request):
#         data = {}
#         return render(request, 'fourOwfour.html', data)

# end of error views

def photos(request):
    title = 'Photos | Ramsa'
    return render(request, 'photos2.html', {"title": title})


# API VIEWS
class ProjectList(APIView):
    def get (self, request, format=None):
        all_projects = ProjectAPI.objects.all()
        serializers = ProjectAPISerializer(all_projects, many=True)
        return Response(serializers.data)

    def post (self, request, format=None):
        serializers=ProjectAPISerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes= (IsAdminOrReadOnly,)


# Getting a single Item
    
class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_proj(self, pk):
        try:
            return ProjectAPI.objects.get(pk=pk)
        except ProjectAPI.DoesNotExist:
            return HTTP404
    
    def get(self, request, pk, format=None):
        proj = self.get_proj(pk)
        serializers = ProjectAPISerializer(proj)

        return Response(serializers.data)

# Updating an item

    def put(self, request, pk, format=None):
        proj = self.get_proj(pk)
        serializers = ProjectAPISerializer(proj, request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

# Deleting an item

    def delete(self, request, pk, format=None):
        proj = self.get_proj(pk)
        proj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

