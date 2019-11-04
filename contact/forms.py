from django import forms

class ContactForm(forms.Form):
    name    = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class':'form-control' , 'placeholder': 'El juanpa de NY'}
    ), min_length=3, max_length=100)
    email   = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={'class':'form-control' , 'placeholder': 'ejemplo@ejemplo.com'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'rows': 3, 'placeholder': 'Escríbenos tus dudas o comentarios'}
    ), min_length=10, max_length=1000)