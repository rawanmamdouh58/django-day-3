# trainee/forms.py
from django import forms
from .models import Trainee
from course.models import Course


class TraineeForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(status=True),
        empty_label="Select a Course",
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Trainee
        fields = ['name', 'email', 'image', 'course']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter trainee name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter trainee email'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Check if email already exists
        if Trainee.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_name(self):
        name = self.cleaned_data.get('name')
        # Example validation: Ensure name is at least 2 characters long
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name