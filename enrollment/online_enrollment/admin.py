from django.contrib import admin
from .models import  StudentInfo, EducationalBackground, Account, FamilyBackground, Subjects

admin.site.register(StudentInfo)
admin.site.register(EducationalBackground)
admin.site.register(Account)
admin.site.register(FamilyBackground)
admin.site.register(Subjects)
