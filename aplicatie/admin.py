from django.contrib import admin # Register your models here.
from aplicatie.models import Topic, Webpage, AccessRecord, User, UserProfileInfo

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(User)
admin.site.register(UserProfileInfo)
