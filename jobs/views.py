from django.shortcuts import render, redirect
from .models import Job, Application, Employer, Jobseeker
from .forms import JobForm, ApplicationForm, EmployerProfileForm, JobseekerProfileForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout

from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.views import LoginView

from django.contrib.auth import get_user_model

from .models import Employer


def home(request):
    return render(request, 'jobs/home.html')

@login_required
def employer_dashboard(request):
    if not hasattr(request.user, 'employer'):
        return redirect('home')

    jobs = Job.objects.filter(employer=request.user.employer)
    return render(request, 'jobs/employer_dashboard.html', {'jobs': jobs})

@login_required
def jobseeker_dashboard(request):
    if not hasattr(request.user, 'jobseeker'):
        return redirect('home')

    jobs = Job.objects.all()
    applications = Application.objects.filter(jobseeker=request.user.jobseeker)
    return render(request, 'jobs/jobseeker_dashboard.html', {'jobs': jobs, 'applications': applications})

@login_required
def add_job(request):
    if not hasattr(request.user, 'employer'):
        return redirect('home')

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user.employer
            job.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm()

    return render(request, 'jobs/add_job.html', {'form': form})

@login_required
def apply_for_job(request, job_id):
    if not hasattr(request.user, 'jobseeker'):
        return redirect('home')

    job = Job.objects.get(id=job_id)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.jobseeker = request.user.jobseeker
            application.save()
            return redirect('jobseeker_dashboard')
    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_for_job.html', {'form': form, 'job': job})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        user_type = request.POST.get('user_type')
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user_type == 'employer':
                Employer.objects.create(user=user)
                return redirect('employer_dashboard')
            else:
                Jobseeker.objects.create(user=user)
                return redirect('jobseeker_dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user.employer)
    
    if request.method == 'POST':
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('employer_dashboard')
    else:
        form = JobForm(instance=job)
    
    return render(request, 'jobs/edit_job.html', {'form': form, 'job': job})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user.employer)
    
    if request.method == 'POST':
        job.delete()
        return redirect('employer_dashboard')
    
    return render(request, 'jobs/delete_job.html', {'job': job})


class CustomLoginView(LoginView):
    def get_redirect_url(self):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, 'employer'):
                return '/employer_dashboard/'
            elif hasattr(user, 'jobseeker'):
                return '/jobseeker_dashboard/'
        return super().get_redirect_url()



def custom_logout_view(request):
    logout(request)
    return redirect('login')  


@login_required
def edit_employer_profile(request):
    if not hasattr(request.user, 'employer'):
        return redirect('home')

    if request.method == 'POST':
        form = EmployerProfileForm(request.POST, request.FILES, instance=request.user.employer)
        if form.is_valid():
            form.save()
            return redirect('employer_dashboard')
    else:
        form = EmployerProfileForm(instance=request.user.employer)

    return render(request, 'jobs/edit_employer_profile.html', {'form': form})


@login_required
def edit_jobseeker_profile(request):
    if not hasattr(request.user, 'jobseeker'):
        return redirect('home')

    if request.method == 'POST':
        form = JobseekerProfileForm(request.POST, request.FILES, instance=request.user.jobseeker)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_dashboard')
    else:
        form = JobseekerProfileForm(instance=request.user.jobseeker)

    return render(request, 'jobs/edit_jobseeker_profile.html', {'form': form})


@login_required
def edit_application(request, application_id):
    application = get_object_or_404(Application, id=application_id, jobseeker=request.user.jobseeker)
    
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('jobseeker_dashboard')
    else:
        form = ApplicationForm(instance=application)
    
    return render(request, 'jobs/edit_application.html', {'form': form, 'application': application})


@login_required
def view_job_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, employer=request.user.employer)
    applications = Application.objects.filter(job=job)
    return render(request, 'jobs/view_job_applications.html', {'job': job, 'applications': applications})

@login_required
def view_applicant_profile(request, job_id, jobseeker_id):
    applicant = get_object_or_404(Jobseeker, id=jobseeker_id)
    job = get_object_or_404(Job, id=job_id)
    applications = Application.objects.filter(job=job, jobseeker=applicant)
    
    if applications.count() == 1:
        application = applications.first()
    else:
        
        application = None  
    
    return render(request, 'jobs/view_applicant_profile.html', {
        'applicant': applicant,
        'job': job,
        'application': application
    })



@login_required
def view_employer_profile(request, employer_id):
    employer = get_object_or_404(Employer, id=employer_id)
    return render(request, 'jobs/view_employer_profile.html', {'employer': employer})


def view_job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/view_job_details.html', {'job': job})

@login_required
def view_jobseeker_profile(request):
    jobseeker = get_object_or_404(Jobseeker, user=request.user)
    return render(request, 'jobs/view_jobseeker_profile.html', {'jobseeker': jobseeker})

@login_required
def view_company_profile(request):
    employer = get_object_or_404(Employer, user=request.user)
    return render(request, 'jobs/view_company_profile.html', {'employer': employer})





