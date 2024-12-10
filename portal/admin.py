from django.contrib import admin
from .models import CustomUser, Unit, Session, Registration, Assignment, Submission

from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_student', 'is_teacher']
    list_filter = ['is_student', 'is_teacher']


admin.site.register(Unit)
admin.site.register(Session)
admin.site.register(Registration)
admin.site.register(Assignment)
admin.site.register(Submission)
