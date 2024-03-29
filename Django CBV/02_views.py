import json

from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView

from .models import Unit


class Index(TemplateView):
    template_name = "products/index.html"


class UnitList(ListView):
    queryset = Unit.objects.filter(is_deleted=False)


class UnitDetail(DetailView):
    model = Unit


class UnitForm(CreateView):
    model = Unit
    fields = ["name", "code", "description"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "New Unit"
        return context


class UnitUpdate(UpdateView):
    model = Unit
    fields = ["name", "code", "description"]
    template_name_suffix = "_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Unit -"
        return context


class UnitDelete(DeleteView):
    model = Unit
    template_name = "products/confirm_delete.html"
    success_url = reverse_lazy("products:unit_list")
