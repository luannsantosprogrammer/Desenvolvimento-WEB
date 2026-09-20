from rest_framework import generics, permissions
from .models import Task
from .serializers import TaskSerializers



class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]    

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializers
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)