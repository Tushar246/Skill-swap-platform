from django.contrib import admin
from .models import UserProfile, Skill, OfferedSkill, WantedSkill

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(OfferedSkill)
admin.site.register(WantedSkill)
