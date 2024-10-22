from django.contrib import admin

from works.models import (
    Achievement,
    Advantage,
    Employee,
    Position,
    Review,
    Service,
    Slide,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    list_display_links = ("title",)
    search_fields = (
        "title",
        "description",
    )
    fields = (
        "title",
        "description",
        "preview",
        "alt_text",
    )


@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    search_fields = (
        "title",
        "description",
    )
    fields = (
        "title",
        "icon_class",
        "description",
    )


@admin.register(Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = (
        "slide_info",
        "alt_text",
    )
    list_display_links = ("slide_info",)
    fields = (
        "image",
        "alt_text",
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at")
    list_display_links = ("author",)
    search_fields = (
        "author",
        "text",
    )
    fields = (
        "author",
        "author_avatar",
        "alt_text",
        "text",
        "created_at",
    )
    readonly_fields = ("created_at",)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)
    fields = ("name",)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position")
    list_display_links = ("full_name",)
    list_filter = ("position",)
    search_fields = (
        "first_name",
        "last_name",
    )
    fields = (
        "first_name",
        "last_name",
        "position",
        "avatar",
        "alt_text",
    )


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_display_links = ("title",)
    search_fields = ("title",)
    fields = ("title", "description")


admin.site.empty_value_display = "Не указано"
