from django.contrib import admin
from . models import User, Gallery


class UserAdmin(admin.ModelAdmin):
          list_display = ('name', 'age')


class GalleryAdmin(admin.ModelAdmin):
        list_display = ('title',)


admin.site.register(User, UserAdmin)
admin.site.register(Gallery, GalleryAdmin)
