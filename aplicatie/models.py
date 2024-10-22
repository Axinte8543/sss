from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True) 
    def __str__(self): 
        return self.top_name
    
    
class Webpage(models.Model): 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True) 

    def __str__(self): 
        return self.name
    
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE) 
    date = models.DateField() 

    def __str__(self): 
        return str(self.date)
    
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    
    def __str__(self):
        return self.first_name

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #leaga modelul de modelul User printr-o relatie one-to-one, daca user este sters atunci este sters si modelul acesta
    portfolio_site = models.URLField(blank=True) #camp optional
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True) #pozele de profil incarcate vor fi pusa in folderul profile_pics
    
    def __str__(self):
        return self.user.first_name #o sa returneze first_name