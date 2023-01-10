from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.manager import CustomUser


class CustomCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'role', 'date_of_birth')


class CustomChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'role', 'date_of_birth')