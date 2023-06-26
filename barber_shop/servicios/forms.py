from django import forms
    
class agregarServicio(forms.Form):
    nombre = forms.CharField(max_length=100)
    precio = forms.CharField.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    descripcion = forms.CharField(max_length=255)
  