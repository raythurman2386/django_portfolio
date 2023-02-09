from django.contrib import admin
from .models import Summary, Projects, Employment, Education, Skill, Contact, Resume_PDF

# Register your models here.
admin.site.register(Summary)
admin.site.register(Projects)
admin.site.register(Employment)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Resume_PDF)
