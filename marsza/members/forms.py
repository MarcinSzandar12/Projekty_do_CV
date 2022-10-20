from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile
from django import forms
from django.forms.widgets import ClearableFileInput

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Imię")
    last_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nazwisko")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = "Nazwa użytkownika"
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = "Hasło"
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = "Potwierdź hasło"

class EditProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Imię")
    last_name = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nazwisko")
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Nazwa użytkownika")
    last_login = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="Ostatnie logowanie")
    is_superuser = forms.CharField(max_length=55, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label="Admin")
    is_staff = forms.CharField(max_length=55, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label="Dostęp do funkcji Admina")
    is_active = forms.CharField(max_length=55, widget=forms.CheckboxInput(attrs={'class': 'form-check'}), label="Aktywny")
    date_joined = forms.CharField(max_length=55, widget=forms.TextInput(attrs={'class': 'form-control'}), label="data dołączenia")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined')

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=55, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label="Stare hasło")
    new_password1 = forms.CharField(max_length=55, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label="Nowe hasło")
    new_password2 = forms.CharField(max_length=55, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}), label="Potwierdź nowe hasło")

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'Obecne'
    input_text = 'Zmień'
    clear_checkbox_label = 'Usuń'

class EditProfilePageForm(forms.ModelForm):
    profile_pic = forms.ImageField(required = False, widget=MyClearableFileInput)

    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProfilePageForm, self).__init__(*args, **kwargs)

        self.fields['bio'].label = "Twój Opis"
        self.fields['profile_pic'].label = "Zdjęcie Profilowe"
        self.fields['website_url'].label = "Link do twojego ulubionego Portalu"
        self.fields['facebook_url'].label = "Link do konta na Facebook'u"
        self.fields['twitter_url'].label = "Link do konta na Twitter'rze"
        self.fields['instagram_url'].label = "Link do konta na Instagram'ie"

class CreateProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'twitter_url', 'instagram_url']

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(CreateProfilePageForm, self).__init__(*args, **kwargs)

        self.fields['bio'].label = "Twój Opis"
        self.fields['profile_pic'].label = "Zdjęcie Profilowe"
        self.fields['website_url'].label = "Link do twojego ulubionego Portalu"
        self.fields['facebook_url'].label = "Link do konta na Facebook'u"
        self.fields['twitter_url'].label = "Link do konta na Twitter'rze"
        self.fields['instagram_url'].label = "Link do konta na Instagram'ie"


        



