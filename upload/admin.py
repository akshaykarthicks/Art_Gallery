from django.contrib import admin
from .models import Image
from django.utils.html import format_html
from unfold.admin import ModelAdmin

class ImageAdmin(ModelAdmin):
    list_display = ("id", "image_tag", "date")
    readonly_fields = ("image_tag",)
    search_fields = ("image",)
    list_filter = ("date",)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" />', obj.image.url)
        return "No Image"
    image_tag.short_description = "Image Preview"

admin.site.register(Image, ImageAdmin)
