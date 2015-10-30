from django import forms

class borrow(forms.Form):
	amount = forms.PositiveSmallIntegerField(default=0)
	