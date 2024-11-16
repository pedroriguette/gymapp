from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import serializers
from . import models
from . import forms


class ExerciceListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Exercice
    template_name = 'exercice_list.html'
    context_object_name = 'exercises'
    paginate_by = 20
    permission_required = 'exercises.view_exercice'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class ExerciceCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Exercice
    template_name = 'exercice_create.html'
    form_class = forms.ExerciceForm
    success_url = reverse_lazy('exercice_list')
    permission_required = 'exercises.add_exercice'


class ExerciceDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Exercice
    template_name = 'exercice_detail.html'
    permission_required = 'exercises.view_exercice'


class ExerciceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Exercice
    template_name = 'exercice_update.html'
    form_class = forms.ExerciceForm
    success_url = reverse_lazy('exercice_list')
    permission_required = 'exercises.change_exercice'


class ExerciceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Exercice
    template_name = 'exercice_delete.html'
    success_url = reverse_lazy('exercice_list')
    permission_required = 'exercises.delete_exercice'


class ExerciceListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Exercice.objects.all()
    serializer_class = serializers.ExerciceSerializer


class ExerciceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Exercice.objects.all()
    serializer_class = serializers.ExerciceSerializer
