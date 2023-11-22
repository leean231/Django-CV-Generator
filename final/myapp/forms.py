from django import forms
from .models import Client
from .models import User
from .models import CustomUser

("""class SignUpForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True, min_length=8)
""")

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Use PasswordInput widget for password field
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)



("""class ClientForm(forms.Form):
    ### Collecting User/Client Informations.
    y_name = forms.CharField(label="Enter Your Name", max_length=100, required=False)
    ##p_image_field = forms.ImageField(label="Upload Your Image")
    position = forms.CharField(label="Enter the Position", max_length=100, help_text="Enter the position your applying for", required=False)
    profile = forms.CharField(label="Career Objective", widget=forms.Textarea, required=False)
    location = forms.CharField(label="Location", max_length=200)
    email = forms.EmailField(label="Email Address", max_length=200)
    phone_number = forms.CharField(label='Phone Number', max_length=15, help_text='Enter your phone number (e.g., +1234567890)')
    linkedin = forms.CharField(label='LinkedIn Profile', max_length=200, required=False, help_text='Enter your LinkedIn profile URL')

    ### Collecting Experience
    experience = forms.CharField(label="Enter Your Work Experience", widget=forms.Textarea, required=False)
    education = forms.CharField(label="Enter Your Educational Qualifications", widget=forms.Textarea)
    languages = forms.CharField(label="Enter the Language You Know", widget=forms.Textarea)
    skills = forms.CharField(label="Enter Additional Skills", widget=forms.Textarea, required=False)
    certificate = forms.CharField(label="Enter Additional Certificates", widget=forms.Textarea, required=False)
 """)

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['y_name', 'position', 'profile', 'location', 'email', 'phone_number', 'linkedin', 'experience', 'education', 'languages', 'skills', 'certificate']
        labels = {"y_name":"Name", "profile":"Objective"}
        widgets = {
            'profile': forms.Textarea(attrs={'rows': 3}),  # Set the number of rows for the Textarea widget
            'experience': forms.Textarea(attrs={'rows': 3}),
            'education': forms.Textarea(attrs={'rows': 3}),
            'languages': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
            'certificate': forms.Textarea(attrs={'rows': 3}),
        }