from django.db import models
from django.utils.text import slugify


# =====================================================
# SITE PROFILE
# =====================================================

class SiteProfile(models.Model):

    name = models.CharField(
        max_length=150,
        default="Calvin Ochieng"
    )

    professional_title = models.CharField(
        max_length=200,
        default="Software Developer & Web Solutions"
    )

    short_bio = models.TextField(
        blank=True,
        default=(
            "I build modern websites, web applications and "
            "digital solutions that help businesses work better."
        )
    )

    photo = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True,
        help_text="Upload your professional profile photo."
    )

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    location = models.CharField(
        max_length=150,
        blank=True,
        default="Kenya"
    )

    github_url = models.URLField(
        blank=True
    )

    linkedin_url = models.URLField(
        blank=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Site Profile"
        verbose_name_plural = "Site Profile"

    def __str__(self):
        return self.name


# =====================================================
# SERVICE
# =====================================================

class Service(models.Model):

    name = models.CharField(
        max_length=200
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField(
        blank=True
    )

    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    price_label = models.CharField(
        max_length=100,
        default="Starting from"
    )

    featured = models.BooleanField(
        default=False
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = [
            "order",
            "name",
        ]

    def __str__(self):
        return self.name


# =====================================================
# PROJECT / PORTFOLIO
# =====================================================

class Project(models.Model):

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: E-Commerce, Business Website, Web Application"
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    # -------------------------------------------------
    # PROJECT INFORMATION
    # -------------------------------------------------

    pages = models.PositiveIntegerField(
        default=1,
        help_text="Number of pages/screens in the project."
    )

    cost = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Project cost in KSh."
    )

    show_cost = models.BooleanField(
        default=False,
        help_text="If enabled, the project cost will be displayed publicly."
    )

    duration = models.CharField(
        max_length=100,
        blank=True,
        help_text="Example: 4 weeks, 2 months"
    )

    role = models.CharField(
        max_length=200,
        blank=True,
        help_text="Example: Full-Stack Developer"
    )

    # -------------------------------------------------
    # TECHNOLOGIES
    # -------------------------------------------------

    technologies = models.CharField(
        max_length=500,
        help_text="Separate technologies with commas."
    )

    # -------------------------------------------------
    # PROJECT FEATURES
    # -------------------------------------------------

    features = models.TextField(
        blank=True,
        help_text="Enter one feature per line."
    )

    # -------------------------------------------------
    # CHALLENGES & SOLUTION
    # -------------------------------------------------

    challenges = models.TextField(
        blank=True
    )

    solution = models.TextField(
        blank=True
    )

    # -------------------------------------------------
    # IMAGES
    # -------------------------------------------------

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True,
        help_text="Main project image."
    )

    # -------------------------------------------------
    # LINKS
    # -------------------------------------------------

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    featured = models.BooleanField(
        default=False
    )

    completed_date = models.DateField(
        blank=True,
        null=True
    )

    # -------------------------------------------------
    # META
    # -------------------------------------------------

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "-completed_date",
            "-created_at",
            "title",
        ]

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# =====================================================
# PROJECT GALLERY
# =====================================================

class ProjectImage(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="gallery"
    )

    image = models.ImageField(
        upload_to="projects/gallery/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = [
            "order",
            "id",
        ]

    def __str__(self):
        return f"{self.project.title} - Gallery Image"


# =====================================================
# SKILL
# =====================================================

class Skill(models.Model):

    name = models.CharField(
        max_length=100
    )

    category = models.CharField(
        max_length=100,
        blank=True
    )

    proficiency = models.PositiveIntegerField(
        default=80,
        help_text="Enter a percentage between 0 and 100."
    )

    order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = [
            "order",
            "name",
        ]

    def __str__(self):
        return self.name


# =====================================================
# CONTACT MESSAGE
# =====================================================

class ContactMessage(models.Model):

    name = models.CharField(
        max_length=150
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30,
        blank=True
    )

    service = models.CharField(
        max_length=200,
        blank=True
    )

    budget = models.CharField(
        max_length=100,
        blank=True
    )

    message = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_read = models.BooleanField(
        default=False
    )

    class Meta:
        ordering = [
            "-created_at"
        ]

    def __str__(self):
        return f"{self.name} - {self.service or 'General Inquiry'}"