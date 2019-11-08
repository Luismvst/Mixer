from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm (UserCreationForm):

    class Meta:
        fields = ('username',)
        model = get_user_model()

        def __init__(self, *args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
            # ver si se puede ingresar por defecto