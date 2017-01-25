from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from imageledger import models
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'provider', 'created_on', 'last_synced_with_source')
    fields = ( 'image_tag', 'title', 'provider', 'license', 'license_version', 'created_on', 'last_synced_with_source',
              'foreign_landing_url', 'foreign_identifier')
    readonly_fields = ('image_tag', 'created_on', 'last_synced_with_source', )

class ListAdmin(admin.ModelAdmin):
    empty_value_display = '-blank-'
    list_display = ('title', 'owner', 'num_images', 'is_public', 'created_on', 'updated_on')
    readonly_fields = ('images', 'slug')
    def num_images(self, obj):
        return obj.images.all().count()

#    filter_horizontal = ['images']
admin.site.register(models.List, ListAdmin)
admin.site.register(models.Image, ImageAdmin)
