from django import forms;

class LoginForm(forms.Form):
	name=forms.CharField();

# application-4
from django import forms;

class ItemAddForm(forms.Form):
		name = forms.CharField();
		quantity = forms.IntegerField();
