from django import forms

class CreateListForm(forms.Form):
	name = forms.CharField(label="Name ", max_length=300)

