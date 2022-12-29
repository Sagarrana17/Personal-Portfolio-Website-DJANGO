from django.contrib import admin
from .models import Home,About,Skills,Qualification,Sevices

# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['id','title','subtitle','description','Linkedln','Dribble','Github','Home_image']
    
@admin.register(About)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id','description','experience','project','worked','About_image']
    
@admin.register(Skills)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id','icon','title','subtitle','skills_name1','skills_number1','skills_name2','skills_number2','skills_name3','skills_number3','skills_name4','skills_number4']

@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    list_display = ['id','qualification_title_E','qualification_subtitle_E', 'qualification_calender_E','qualification_title_W','qualification_subtitle_W', 'qualification_calender_W']
    
@admin.register(Sevices)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id','services_icon','services_title_1','services_title_2','services_line1','services_line2','services_line3','services_line4']