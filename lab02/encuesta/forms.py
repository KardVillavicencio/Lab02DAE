from django import forms

OPERACIONES = (
    ('suma', 'Suma'),
    ('resta', 'Resta'),
    ('multiplicacion', 'Multiplicación'),
)

class CalculadoraForm(forms.Form):
    numero1 = forms.DecimalField(label='Primer número')
    numero2 = forms.DecimalField(label='Segundo número')
    operacion = forms.ChoiceField(choices=OPERACIONES, label='Operación')
class CilindroForm(forms.Form):
    altura = forms.DecimalField(label='Altura (metros)')
    diametro = forms.DecimalField(label='Diámetro (metros)')
