from django.urls import path
from . import views
from .views import CustomLoginView 
from django.contrib.auth import views as auth_views
from .views import custom_logout_view
from .views import edit_employer_profile, edit_jobseeker_profile
from .views import edit_application
from .views import view_job_applications, view_applicant_profile
from .views import view_employer_profile
from .views import view_job_details


urlpatterns = [
    path('', views.home, name='home'),
    path('employer_dashboard/', views.employer_dashboard, name='employer_dashboard'),
    path('jobseeker_dashboard/', views.jobseeker_dashboard, name='jobseeker_dashboard'),
    path('add_job/', views.add_job, name='add_job'),
    path('apply_for_job/<int:job_id>/', views.apply_for_job, name='apply_for_job'),
    path('edit_job/<int:job_id>/', views.edit_job, name='edit_job'),  # Add this line
    path('delete_job/<int:job_id>/', views.delete_job, name='delete_job'),  
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', custom_logout_view, name='logout'),
    path('edit_employer_profile/', edit_employer_profile, name='edit_employer_profile'),
    path('edit_jobseeker_profile/', edit_jobseeker_profile, name='edit_jobseeker_profile'),
    path('edit_application/<int:application_id>/', edit_application, name='edit_application'),
    path('view_job_applications/<int:job_id>/', view_job_applications, name='view_job_applications'),
    path('view_job_applications/<int:job_id>/', view_job_applications, name='view_job_applications'),
    path('view_applicant_profile/<int:job_id>/<int:jobseeker_id>/', view_applicant_profile, name='view_applicant_profile'),
    path('employer_profile/<int:employer_id>/', view_employer_profile, name='view_employer_profile'),
    path('job_details/<int:job_id>/', view_job_details, name='view_job_details'),
    path('jobseeker/profile/', views.view_jobseeker_profile, name='view_jobseeker_profile'),
    path('company/profile/', views.view_company_profile, name='view_company_profile'),
        
]

