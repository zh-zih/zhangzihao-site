from django.contrib import admin
from .models import Post, MediaFile

# Register your models here.
class MediaFileInline(admin.TabularInline):
    model = MediaFile
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [MediaFileInline]

    list_display = ("id", "order", "title", "post_info", "created_date", "display_date", "media_info", "content_preview")
    list_editable = ("order",)
    search_fields = ("title", "content", "post_info")
    ordering = ("-order", "-id")

    @admin.display(description="Media")
    def media_info(self, obj):
        media_list = obj.media.all()  # related_name='media'
        return ", ".join([f"{m.type}: {m.file.name.split('/')[-1]}" for m in media_list])

    @admin.display(description="Content")
    def content_preview(self, obj):
        text = (obj.content or "").strip()
        return (text[:80] + "…") if len(text) > 80 else text
    