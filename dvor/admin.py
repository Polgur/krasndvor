from django.contrib import admin

from .models import Techno, Project, PrjPhoto, PrjKit, Article, Calculation, PhoneCall

class PrjPhotoInline(admin.StackedInline):
    model = PrjPhoto

class PrjKitInline(admin.StackedInline):
    model = PrjKit


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PrjPhotoInline,
        PrjKitInline,
    ]

class CalculationAdmin(admin.ModelAdmin):
    list_display = ('created', 'fio', 'email', 'phone', 'kit')
    ordering = ('-created',)

class PhoneCallAdmin(admin.ModelAdmin):
    list_display = ('created','phone','wtime','fio','email')
    ordering = ('-created',)

admin.site.register(Techno)
admin.site.register(Project,ProjectAdmin)
admin.site.register(PrjPhoto)
admin.site.register(Article)
admin.site.register(Calculation,CalculationAdmin)
admin.site.register(PhoneCall,PhoneCallAdmin)

