from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import serializers
from . import models
from . import forms


class MuscleGroupListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.MuscleGroups
    template_name = 'muscle_group_list.html'
    context_object_name = 'muscle_groups'
    paginate_by = 5
    permission_required = 'muscle_groups.view_musclegroups'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset


class MuscleGroupCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.MuscleGroups
    template_name = 'muscle_group_create.html'
    form_class = forms.MuscleGroupForm
    success_url = reverse_lazy('muscle_group_list')
    permission_required = 'muscle_groups.add_musclegroups'


class MuscleGroupDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.MuscleGroups
    template_name = 'muscle_group_delete.html'
    success_url = reverse_lazy('muscle_group_list')
    permission_required = 'muscle_groups.delete_musclegroups'


class MuscleGroupListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.MuscleGroups.objects.all()
    serializer_class = serializers.MuscleGroupSerializer


class MuscleGroupDestroyAPIView(generics.DestroyAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.MuscleGroups.objects.all()
    serializer_class = serializers.MuscleGroupSerializer
