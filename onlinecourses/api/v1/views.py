from rest_framework import generics, status, permissions, viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from accounts.serializers import ProfileSerializer, LoginSerializer, LogoutSerializer
from accounts.models import Profile
from courses.models import Course
from courses.serializers import CourseSerializer


class ProfileAPIView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


# class ProfileAPIView(
#     generics.UpdateAPIView, generics.ListAPIView,

# ):

#     parser_classes = (MultiPartParser,)
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()
    

#     #def get (self, request):


#     def update (self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return super().update(request, *args, **kwargs)
        # serializer = self.get_serializer(data=request.data, partial=True)
    #     # bio = request.data['bio']
    #     print (request.data)
    #     print (request.FILES)
    #     if serializer.is_valid(raise_exception=True):
    #         file = request.FILES['image']
    #         serializer.save(image=file)
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def get(self, request):
        user = request.user
        if not user or not user.id:
            return Response({'msg': 'You are not logged in'})
        return Response({'msg': f'You are already logged in as {user}'})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password) # (**request.data) Query dict?
        if not user:
            return Response({'error': 'wrong credentials'}, status=status.HTTP_400_BAD_REQUEST)

        if user.is_active:
            login(request, user)
            return Response({'msg': f'You are  logged in as {user}'}, status=200)

        return Response({'error': 'something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    serializer_class = LogoutSerializer

    # authentication_classes = (TokenAuthentication,)
    def get(self, request):

        user = request.user
        if not user or not user.id:
            return Response({'msg': 'you are not logged in'})
        return Response({'msg': f'you are logged in as {user}'})


    def post (self, request):
        #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
        logout(request)
        return Response('Logout successful', status=204)


class CoursesListView(APIView):

    #permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)