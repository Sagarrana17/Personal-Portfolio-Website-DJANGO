from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    Linkedln = models.CharField(max_length=100)
    Dribble = models.CharField(max_length=100)
    Github = models.CharField(max_length=100)
    Home_image = models.ImageField(upload_to='HomeImage')
    
    def __str__(self):
        return str(self.id)
    
class About(models.Model):
    description = models.TextField()
    experience = models.CharField(max_length=10)
    project = models.CharField(max_length=10)
    worked = models.CharField(max_length=10)
    About_image = models.ImageField(upload_to='AboutImage')
    
    def __str__(self):
        return str(self.id)
    
class Skills(models.Model):
    
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    skills_name1 = models.CharField(max_length=50)
    skills_number1 = models.IntegerField()
    skills_name2 = models.CharField(max_length=50)
    skills_number2 = models.IntegerField()
    skills_name3 = models.CharField(max_length=50)
    skills_number3 = models.IntegerField()
    skills_name4 = models.CharField(max_length=50)
    skills_number4 = models.IntegerField()
    
    def __str__(self):
            return str(self.id)
        
class Qualification(models.Model):
    
    qualification_title_E = models.CharField(max_length=100)
    qualification_subtitle_E = models.CharField(max_length=100)
    qualification_calender_E = models.CharField(max_length=100)
    qualification_title_W = models.CharField(max_length=100)
    qualification_subtitle_W = models.CharField(max_length=100)
    qualification_calender_W = models.CharField(max_length=100)
    
    def __str__(self):
            return str(self.id)
        
class Sevices(models.Model):
    
    services_icon = models.TextField()
    services_title_1 = models.CharField(max_length=20)
    services_title_2 = models.CharField(max_length=20)
    services_line1 = models.TextField()
    services_line2 = models.TextField()
    services_line3 = models.TextField()
    services_line4 = models.TextField()
    
    def __str__(self):
            return str(self.id)
    
    
    
    