from django.contrib import admin

from .models import Techno, Project, PrjPhoto, PrjBuilt, PrjKit, Readyobj, ReadyPhoto, Reconst, ReconstPhoto, Article, Review, ReviewPhoto, Calculation, PhoneCall

class PrjPhotoInline(admin.StackedInline):
    model = PrjPhoto

class PrjBuiltInline(admin.StackedInline):
    model = PrjBuilt

class PrjKitInline(admin.StackedInline):
    model = PrjKit

class ReadyPhotoInline(admin.StackedInline):
    model = ReadyPhoto

class ReconstPhotoInline(admin.StackedInline):
    model = ReconstPhoto

class ReviewPhotoInline(admin.StackedInline):
    model = ReviewPhoto

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PrjPhotoInline,
        PrjBuiltInline,
        PrjKitInline,
    ]

class ReadyobjAdmin(admin.ModelAdmin):
    inlines = [
        ReadyPhotoInline,
    ]

class ReconstAdmin(admin.ModelAdmin):
    inlines = [
        ReconstPhotoInline,
    ]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'publish')

class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        ReviewPhotoInline,
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
admin.site.register(Readyobj,ReadyobjAdmin)
admin.site.register(Reconst,ReconstAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(Calculation,CalculationAdmin)
admin.site.register(PhoneCall,PhoneCallAdmin)

