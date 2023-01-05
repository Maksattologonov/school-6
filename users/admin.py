from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms
from django.utils.translation import gettext_lazy as _

from .forms import CustomCreationForm, CustomChangeForm
from .models import CustomUser, Teacher


class UserCreationForm(forms.ModelForm):
    CHOICES = [('T', 'Teacher'), ('A', 'Admin'), ('S', 'Student')]

    password1 = forms.CharField(label=_('Пароль'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Повторить пароль'), widget=forms.PasswordInput)
    roles = forms.ChoiceField(choices=CHOICES, required=True, label=_('Роли'))
    name = forms.CharField(max_length=100, required=True, label=_("Имя"))
    surname = forms.CharField(max_length=100, required=True, label=_("Фамилия"))
    patronymic = forms.CharField(max_length=100, required=False, label=_("Отчество"))
    date_of_birth = forms.DateField(required=False, label=_("Дата рождения"))

    class Meta:
        model = CustomUser
        fields = ('username', 'name', 'surname', 'role', 'patronymic', 'date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=True)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'is_active', 'role')

    def clean_password(self):
        return self.initial["password"]


class TeacherAdmin(admin.TabularInline):
    model = Teacher
    extra = 1


class UserAdmin(admin.ModelAdmin):
    form = CustomCreationForm
    add_form = CustomChangeForm
    list_display = ('username',)
    list_filter = ('username',)
    add_fieldsets = (
        ('fields', {
            'fields': ('username', 'role', 'name', 'surname', 'patronymic', 'date_of_birth'),
        }),
    )
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('username', 'image', 'job_title', 'subject_id')
    list_filter = ('job_title',)
    search_fields = ('username', 'image', 'job_title')
