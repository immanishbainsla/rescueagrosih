from django.contrib import admin
from .models import Organisation,address1,Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'user', 'is_active', 'amount', 'type') #
    list_display_links = ('name', 'id')
    search_fields = ('name',) #
    list_editable = ('is_active',)
    list_per_page = 25

admin.site.register(Post, PostAdmin)

admin.site.register(Organisation)
admin.site.register(address1)
# admin.site.register(Post)
