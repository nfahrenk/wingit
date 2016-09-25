from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from seating.forms import PersonForm
from seating.models import Person
from django.contrib import messages
from LIKE_CHOICES import COUNTS
from seating_algorithm import findMatches

class IndexView(TemplateView):
    def get(self, request):
        forms = {
            str(person): PersonForm(instance=person, prefix=str(person))
            for person in Person.objects.all()
        }
        fbInfo = {
            person.pk: person.getIndustry() if person.prefersBusiness else [(COUNTS[like][1], like, COUNTS[like][0]) for like in person.likes]
            for person in Person.objects.all()
        }
        matches = [
            (Person.objects.get(pk=personA), Person.objects.get(pk=personB), reason)
            for personA, personB, reason in findMatches(fbInfo)
        ]
        return render(request, 'index.html', {"forms": forms, "matches": matches})

    def post(self, request):
        forms = [
            PersonForm(request.POST, instance=person, prefix=str(person))
            for person in Person.objects.all()
        ]
        stillTrue = True
        
        for form in forms:
            stillTrue = stillTrue and form.is_valid()
        
        if stillTrue:
            for form in forms:
                form.save(commit=True)
        else:
            for form in forms:
                if not form.is_valid():
                    for key, error in form.errors.items():
                        messages.error(key + " - " + error)
        
        return HttpResponseRedirect(reverse('index', args=[]))