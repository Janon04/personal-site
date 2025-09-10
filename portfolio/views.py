from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import PersonalInfo, Experience, Education, Skill, Project, Certificate, Contact, Reference
import json
import os

def home(request):
    # Get or create personal info
    personal_info, created = PersonalInfo.objects.get_or_create(
        defaults={
            'name': 'Janon DUKUZUMUREMYI',
            'email': 'janon3030@gmail.com',
            'phone': '0786003139/0733695764',
            'location': 'Nyamata-Bugesera, Rwanda',
            'profile_summary': 'A certified Data Analyst and Web Developer with expertise in statistical analysis, data management, and full-stack development.'
        }
    )
    
    # Get featured projects
    featured_projects = Project.objects.filter(featured=True)[:3]
    
    # Get top skills by category
    technical_skills = Skill.objects.filter(category='technical')[:6]
    
    context = {
        'personal_info': personal_info,
        'featured_projects': featured_projects,
        'technical_skills': technical_skills,
    }
    return render(request, 'portfolio/home.html', context)

def about(request):
    personal_info = PersonalInfo.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    certificates = Certificate.objects.all()
    references = Reference.objects.all()
    context = {
        'personal_info': personal_info,
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'certificates': certificates,
        'references': references,
    }
    return render(request, 'portfolio/about.html', context)

def projects(request):
    category = request.GET.get('category')
    if category:
        projects = Project.objects.filter(category=category)
    else:
        projects = Project.objects.all()
    categories = Project.CATEGORY_CHOICES
    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'portfolio/projects.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save to database
        contact_message = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Send email notification
        from django.core.mail import send_mail
        send_mail(
            subject=f'New Contact Message: {subject}',
            message=f'Name: {name}\nEmail: {email}\nMessage: {message}',
            from_email='janon3030@gmail.com',
            recipient_list=['janon3030@gmail.com'],
            fail_silently=False,
        )

        messages.success(request, 'Thank you for your message! I will get back to you soon.')
        return redirect('contact')
    
    personal_info = PersonalInfo.objects.first()
    context = {
        'personal_info': personal_info,
    }
    return render(request, 'portfolio/contact.html', context)

def load_initial_data(request):
    """Load initial data from JSON file"""
    json_file_path = os.path.join(settings.BASE_DIR.parent, 'portfolio_data.json')
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
        # Create or update personal info
        personal_details = data['personal_details']
        personal_info, created = PersonalInfo.objects.get_or_create(
            defaults={
                'name': personal_details['name'],
                'email': personal_details['email'],
                'phone': personal_details['phone'],
                'location': personal_details['location'],
                'profile_summary': personal_details['profile_summary']
            }
        )
        
        # Create experiences
        for i, exp in enumerate(data['professional_experience']):
            Experience.objects.get_or_create(
                title=exp['title'],
                organization=exp['organization'],
                defaults={
                    'duration': exp['duration'],
                    'location': exp['location'],
                    'description': exp['description'],
                    'order': i
                }
            )
        
        # Create education
        for i, edu in enumerate(data['education']):
            Education.objects.get_or_create(
                degree=edu['degree'],
                institution=edu['institution'],
                defaults={
                    'duration': edu['duration'],
                    'location': edu['location'],
                    'description': edu.get('description', ''),
                    'order': i
                }
            )
        
        # Create skills
        for skill_name in data['skills']:
            category = 'technical'
            if any(word in skill_name.lower() for word in ['communication', 'decision', 'driving']):
                category = 'soft'
            elif any(word in skill_name.lower() for word in ['power', 'stata', 'spss', 'excel']):
                category = 'tools'
            elif any(word in skill_name.lower() for word in ['data', 'analysis', 'statistical']):
                category = 'analytical'
                
            Skill.objects.get_or_create(
                name=skill_name,
                defaults={
                    'category': category,
                    'proficiency': 85
                }
            )
        
        # Create certificates
        for cert_name in data['certificates']:
            Certificate.objects.get_or_create(
                name=cert_name,
                defaults={
                    'issuer': 'Professional Certification Body'
                }
            )
        
        return render(request, 'portfolio/data_loaded.html', {'message': 'Data loaded successfully!'})
    
    return render(request, 'portfolio/data_loaded.html', {'message': 'No data file found!'})
