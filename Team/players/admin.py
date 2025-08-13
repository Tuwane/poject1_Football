from django.contrib import admin
from .models import Team
# Register your models here.


class TeamAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "age",)
    
admin.site.register(Team, TeamAdmin)

admin.site.site_header = "VAAL ECOS FOOTBALL CLUB ADMIN"
admin.site.site_title = "VAAL ECOS FOOTBALL CLUB PORTAL"
admin.site.index_title = "WELLCOME TO VALL ECOES FC MANAGEMENT PANNEL"