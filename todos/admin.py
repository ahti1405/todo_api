from django.contrib import admin

from .models import Todo



class TodoAdmin(admin.ModelAdmin):
    
    model = Todo
    list_display = ('title', 'created')


admin.site.register(Todo, TodoAdmin)