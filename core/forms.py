from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	'''
	name = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))

	email = forms.EmailField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))

	message = forms.CharField(widget=forms.Textarea(
		attrs={
			'class': 'form-control'
		}
	))
	'''

	class Meta:
		model = Contact
		fields = ('name', 'email', 'message')