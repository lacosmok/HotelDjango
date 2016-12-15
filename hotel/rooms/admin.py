from django.contrib import admin
from django.contrib.auth.models import User, Group
from . import models


# Register your models here.
class HotelInline(admin.StackedInline):
    model = models.Hotel


class ProfileInline(admin.StackedInline):
    model = models.Profile
    max_num = 1
    can_delete = False


class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]


class HotelAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ('name', 'address', 'description')
    fieldsets = (
        ('Standard info', {
            'fields': ('name', 'description', 'photo')
        }),
        ('Contact info', {
            'fields': ('address',)
        }),
    )


class RoomAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description']
    list_display = ['name', 'hotel', 'description']


class AddressAdmin(admin.ModelAdmin):
    inlines = [HotelInline]
    list_display = ('street', 'nr', 'city')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
admin.site.register(models.Reservation)
admin.site.register(models.Telephone)
admin.site.register(models.Hotel, HotelAdmin)
admin.site.register(models.Profile)
admin.site.register(models.Room, RoomAdmin)
admin.site.register(models.Address)
