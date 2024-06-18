from django.contrib import admin
from .models import Doctor
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs['minlength'] = 4
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class CustomDoctorAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Doctor
    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'surname', 'iin', 'phone_number', 'password', 'email', 'position')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'surname', 'iin', 'phone_number', 'password', 'email', 'position')}
        ),
    )
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'position')
    ordering = ('last_name', 'first_name')
    

admin.site.register(Doctor, CustomDoctorAdmin)
