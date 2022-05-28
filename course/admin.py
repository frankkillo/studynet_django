from django.contrib import admin

from .models import Category, Course, Lesson, Comment, Quiz


class LessonCommentInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ["lesson"]


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class LessonAdmin(admin.ModelAdmin):
    list_display = ["title", "course", "status", "type"]
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["status", "type"]
    search_fields = ["title", "short_description", "long_description"]
    inlines = [LessonCommentInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment)
admin.site.register(Quiz)