from django import forms
from django.contrib.admin.forms import AdminAuthenticationForm


class CustomAdminAuthenticationForm(AdminAuthenticationForm):

    class Media:
        css = {'all': ('path/to/media.css',)}

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username == 'customform':
            raise forms.ValidationError('custom form error')
        return username