from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'AboutUs.html')


def impact(request):
    return render(request, 'OurImpact.html')


def contact(request):
    message = ''
    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            comments = request.POST.get('comments', '')
            # culture_qs = Culture.objects.filter(username=username, name=name)

            contact_obj = Contact(name=name, email=email, phone=phone, comments=comments)

            contact_obj.save()
            message = 'SUCCESFULLY POSTED'
            context = {'form': form, 'message': message}
        return render(request, "ContactUs.html", context)

    else:
        form = ContactForm()

    context = {'form': form}

    return render(request, 'ContactUs.html', context)


# def login(request):
# 	return render(request,'Login.html')
#
# def register(request):
# 	return render(request,'Register.html')

def team(request):
    return render(request, 'team.html')
