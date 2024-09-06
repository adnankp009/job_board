from django.contrib.auth.models import User
from django.db import models

class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_description = models.TextField()
    profile_picture = models.ImageField(upload_to='employer_pictures/', blank=True, null=True)

    def __str__(self):
        return self.company_name
    

class Jobseeker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='jobseeker_pictures/', blank=True, null=True)
    bio = models.TextField()
    education = models.TextField(blank=True, null=True)
    current_job = models.CharField(max_length=255, blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.user.username
    

class Job(models.Model):
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements= models.TextField(default="No specific requirements")
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Application(models.Model):
#     job = models.ForeignKey(Job, on_delete=models.CASCADE)
#     jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
#     cover_letter = models.TextField()
#     applied_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.jobseeker.user.username} - {self.job.title}'

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    cover_letter = models.TextField()
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'jobseeker')

    def __str__(self):
        return f'{self.jobseeker.user.username} - {self.job.title}'
    