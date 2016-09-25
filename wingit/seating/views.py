from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from seating.forms import PersonForm
from seating.models import Person
from django.contrib import messages

class IndexView(TemplateView):
    def get(self, request):
        forms = {
            str(person): PersonForm(instance=person, prefix=str(person))
            for person in Person.objects.all()
        }
        people = Person.objects.all()
        matches = [
            (people[2*i], people[2*i+1], "band%d" % i)
            for i in range(0, len(people)/2)
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