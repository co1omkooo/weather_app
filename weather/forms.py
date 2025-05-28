from django import forms


class CityForm(forms.Form):
    city = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите город',
            'autocomplete': 'off'  # отключаем автозаполнение браузера
        })
    )
