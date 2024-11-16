from rest_framework import generics
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from app.permissions import GlobalDefaultPermissions
from . import models
from . import forms
from . import serializers


class CoachListView(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.Coach
    template_name = 'coach_list.html'
    context_object_name = 'coaches'
    paginate_by = 20
    permission_required = 'coaches.view_coach'

    def get_queryset(self):
        queryset = super().get_queryset()
        full_name = self.request.GET.get('full_name')

        if full_name:
            queryset = queryset.filter(full_name__icontains=full_name)

        return queryset


class CoachCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.Coach
    template_name = 'coach_create.html'
    form_class = forms.CoachForm
    success_url = reverse_lazy('coach_list')
    permission_required = 'coaches.add_coach'


class CoachDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = models.Coach
    template_name = 'coach_detail.html'
    permission_required = 'coaches.view_coach'


class CoachUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.Coach
    template_name = 'coach_update.html'
    form_class = forms.CoachForm
    success_url = reverse_lazy('coach_list')
    permission_required = 'coaches.change_coach'


class CoachDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.Coach
    template_name = 'coach_delete.html'
    success_url = reverse_lazy('coach_list')
    permission_required = 'coaches.delete_coach'


class CoachListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Coach.objects.all()
    serializer_class = serializers.CoachSerializer


class CoachRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.Coach.objects.all()
    serializer_class = serializers.CoachSerializer
