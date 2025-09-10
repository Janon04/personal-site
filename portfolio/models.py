
from django.db import models
from ckeditor.fields import RichTextField

class Reference(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    email = models.EmailField()
    def __str__(self):
        return self.name

class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    profile_summary = RichTextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    signature_image = models.ImageField(upload_to='profile/signature/', blank=True, null=True, help_text='Upload a PNG signature image.')
    signature_pdf = models.FileField(upload_to='profile/signature/', blank=True, null=True, help_text='Upload a PDF signature.')
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = RichTextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.title} at {self.organization}"

class Education(models.Model):
    degree = models.CharField(max_length=200)
    duration = models.CharField(max_length=50)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = RichTextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('technical', 'Technical'),
        ('analytical', 'Analytical'),
        ('soft', 'Soft Skills'),
        ('tools', 'Tools & Software'),
    ])
    proficiency = models.IntegerField(default=80, help_text="Proficiency level (0-100)")
    
    def __str__(self):
        return self.name

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('data', 'Data Analysis'),
        ('web', 'Web Development'),
        ('ml', 'Machine Learning'),
        # Add more as needed
    ]
    title = models.CharField(max_length=100)
    description = RichTextField()
    technologies = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    date_issued = models.DateField(blank=True, null=True)
    credential_url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='certificates/', blank=True, null=True, help_text='Upload certificate as PDF')

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name}"
