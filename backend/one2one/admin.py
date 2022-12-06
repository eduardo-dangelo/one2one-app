from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Workspace, One2One, Okr

class OkrInline(admin.TabularInline):
    model = Okr
    fieldsets = [
        (None, {'fields':  ['title', 'result_note', 'completion_score']}),
    ]
    extra = 0

class One2OneInline(admin.TabularInline):
    model = One2One
    extra = 0

class WorkspaceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['title', 'created_at']}),
    ]
    inlines = [One2OneInline]

class One2OneAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':  ['title', 'created_at', 'workspace']}),
    ]
    inlines = [OkrInline]

admin.site.register(Workspace, WorkspaceAdmin)
admin.site.register(One2One, One2OneAdmin)
# Register your models here.
