from django.shortcuts import render
from django.views import View
from .models import Home,About,Skills,Qualification,Sevices 

# Create your views here.
#def index(request):
#    homes = Home.objects.all()
#    return render(request, 'index.html', {'homes': homes})

class index(View):
    def get(self, request):
        homes = Home.objects.all()
        abouts = About.objects.all()
        skillss = Skills.objects.all()
        qualifications = Qualification.objects.all()
        return render(request, 'index.html',
        {'homes': homes, 'abouts': abouts, 'skillss': skillss, 'qualifications': qualifications})
    












