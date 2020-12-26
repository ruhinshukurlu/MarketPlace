from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from account.models import *

from django.contrib.auth import get_user_model

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name','profile_img',)}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'is_customer',
            'is_worker',
            'groups',
            'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'id', 'is_staff','is_customer','is_worker',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_customer','is_worker')
    search_fields = ('email',)
    ordering = ('email',)
    # filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    # search_fields = ('email',)
    # ordering = ('email',)
admin.site.register(Customer, CustomerAdmin)

admin.site.register(Worker)
admin.site.register(WorkPlace)