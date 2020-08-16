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
    title = "Ramza | Full Stack Dev. "
    return render(request, 'index.html', {"title": title })

def about(request):
    title = " Ramza | About"
    return render(request, 'about.html', {"title": title})

def projects(request):
    title = 'Ramza | Projects'
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
    title = 'Photos | Ramza'
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
    