from django.contrib import admin
from .models import *
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.db import IntegrityError

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_student', 'is_teacher']
    list_filter = ['is_student', 'is_teacher']

    # Override delete_queryset to handle related objects
    def delete_queryset(self, request, queryset):
        for user in queryset:
            # Check for related records
            if user.is_student:
                if Registration.objects.filter(student=user).exists() or Submission.objects.filter(student=user).exists():
                    raise ValidationError(
                        f"Cannot delete student {user.username} as they have related registrations or submissions."
                    )
            elif user.is_teacher:
                if Unit.objects.filter(teacher=user).exists():
                    raise ValidationError(
                        f"Cannot delete teacher {user.username} as they are assigned to units."
                    )
        
        # Proceed with deletion
        super().delete_queryset(request, queryset)

    # Optional: Add warning messages in the admin UI (Django >= 3.0)
    def has_delete_permission(self, request, obj=None):
        # Restrict deletion based on custom logic
        if obj:
            if obj.is_student and Registration.objects.filter(student=obj).exists():
                self.message_user(request, f"Cannot delete {obj.username}: Related registrations exist.", level='error')
                return False
            if obj.is_teacher and Unit.objects.filter(teacher=obj).exists():
                self.message_user(request, f"Cannot delete {obj.username}: Related units exist.", level='error')
                return False
        return True



admin.site.register(Unit)
from django.db import models
from django.contrib.auth import get_user_model

from django.contrib import admin
from .models import Session

@admin.register(Session)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active', 'start_date', 'end_date')
    search_fields = ('name', 'academic_year')

admin.site.register(Registration)
admin.site.register(Assignment)
admin.site.register(Submission)
