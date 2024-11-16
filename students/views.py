from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import serializers
from . import models
from . import forms


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Student
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 3
    permission_required = 'students.view_student'

    def get_queryset(self):
        queryset = super().get_queryset()
        full_name = self.request.GET.get('full_name')
        active = self.request.GET.get('active')

        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)

        if active is not None:
            if active.lower() == 'true':
                queryset = queryset.filter(active=True)

            elif active.lower() == 'false':
                queryset = queryset.filter(active=False)

        return queryset


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Student
    template_name = 'student_create.html'
    form_class = forms.StudentForm
    success_url = reverse_lazy('student_list')
    permission_required = 'students.add_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Student
    template_name = 'student_detail.html'
    permission_required = 'students.view_student'


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Student
    template_name = 'student_update.html'
    form_class = forms.StudentForm
    success_url = reverse_lazy('student_list')
    permission_required = 'students.change_student'


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Student
    template_name = 'student_delete.html'
    success_url = reverse_lazy('student_list')
    permission_required = 'students.delete_student'


class StudentListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
