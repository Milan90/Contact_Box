from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from contact_box.models import *


class AddPerson(View):

    def get(self, request):
        return render(request, "contact_box/addPerson.html")

    def post(self, request):
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        description = request.POST.get("description")

        new_person = Person.objects.create(name=name, surname=surname, description=description)
        id = new_person.id
        return redirect("/show/%s" % id)


class EditPerson(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        phones = person.phone_set.all()
        emails = person.email_set.all()
        ctxt = {
            'person': person,
            'phones': phones,
            'emails': emails,
        }
        return render(request, "contact_box/editPerson.html", ctxt)

    def post(self, request, id):
        person = Person.objects.get(pk=id)
        person.name = request.POST.get("name")
        person.surname = request.POST.get("surname")
        person.description = request.POST.get("description")
        person.save()
        return redirect("/")


class DeletePerson(View):
    def get(self, request, id):
        ctxt = {'person': Person.objects.get(pk=id)}
        return render(request, "contact_box/deletePerson.html", ctxt)

    def post(self, request, id):
        if request.POST.get("decision") == "yes":
            person = Person.objects.get(pk=id)
            person.delete()
            return redirect("/")
        else:
            return redirect("/")


class ShowPerson(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        ctxt = {
            'person': person
        }
        return render(request, "contact_box/showPerson.html", ctxt)


class ShowPersonList(View):
    def get(self, request):
        persons = Person.objects.all().order_by("name")
        ctxt = {
            'persons': persons
        }
        return render(request, "contact_box/showPersonList.html", ctxt)


class addAddress(View):
    def get(self, request, id):
        person = Person.objects.get(pk=id)
        address_id = person.address.id
        address = Address.objects.get(pk=address_id)
        address.person_set.remove(person)
        address.save()
        return redirect("/modify/%s" % person.id)

    def post(self, request, id):
        city = request.POST.get("city")
        street = request.POST.get("street")
        building_number = request.POST.get("building_number")
        flat_number = request.POST.get("flat_number")
        if Address.objects.filter(city=city, street=street, building_number=building_number,
                                  flat_number=flat_number).exists():
            new_address = Address.objects.get(city=city, street=street, building_number=building_number,
                                              flat_number=flat_number)
            person = Person.objects.get(pk=id)
            person.address = new_address
            person.save()
            return redirect("/show/%s" % id)
        else:
            new_address = Address.objects.create(city=city, street=street, building_number=building_number,
                                                 flat_number=flat_number)
            person = Person.objects.get(pk=id)
            person.address = new_address
            person.save()
        return redirect("/show/%s" % id)


class DelPhone(View):
    def get(self, request, id):
        phone = Phone.objects.get(pk=id)
        phone.delete()
        return redirect("/modify/%s" % phone.person.id)


class AddPhone(View):
    def post(self, request, id):
        phone_number = request.POST.get("phone_number")
        phone_type = request.POST.get("type")
        person = Person.objects.get(pk=id)
        Phone.objects.create(phone_number=phone_number, type=phone_type, person=person)
        return redirect("/modify/%s" % id)
