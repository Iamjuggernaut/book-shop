from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
import hashlib
import random

from authapp.models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


    # def save(self):
    #     user = super(ShopUserRegisterForm, self).save()

    #     user.is_active = False
    #     salt = hashlib.shal(str(random.random()).encode('utf8')).hexdigest()[:6]
    #     user.activation_key = hashlib.shal((user.email + salt).encode('utf8')).hexdigest()
    #     user.save()