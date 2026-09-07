from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from django.contrib import messages

from django.http import HttpResponse

from .models import (
    SiteProfile,
    Service,
    Project,
    Skill,
    ContactMessage,
)


# =====================================================
# HOME PAGE
# =====================================================

def home(request):

    # -------------------------------------------------
    # SITE PROFILE
    # -------------------------------------------------

    profile = SiteProfile.objects.first()

    # -------------------------------------------------
    # SERVICES
    # -------------------------------------------------

    services = Service.objects.all()

    # -------------------------------------------------
    # FEATURED PROJECTS
    # -------------------------------------------------

    featured_projects = Project.objects.filter(
        featured=True
    )

    # -------------------------------------------------
    # SKILLS
    # -------------------------------------------------

    skills = Skill.objects.all()

    # -------------------------------------------------
    # CONTACT FORM
    # -------------------------------------------------

    if request.method == "POST":

        name = request.POST.get(
            "name",
            ""
        ).strip()

        email = request.POST.get(
            "email",
            ""
        ).strip()

        phone = request.POST.get(
            "phone",
            ""
        ).strip()

        service = request.POST.get(
            "service",
            ""
        ).strip()

        budget = request.POST.get(
            "budget",
            ""
        ).strip()

        message = request.POST.get(
            "message",
            ""
        ).strip()

        if name and email and message:

            ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                service=service,
                budget=budget,
                message=message,
            )

            messages.success(
                request,
                "Thanks! Your message has been sent successfully."
            )

            return redirect("/#contact")

        messages.error(
            request,
            "Please fill in your name, email and message."
        )

    context = {
        "profile": profile,
        "services": services,
        "featured_projects": featured_projects,
        "skills": skills,
    }

    return render(
        request,
        "home.html",
        context
    )


# =====================================================
# ALL PROJECTS
# =====================================================

def projects(request):

    all_projects = Project.objects.all()

    context = {
        "projects": all_projects,
    }

    return render(
        request,
        "projects.html",
        context
    )


# =====================================================
# PROJECT DETAIL
# =====================================================

def project_detail(request, slug):

    project = get_object_or_404(
        Project,
        slug=slug
    )

    technologies = [
        technology.strip()
        for technology in project.technologies.split(",")
        if technology.strip()
    ]

    features = [
        feature.strip()
        for feature in project.features.splitlines()
        if feature.strip()
    ]

    context = {
        "project": project,
        "technologies": technologies,
        "features": features,
    }

    return render(
        request,
        "project_detail.html",
        context
    )



def robots_txt(request):
    sitemap_url = request.build_absolute_uri('/sitemap.xml')

    content = f"""User-agent: *
Allow: /

Sitemap: {sitemap_url}
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )