from django import forms

from django.contrib.auth import(
authenticate,
get_user_model,
login,
logout
)
user=get_user_model()

class userLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username="username",password="password")

        if username and password:
            user=authenticate(username="username",password="password")
        if not user:
            raise forms.ValidationError("Username entered is incorrect")
        if not user.check_password(password):
                raise forms.ValidationError("Password entered is incorrect")
        return super(userLoginForm,self).clean(*args,**kwargs)




class userRegisterForm(forms.ModelForm):

    class Meta:
        model = user
        fields=[
            "username",
            "email",
            "password",
        
            

        ]
    email=forms.EmailField(label='Email Address')
    password=forms.CharField(widget=forms.PasswordInput)
  

