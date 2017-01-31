from django.contrib import admin

from .models import Techno, Project, PrjPhoto, PrjKit, Article, Calculation

class PrjPhotoInline(admin.StackedInline):
    model = PrjPhoto

class PrjKitInline(admin.StackedInline):
    model = PrjKit


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PrjPhotoInline,
        PrjKitInline,
    ]

admin.site.register(Techno)
admin.site.register(Project,ProjectAdmin)
admin.site.register(PrjPhoto)
admin.site.register(Article)
admin.site.register(Calculation)
