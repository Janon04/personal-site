
from django.contrib import admin

from .models import PersonalInfo, Experience, Education, Skill, Project, Certificate, Contact, Reference
@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
	pass
from django import forms
from ckeditor.widgets import CKEditorWidget

# Custom admin forms for rich text fields
class PersonalInfoAdminForm(forms.ModelForm):
	class Meta:
		model = PersonalInfo
		fields = '__all__'
		widgets = {
			'profile_summary': CKEditorWidget(),
			# File/image fields use default widgets
		}

class ExperienceAdminForm(forms.ModelForm):
	class Meta:
		model = Experience
		fields = '__all__'
		widgets = {
			'description': CKEditorWidget(),
		}

class EducationAdminForm(forms.ModelForm):
	class Meta:
		model = Education
		fields = '__all__'
		widgets = {
			'description': CKEditorWidget(),
		}

class ProjectAdminForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = '__all__'
		widgets = {
			'description': CKEditorWidget(),
		}

class ContactAdminForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'message': CKEditorWidget(),
		}

@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
	form = PersonalInfoAdminForm

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
	form = ExperienceAdminForm

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
	form = EducationAdminForm

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
	pass

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminForm

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
	pass

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	form = ContactAdminForm
