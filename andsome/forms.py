from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={ 'size':60 }))
    body = forms.CharField(widget=forms.Textarea(attrs={'class':'vLargeTextField', 'rows':10, 'cols':40 }))
    
    def get_data(self):
        return self.cleaned_data['subject'], self.cleaned_data['body']
