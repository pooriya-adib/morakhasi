from django import forms


class ExcelFileForm(forms.Form):
    file = forms.FileField(label='Select a file')