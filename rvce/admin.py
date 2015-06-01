from django.contrib import admin

from .models import Result, Subject

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

class SGPAFilter(admin.SimpleListFilter):
    title = _('SGPA')

    parameter_name = 'sgpaSort'

    def lookups(self, request, model_admin):
        return (
            ('10', _('10')),
            ('9p', _('9-10')),
            ('8p', _('8-9')),
            ('7p', _('7-8')),
            ('6p', _('6-7')),
            ('5p', _('5-6')),
            ('4p', _('4-5')),
            ('3p', _('3-4')),
            ('2p', _('2-3')),
            ('1p', _('1-2')),
            ('0p', _('0-1')),
        )

    def queryset(self, request, queryset):
        if self.value() == '10':
            return queryset.filter(result_sgpa__gte=10)
        if self.value() == '9p':
            return queryset.filter(result_sgpa__gte=9.0, result_sgpa__lt=10).order_by('result_sgpa')
        if self.value() == '8p':
            return queryset.filter(result_sgpa__gte=8.0, result_sgpa__lt=9).order_by('result_sgpa')
        if self.value() == '7p':
            return queryset.filter(result_sgpa__gte=7.0, result_sgpa__lt=8).order_by('result_sgpa')
        if self.value() == '6p':
            return queryset.filter(result_sgpa__gte=6.0, result_sgpa__lt=7).order_by('result_sgpa')
        if self.value() == '5p':
            return queryset.filter(result_sgpa__gte=5.0, result_sgpa__lt=6).order_by('result_sgpa')
        if self.value() == '4p':
            return queryset.filter(result_sgpa__gte=4.0, result_sgpa__lt=5).order_by('result_sgpa')
        if self.value() == '3p':
            return queryset.filter(result_sgpa__gte=3.0, result_sgpa__lt=4).order_by('result_sgpa')
        if self.value() == '2p':
            return queryset.filter(result_sgpa__gte=2.0, result_sgpa__lt=3).order_by('result_sgpa')
        if self.value() == '1p':
            return queryset.filter(result_sgpa__gte=1.0, result_sgpa__lt=2).order_by('result_sgpa')
        if self.value() == '0p':
            return queryset.filter(result_sgpa__gte=0.0, result_sgpa__lt=1).order_by('result_sgpa')
       
class AdminOwn(admin.ModelAdmin):
    list_display = ('result_name', 'result_sgpa', 'result_usn')
    fieldsets = [
    	('Basic Information', {'fields': ['result_name', 'result_usn', 'result_sem']}),
    	('Result'           , {'fields': ['result_sgpa', 'result_branch', 'result_sub']}),
    ]
    search_fields = ['result_name']

    list_filter = ('result_branch', SGPAFilter, 'result_sem')

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return self.readonly_fields
        #get all fields as readonly
        fields = [f.name for f in self.model._meta.fields]
        return fields

# Register your models here.
admin.site.register(Result, AdminOwn)
admin.site.register(Subject)
# admin.site.register(Result)