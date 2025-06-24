from django.contrib import admin
from .models import Patient
from .models import Feedback
from .models import ConsultationRequest

# Register your models here.
admin.site.register(Patient)

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('patient', 'rating','comment','submitted_at')
    search_fields = ('patient__full_name', 'comment')
    list_filter = ('rating', 'submitted_at')

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = ('patient', 'mode', 'preferred_time', 'submitted_at')
    list_filter = ('mode', 'submitted_at')
    search_fields = ('patient__full_name', 'symptoms')
