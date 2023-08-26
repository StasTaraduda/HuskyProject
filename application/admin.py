from django.contrib import admin
from .models import Animal, BreedOfAnimal,Client, ClientPet, Timetable
# Register your models here.


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('kindOfAnimal', 'id')
    list_filter = ('kindOfAnimal',)
    search_fields = ('kindOfAnimal',)


class BreedOfAnimalAdmin(admin.ModelAdmin):
    def kindOfAnimal(obj):
        return obj.animal.kindOfAnimal
    list_display = ('name', kindOfAnimal)
    list_filter = ('name',)
    search_fields = (kindOfAnimal, 'name')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')
    list_filter = ('first_name', 'last_name')
    list_editable = ('email', 'phone_number')
    list_display_links = None
    search_fields = ('first_name', 'last_name')


class ClientPetAdmin(admin.ModelAdmin):
    def name(obj):
        return obj.breedOfAnimal.name
    list_display = ('nickname', 'age', 'sex', 'client', name)
    list_filter = ('nickname', 'age', 'sex')
    search_fields = ('nickname',)


class TimetableAdmin(admin.ModelAdmin):
    list_display = ('dateofAdmission', 'statusTimetable', 'client')
    list_filter = ('dateofAdmission', 'statusTimetable')
    search_fields = ('dateofAdmission',)


admin.site.register(Animal, AnimalAdmin)
admin.site.register(BreedOfAnimal, BreedOfAnimalAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ClientPet, ClientPetAdmin)
admin.site.register(Timetable, TimetableAdmin)

