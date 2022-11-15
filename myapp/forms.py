from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=255)
    gender = forms.CharField(max_length=1)
    age = forms.IntegerField(required=True)

    def __str__(self):
        return self.email