from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from sewaService.models import Services
from .forms import ServiceForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


def index(request):
    services = Services.objects.all()
    context = {'services': services}
    return render(request, 'sewaService\home.html', context)

# def addService(request):
#     if request.method == "POST":
#         form = ServiceForm(request.post)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'New service {{ title }} has been added successfully.')
#             return redirect('sewa-home')
#     else:
#         form = ServiceForm()

#     context = { 'form': form}

#     return render(request, 'sewaService/service_form.html', context)

class ServiceCreateView(CreateView):
    model = Services
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)

class ServiceListView(ListView):
    model = Services
    template_name = 'sewaService/home.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Services

class ServiceUpdateView(UpdateView):
    model = Services
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):   
        return super().form_valid(form)

class ServiceDeleteView(DeleteView):
    model = Services
    success_url = '/'
