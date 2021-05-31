from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Allergy

# Create your views here.
def index(request):
	allergy_list = Allergy.objects.all()
	context = {
		'allergy_list': allergy_list
	}
	return render(request, 'alg/index.html', context)

def add_allergy(request):
	a = Allergy(name = request.POST['name'])
	a.save()
	return HttpResponseRedirect(reverse('alg:index'))

def detail(request, allergy_id):
	a = get_object_or_404(Allergy, id=allergy_id)
	return HttpResponse(str(a))

def enrage(request):
	a = get_object_or_404(Allergy, id=request.POST['id'])
	a.anger += 1
	a.save()
	return HttpResponseRedirect(reverse('alg:index'))