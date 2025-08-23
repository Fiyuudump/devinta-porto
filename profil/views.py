from django.shortcuts import render
from profil.models import About,SocialMedia, Experience, Education, Skill, Interest

def home(request):
    abouts = About.objects.first()
    social_medias = SocialMedia.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()
    skills = Skill.objects.all()
    interests = Interest.objects.all()

    if abouts and abouts.name:
        full_name = abouts.name
        parts = full_name.split(' ', 1)
        a_first_name = parts[0]
        a_last_names = parts[1] if len(parts) > 1 else ''
    else:
        a_first_name = ""
        a_last_names = ""


    context = {
        'abouts': abouts,
        'social_medias': social_medias,
        'experiences': experiences,
        'educations': educations,
        'skills': skills,
        'interests': interests,
        'a_first_name': a_first_name,
        'a_last_names': a_last_names,
    }

    return render(request, 'index.html', context)
