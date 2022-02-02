from django.views import generic


from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PersonInfo, PersonExercise
from .models import Exercise
from rest_framework import generics
from .serializers import ValidData, ValidToken, PersonExerciseSerializer, ValidTokenAndDate

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test

from .serializers import PersonInfoSerializer


class Login(APIView):
    print('login')


    def post(self, request, format=None):

        print('request = ')
        print(request)
        print(request.data)
        valid = ValidData(data=request.data)

        if valid.is_valid():
            PersonInfos = PersonInfo.objects.filter(Username=valid.data['Username'],
                                                    Password=valid.data['Password']).select_related()
            serializer = PersonInfoSerializer(PersonInfos, many=True)
            if (serializer.data):
                return Response(serializer.data)
            else:
                return Response('Username Or PasswordIs wrong ', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(valid.errors, status=status.HTTP_400_BAD_REQUEST)


class Splahe(APIView):

    def post(self, request, format=None):

        valid = ValidToken(data=request.query_params)

        if valid.is_valid():
            PersonInfos = PersonInfo.objects.filter(ApiToken=valid.data['Token']).select_related()
            serializer = PersonInfoSerializer(PersonInfos, many=True)
            if (serializer.data):
                return Response(serializer.data)
            else:
                return Response('Token is Wrong ', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(valid.errors, status=status.HTTP_400_BAD_REQUEST)


class Exercise(APIView):

    def post(self, request, format=None):

        valid = ValidTokenAndDate(data=request.query_params)

        if valid.is_valid():
            PersonInfos = PersonInfo.objects.filter(ApiToken=valid.data['Token']).select_related()
            # serializer = PersonInfoSerializer(PersonInfos, many=True)


            print(PersonInfos[0].id)




            # return Response(1)

            if (PersonInfos[0].id):

                PersonExercise1 = PersonExercise.objects.filter(PersonInfo=PersonInfos[0].id,DateWeek__contains =valid.data['DateW'] ).select_related().order_by('ShomareHarkat')
                serializer2 = PersonExerciseSerializer(PersonExercise1, many=True)



                return Response(serializer2.data)



            else:
                return Response('Token is Wrong ', status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(valid.errors, status=status.HTTP_400_BAD_REQUEST)


class ApiListPersonInfo(APIView):
    def get(self, request, format=None):
        print(1111111111111)
        # return Response(request.query_params )

        id = request.query_params['id']

        # PersonInfos = PersonInfo.objects.all()
        PersonInfos = PersonInfo.objects.filter(id=id).select_related()
        serializer = PersonInfoSerializer(PersonInfos, many=True)

        # return 1
        return Response(serializer.data)

    def post(self, request, format=None):
        return Response(1)
        serializers = PersonInfoSerializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


from .serializers import ExerciseSerializer


#
# class ApiListExercise(APIView):
#     def get(self, request, format=None):
#         Exercises = Exercise.objects.all()
#         serializer = ExerciseSerializer(Exercises, many=True)
#         return Response(serializer.data)
#
#     def post(self,request,format=None):
#         serializers =ExerciseSerializer(data=request.data)
#         serializers.is_valid(raise_exception =True)
#         serializers.save()
#         return Response(serializers.data,status=status.HTTP_201_CREATED)
#
# class ApiListExercise(generics.ListCreateAPIView):
#     queryset = Exercise.objects.all()
#     serializer_class = ExerciseSerializer

#
# from .models import Book
# from .models import BookInstance
# from .models import Author
# from .models import Genre
# from .models import BookHome
#
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
#
# # Create your views here.
#
# @login_required()
# def index(request):
#     num_books = Book.objects.all()
#     context = {
#         'num_books': num_books
#     }
#     return render(request, 'book/index.html', context)
#
#
# class BookListView(generic.ListView):
#     model = Book
#
#
# class BookDetailView(LoginRequiredMixin,generic.DetailView):
#     model = Book
#
# #
# class BookHomeListView(generic.ListView):
#     model = BookHome
#
#
# class BookHomeDetailView(LoginRequiredMixin,generic.DetailView):
#     model = BookHome
#
#
