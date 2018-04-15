from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# import requests
from django import forms
# Create your views here
from .models import Culture
from kits.models import Kits
from .forms import AddForm
from django.shortcuts import render, redirect


# Create your views here.


@login_required(login_url='/account/login/')
def index(request):
    username = request.user.username
    cultures_qs = Culture.objects.filter(username=username)
    context = {'cultures': cultures_qs}
    return render(request, 'userprofile/track.html', context)


@login_required(login_url='/account/login/')
def new_culture(request):
    if request.method == 'POST':

        form = AddForm(request.POST)

        if form.is_valid():
            username = request.user.username
            name = request.POST.get('name', '')
            volume = request.POST.get('volume', '')
            reg_number = request.POST.get('reg_number', '')
            culture_qs = Culture.objects.filter(username=username, name=name)

            kits_qs = Kits.objects.filter(reg_number=reg_number)

            if kits_qs.exists():
                if kits_qs[0].is_registered == 1 :
                    errors = "This kit has already been registered"
                    form = AddForm()
                    context = {'form': form, 'errors': errors}
                    return render(request, 'userprofile/new.html', context)
                else:
                    culture_obj = Culture(username=username, name=name, volume=volume, reg_number=reg_number)
                    k = Kits.objects.get(reg_number=reg_number)

                    k.is_registered = 1
                    k.save()
                    culture_obj.save()
                    return redirect('profile:index')
            else:
                errors = "Wrong Registration number"
                form = AddForm()
                context = {'form': form, 'errors': errors}
                return render(request, 'userprofile/new.html', context)







    else:
        form = AddForm()

    context = {'form': form}

    return render(request, 'userprofile/new.html', context)


@login_required(login_url='/account/login/')
def delete_culture(request, id):
    Culture.objects.filter(id=id).delete()
    return redirect('profile:index')


@login_required(login_url='/account/login/')
def testc(request, id):
    culture = Culture.objects.filter(id=id)
    context = {'culture': culture}
    return render(request, 'userprofile/testculture.html', context)


@login_required(login_url='/account/login/')
def imagetest(request, id):
    culture = Culture.objects.filter(id=id)
    context = {'culture': culture}
    return render(request, 'userprofile/imagetest.html', context)


@login_required(login_url='/account/login/')
def result(request, id):
    culture = Culture.objects.filter(id=id)
    context = {'culture': culture}
    return render(request, 'userprofile/result.html', context)
