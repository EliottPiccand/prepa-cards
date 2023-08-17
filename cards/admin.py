from django.contrib import admin

from .models import Subject, Chapter, Question


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
    )

    fieldsets = (
        (None, {
            "fields": (
                "name",
            )
        }),
    )

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        "year",
        "subject",
        "name",
    )

    fieldsets = (
        (None, {
            "fields": (
                "year",
                "subject",
                "name",
            )
        }),
    )

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "chapter",
        "question",
        "answer",
    )

    fieldsets = (
        (None, {
            "fields": (
                "chapter",
                "question",
                "answer",
            )
        }),
    )
