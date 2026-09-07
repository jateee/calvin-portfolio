from django.contrib import admin

from .models import (
    SiteProfile,
    Service,
    Project,
    ProjectImage,
    Skill,
    ContactMessage,
)


# =====================================================
# SITE PROFILE
# =====================================================

@admin.register(SiteProfile)
class SiteProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "professional_title",
        "email",
        "phone",
        "updated_at",
    )

    fieldsets = (

        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "professional_title",
                    "photo",
                    "short_bio",
                )
            }
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "location",
                )
            }
        ),

        (
            "Social Links",
            {
                "fields": (
                    "github_url",
                    "linkedin_url",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "updated_at",
                )
            }
        ),

    )

    readonly_fields = (
        "updated_at",
    )


# =====================================================
# PROJECT GALLERY INLINE
# =====================================================

class ProjectImageInline(admin.TabularInline):

    model = ProjectImage

    extra = 1

    fields = (
        "image",
        "caption",
        "order",
    )


# =====================================================
# PROJECT
# =====================================================

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "pages",
        "cost",
        "show_cost",
        "duration",
        "featured",
        "completed_date",
    )

    list_filter = (
        "featured",
        "show_cost",
        "category",
        "completed_date",
    )

    search_fields = (
        "title",
        "category",
        "description",
        "technologies",
        "features",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    list_editable = (
        "featured",
        "show_cost",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "short_description",
                    "description",
                )
            }
        ),

        (
            "Project Details",
            {
                "fields": (
                    "pages",
                    "cost",
                    "show_cost",
                    "duration",
                    "role",
                )
            }
        ),

        (
            "Technologies & Features",
            {
                "fields": (
                    "technologies",
                    "features",
                )
            }
        ),

        (
            "Challenges & Solution",
            {
                "fields": (
                    "challenges",
                    "solution",
                )
            }
        ),

        (
            "Images",
            {
                "fields": (
                    "image",
                )
            }
        ),

        (
            "Project Links",
            {
                "fields": (
                    "github_url",
                    "live_url",
                )
            }
        ),

        (
            "Status",
            {
                "fields": (
                    "featured",
                    "completed_date",
                )
            }
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            }
        ),

    )

    inlines = [
        ProjectImageInline,
    ]


# =====================================================
# PROJECT IMAGE
# =====================================================

@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "caption",
        "order",
    )

    list_filter = (
        "project",
    )

    search_fields = (
        "caption",
        "project__title",
    )


# =====================================================
# SERVICE
# =====================================================

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "starting_price",
        "featured",
        "order",
    )

    list_filter = (
        "featured",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
    )

    list_editable = (
        "starting_price",
        "featured",
        "order",
    )


# =====================================================
# SKILL
# =====================================================

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "proficiency",
        "order",
    )

    list_filter = (
        "category",
    )

    search_fields = (
        "name",
    )

    list_editable = (
        "proficiency",
        "order",
    )


# =====================================================
# CONTACT MESSAGES
# =====================================================

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "service",
        "budget",
        "is_read",
        "created_at",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "service",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )