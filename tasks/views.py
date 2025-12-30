from rest_framework.viewsets import ModelViewSet
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h2>Task Management API</h2>
        <ul>
            <li><a href='/api/tasks/'>API</a></li>
            <li><a href='/dashboard/'>Dashboard</a></li>
            <li><a href='/admin/'>Admin</a></li>
        </ul>
    """)


class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


def dashboard(request):
    total = Task.objects.count()
    completed = Task.objects.filter(status='completed').count()
    pending = Task.objects.filter(status='pending').count()

    return render(request, "dashboard.html", {
        "total": total,
        "completed": completed,
        "pending": pending
    })
