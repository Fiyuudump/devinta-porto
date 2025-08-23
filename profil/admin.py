from django.contrib import admin
from . models import About, Experience, Education, Skill, Interest, SocialMedia

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm
from unfold.admin import ModelAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
  # Forms loaded from `unfold.forms`
  form = UserChangeForm
  add_form = UserCreationForm
  change_password_form = AdminPasswordChangeForm

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
  pass

# ----------------------------------------------------------------

class SocialMediaAdmin(ModelAdmin):
  list_display=['css_icon', 'link']
  search_fields=['css_icon']
  list_filter=('css_icon',)
  list_per_page=10

class AboutAdmin(ModelAdmin):
  list_display=['name','address','postal_code','phone','email']
  search_fields=['name']
  list_filter=('name','address')
  list_per_page=10

class ExperienceAdmin(ModelAdmin):
  list_display=['job_title', 'job_desc', 'experience']
  search_fields=['job_title']
  list_filter=('job_title', 'job_desc')
  list_per_page=10

class EducationAdmin(ModelAdmin):
  list_display=['degree', 'major', 'experience']
  search_fields=['degree']
  list_filter=('degree', 'major')
  list_per_page=10

class SkillAdmin(ModelAdmin):
  list_display=['experience', 'css_icon']
  search_fields=['experience']
  list_filter=('experience',)
  list_per_page=10

class InterestAdmin(ModelAdmin):
  list_display=['desc']
  search_fields=['desc']
  list_filter=('desc',)
  list_per_page=10

admin.site.register(SocialMedia, SocialMediaAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(About, AboutAdmin)
