from django.contrib import admin
from .models import UserLocation, TokenSummary, VisitCount,ContactFormData
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'time']

class TokenSummaryAdmin(admin.ModelAdmin):
    list_display = ['author', 'chat_id', 'link']

class VisitCountAdmin(admin.ModelAdmin):
    list_display = ['author', 'visit_count', 'today_total', 'monthly_total', 'yearly_total']

admin.site.register(UserLocation)
admin.site.register(TokenSummary, TokenSummaryAdmin)
admin.site.register(VisitCount, VisitCountAdmin)
admin.site.register(ContactFormData, ContactAdmin)
