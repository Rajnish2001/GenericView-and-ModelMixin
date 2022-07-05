from .models import Student
from .serializers import StudentSerializer
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.generics import GenericAPIView

class LCStudent(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self,request,*args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)


class RUStudent(RetrieveModelMixin,UpdateModelMixin,GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

   


# class StudentList(ListModelMixin,GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self,request,*args, **kwargs):
#         return self.list(request, *args, **kwargs)


# class StudentCreate(CreateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class StudentRetrieve(RetrieveModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class StudentUpdate(UpdateModelMixin, GenericAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

class StudentDestroy(DestroyModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    