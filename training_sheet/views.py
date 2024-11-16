from rest_framework import generics
from app.permissions import GlobalDefaultPermissions
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import serializers
from . import models
from . import forms


class TrainingSheetListview(LoginRequiredMixin, PermissionRequiredMixin, generic.ListView):
    model = models.TrainingSheet
    template_name = 'training_sheet_list.html'
    context_object_name = 'training_sheets'
    paginate_by = 20
    permission_required = 'training_sheet.view_trainingsheet'

    def get_queryset(self):
        queryset = super().get_queryset().filter()
        user = self.request.user
        student = self.request.GET.get('student')

        if not user.is_staff:
            queryset = queryset.filter(student__user=user)

        if student:
            queryset = queryset.filter(student__full_name__icontains=student)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = models.Group.objects.all()
        return context


class TrainingSheetCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    model = models.TrainingSheet
    template_name = 'training_sheet_create.html'
    form_class = forms.TrainingSheetForm
    success_url = reverse_lazy('training_sheet_list')
    permission_required = 'training_sheet.add_training_sheet'


class TrainingSheetUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    model = models.TrainingSheet
    template_name = 'training_sheet_update.html'
    form_class = forms.TrainingSheetForm
    success_url = reverse_lazy('training_sheet_list')
    permission_required = 'training_sheet.change_training_sheet'


class TrainingSheetDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    model = models.TrainingSheet
    template_name = 'training_sheet_delete.html'
    success_url = reverse_lazy('training_sheet_list')
    permission_required = 'training_sheet.delete_training_sheet'


class TrainingSheetListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.TrainingSheet.objects.all()
    serializer_class = serializers.TrainingSheetSerializer


class TrainingSheetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (GlobalDefaultPermissions,)
    queryset = models.TrainingSheet.objects.all()
    serializer_class = serializers.TrainingSheetSerializer
