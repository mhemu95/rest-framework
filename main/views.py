from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# generic view
from rest_framework import generics

from django.contrib.auth.models import User

from . models import Student, Category, Book
from . serializers import StudentSerializer, CategorySerializer, BookSerializer, UserSerializer

# imported for token authentication
from rest_framework.authentication import TokenAuthentication

from rest_framework.permissions import IsAuthenticated

# imported for token authentication
from rest_framework.authtoken.models import Token
# imported for jwt authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


class UserView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username=serializer.data['username'])
            # token authentication
            token, _ = Token.objects.get_or_create(user=user)
            # jwt token refresh manually
            refresh = RefreshToken.for_user(user)

            return Response({'status': 'Success', 'refresh': str(refresh), 'access': str(refresh.access_token), 'message': 'User created successfully'})

        else:
            return Response({'status': 'failed', 'message': 'something went wrong'})


# rest framework generic view
class StudentGenericView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


'''
# class based view
class StudentView(APIView):
    
    # for token authentication
    # authentication_classes = [TokenAuthentication]

    # for jwt authentication
    authentication_classes = [JWTAuthentication]
    # permission or for authorization
    permission_classes = [IsAuthenticated]               

    def get(self, request):
        students = Student.objects.all()        
        serializer = StudentSerializer(students, many=True)

        return Response({'status': 'success', 'payload': serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'payload': serializer.data, 'message': 'data inserted successfully'})
        else:
            return Response({'status': 'failed', 'message': 'Something went wrong', 'error': serializer.errors})

    def patch(self, request):
        student = Student.objects.get(id=request.data['id'])
        serializer = StudentSerializer(student, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response({'status': 'success', 'payload': serializer.data, 'message': 'data updated successfully'})

        else:
            return Response({'status': 403, 'message': 'something went wrong, failed to update data'})

    def delete(self, request):
        id = request.GET.get('id')
        serializer = Student.objects.get(id=id)
        serializer.delete()

        return Response({'status': 'success', 'message': 'data deleted successfully'})
'''

'''
# function based view
# data list
@api_view(['GET'])
def home(request):
    student_obj = Student.objects.all()
    serializer = StudentSerializer(student_obj, many=True)

    return Response({'status': 200, 'payload': serializer.data})

# create data
@api_view(['POST'])
def post_data(request):
    serializer = StudentSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'data': serializer.data, 'message': 'Data inserted successfully'})

    else:
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong!!!'})

# read data
@api_view(['GET'])
def read_data(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student, many=False)

    return Response({'status': 200, 'data': serializer.data})

# update data
@api_view(['POST'])
def update_data(request,pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(instance=student, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'status': 200, 'data': serializer.data, 'message': 'Data updated successfully'})

    else:
        return Response({'status': 403, 'errors': serializer.errors, 'message': 'something went wrong!!!'})

# delete data
@api_view(['DELETE'])
def delete_data(request,pk):
    student = Student.objects.get(id=pk)
    student.delete()

    return Response({'status': 200, 'message': 'Data deleted successfully'})


# book list view
@api_view(['GET'])
def book_list(request):
    books_obj = Book.objects.all()
    serializer = BookSerializer(books_obj, many=True)
    
    return Response({'status': 200, 'data': serializer.data})


# fix the problem 
# @api_view(['POST'])
# def book_post(request):
#     book_serializer = BookSerializer(data = request.data)

#     if book_serializer.is_valid():
#         book_serializer.save()
#         return Response({'status': 200, 'data': 'book posted successfully'})
#     else:
#         return Response({'status': 403, 'data': 'could not post the book'})
'''
