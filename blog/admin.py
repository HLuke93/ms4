from django.contrib import admin
from .models import Post
from django_summernote.admin import SummerNoteModelAdmin

@admin.register(Post)
class PostAdmin(SummerNoteModelAdmin):
    summernote_fields = ('content')

