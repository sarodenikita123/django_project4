from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Registration
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form save successfully!!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = Registration.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def updated_view(request, pk):
    template_name = "curd_app/create.html"
    obj = Registration.objects.get(id=pk)
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = Registration.objects.get(id=pk)
    form = RegistrationForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)



