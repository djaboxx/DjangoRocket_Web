from django.forms import ModelForm, TextInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User as AuthUser
from django.contrib import auth
from django import forms
from account.models import Organization, User, Team
from django.utils.translation import gettext_lazy as _

class OrganiztionForm(ModelForm):
    class Meta:
        model = Organization
        fields = ['org_name']
        labels = {
            'org_name': _('Organiztion')
        }
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password'
        ]
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name')
        }
        
class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name']



class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(forms.Form):

    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(render_value=False)
    )
    remember = forms.BooleanField(
        label=_("Remember Me"),
        required=False
    )
    user = None

    def clean(self):
        if self._errors:
            return
        user = auth.authenticate(**self.user_credentials())
        if user:
            if user.is_active:
                self.user = user
            else:
                raise forms.ValidationError(_("This account is inactive."))
        else:
            raise forms.ValidationError(self.authentication_fail_message)
        return self.cleaned_data

    def user_credentials(self):
        return hookset.get_user_credentials(self, self.identifier_field)


class UserLoginForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = [
            "username",
            "password"
        ]
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None