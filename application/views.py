from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import datetime

from .models import Animal, BreedOfAnimal, Client, ClientPet, Timetable


def index(request):
    return HttpResponse(" Всім привіт! Це пробна сторінка. ")


class MainView(TemplateView):
    template_name = 'index.html'


# class NewsView(TemplateView):
#     template_name = 'newssite.html'


class RecordingView(TemplateView):
    template_name = 'recording.html'


@login_required
def news(request):
    return render(request, 'newssite.html')


class DiscussionView(TemplateView):
    template_name = 'discussion.html'


class PollsView(TemplateView):
    template_name = 'polls.html'


def products(request, id):
    category = request.GET.get("cat", "")
    output = "<h2 style = 'color: red'>Product № {0} Category: {1}</h2>".format(id, category)
    return HttpResponse(output)


def fun(request, text="Clinick chaska"):
    change = text + ' ' + 'найкраща у світі'
    return render(request, 'index.html', {'change': change})


def color(request):
    dif = "style = background: red;"
    return render(request,'index.html',{'dif': dif})


class AnimalView(ListView):
    model = Animal
    template_name = "animal.html"

@csrf_exempt
def client(request):
    if request.method == "GET":
        # animals = Animal.objects.all()
        return render(request, 'recording.html')
    if request.method == "POST":
        ClientFirstName = request.POST["ClientFirstName"]
        ClientLastName = request.POST["ClientLastName"]
        ClientEmail = request.POST["ClientEmail"]
        ClientPhoneNumber = request.POST["ClientPhoneNumber"]
        AnimalKindOfAnimal = request.POST["AnimalKindOfAnimal"]
        BreedOfAnimalName = request.POST["BreedOfAnimalName"]
        ClientPetNickname = request.POST["ClientPetNickname"]
        ClientPetAge = request.POST["ClientPetAge"]
        ClientPetSex = request.POST["ClientPetSex"]
        TimetableDateOfAdmission = request.POST["TimetableDateOfAdmission"]
        try:
            kindOfAnimal = Animal.objects.get(kindOfAnimal=AnimalKindOfAnimal)
        except:
            kindOfAnimal = Animal(kindOfAnimal=AnimalKindOfAnimal)
            try:
                kindOfAnimal.full_clean()
                kindOfAnimal.save()
            except ValidationError as e:
                if "kindOfAnimal" in e.message_dict:
                    Validationserrors5 = e.message_dict["kindOfAnimal"]
                    err5 = "Є помилка у введені даних: " + str(Validationserrors5)
                    return render(request, 'recording.html',
                                  {'err5': err5, "ClientLastName": ClientLastName, "ClientFirstName": ClientFirstName,
                                   "BreedOfAnimalName": BreedOfAnimalName, "ClientEmail": ClientEmail,
                                   "ClientPhoneNumber": ClientPhoneNumber})
        try:
            name = BreedOfAnimal.objects.get(name=BreedOfAnimalName)
        except:
            name = BreedOfAnimal(name=BreedOfAnimalName, animal=kindOfAnimal)
            try:
                name.full_clean()
                name.save()
            except ValidationError as e:
                if "name" in e.message_dict:
                    Validationserrors6 = e.message_dict["name"]
                    err6 = "Є помилка у введені даних: " + str(Validationserrors6)
                    return render(request, 'recording.html', {'err6': err6, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientEmail": ClientEmail,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal})
        try:
            lastName = Client.objects.get(last_name=ClientLastName)
        except:
            lastName = Client(first_name=ClientFirstName, last_name=ClientLastName, email=ClientEmail,
                               phone_number=ClientPhoneNumber)
            try:
                lastName.full_clean()
                lastName.save()
            except ValidationError as e:
                if "last_name" in e.message_dict:
                    Validationserrors1 = e.message_dict["last_name"]
                    err1 = "Є помилка у введені даних: " + str(Validationserrors1)
                    return render(request, 'recording.html', {'err1': err1, "ClientFirstName": ClientFirstName,
                                                              "ClientEmail": ClientEmail,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
                elif "first_name" in e.message_dict:
                    Validationserrors2 = e.message_dict["first_name"]
                    err2 = "Є помилка у введені даних:" + str(Validationserrors2)
                    return render(request, 'recording.html', {'err2': err2, "ClientLastName": ClientLastName,
                                                              "ClientEmail": ClientEmail,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
                elif "email" in e.message_dict:
                    Validationserrors3 = e.message_dict["email"]
                    err3 = "Є помилка у введені даних: " + str(Validationserrors3)
                    return render(request, 'recording.html', {'err3': err3, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
                elif "phone_number" in e.message_dict:
                    Validationserrors4 = e.message_dict["phone_number"]
                    err4 = "Є помилка у введені даних: " + str(Validationserrors4)
                    return render(request, 'recording.html', {'err4': err4, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientEmail": ClientEmail,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
        try:
            dateofAdmission = Timetable.objects.get(dateofAdmission=TimetableDateOfAdmission)
        except:
            dateofAdmission = Timetable(dateofAdmission=TimetableDateOfAdmission, statusTimetable =False, client=lastName)
            try:
                dateofAdmission.full_clean()
                dateofAdmission.save()
            except ValidationError as e:
                if "dateofAdmission" in e.message_dict:
                    Validationserrors10 = e.message_dict["dateofAdmission"]
                    err10 = "Є помилка у введені даних: " + str(Validationserrors10)
                    return render(request, 'recording.html', {'err10': err10, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
        try:
            nickname = ClientPet.objects.get(nickname=ClientPetNickname)
        except:
            nickname = ClientPet(nickname=ClientPetNickname, age=ClientPetAge, sex=ClientPetSex, breedOfAnimal=name,
                                 client=lastName)
            try:
                nickname.full_clean()
                nickname.save()
            except ValidationError as e:
                if "nickname" in e.message_dict:
                    Validationserrors7 = e.message_dict["nickname"]
                    err7 = "Є помилка у введені даних: " + str(Validationserrors7)
                    return render(request, 'recording.html', {'err7': err7, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName})
                elif "age" in e.message_dict:
                    Validationserrors8 = e.message_dict["age"]
                    err8 = "Є помилка у введені даних: " + str(Validationserrors8)
                    return render(request, 'recording.html', {'err8': err8, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName,
                                                              "ClientPetNickname": ClientPetNickname})
                elif "sex" in e.message_dict:
                    Validationserrors9 = e.message_dict["sex"]
                    err9 = "Є помилка у введені даних: " + str(Validationserrors9)
                    return render(request, 'recording.html', {'err9': err9, "ClientLastName": ClientLastName,
                                                              "ClientFirstName": ClientFirstName,
                                                              "ClientPhoneNumber": ClientPhoneNumber,
                                                              "AnimalKindOfAnimal": AnimalKindOfAnimal,
                                                              "BreedOfAnimalName": BreedOfAnimalName,
                                                              "ClientPetNickname": ClientPetNickname, "ClientPetAge": ClientPetAge})
        clients = Client.objects.order_by('-id')
        return render(request, 'recording.html', {'clients': clients})


def clientToDict(objClient):
    if objClient == None:
        return None

    dictionary = {}
    dictionary["first_name"] = objClient.client.first_name
    dictionary["last_name"] = objClient.client.last_name
    return dictionary

def timeClient(request):
    currentDate = datetime.date.today()
    infoClient = Timetable.objects.filter(dateofAdmission=currentDate)
    clnJson = []
    for sp in infoClient:
       clnJson.append(clientToDict(sp))
    print(clnJson)
    return JsonResponse(clnJson, safe = False)














