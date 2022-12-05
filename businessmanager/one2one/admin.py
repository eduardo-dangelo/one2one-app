from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Project, One2One, Okr

class OkrInline(admin.TabularInline):
    model = Okr
    fieldsets = [
        (None, {'fields':  ['title', 'result_note', 'completion_score']}),
    ]
    extra = 0

class One2OneInline(admin.TabularInline):
    model = One2One
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['title', 'created_at']}),
    ]
    inlines = [One2OneInline]

class One2OneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['title', 'created_at', 'project']}),
    ]
    inlines = [OkrInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(One2One, One2OneAdmin)
# Register your models here.
