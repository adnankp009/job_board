from django import forms
from .models import Job, Application, Employer, Jobseeker

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','requirements', 'location', 'salary']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['cover_letter']

class EmployerProfileForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ['company_name', 'company_description', 'profile_picture']

class JobseekerProfileForm(forms.ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['profile_picture','bio','education', 'current_job', 'work_experience','resume']
