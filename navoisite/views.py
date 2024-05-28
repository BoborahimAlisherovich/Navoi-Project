
from django.shortcuts import render
from django.contrib import messages

def home_view(request):
    return render(request, "index.html" )


def blog_view(request):
    return render(request, "blog.html")

def blog_single_post_view(request):
    return render(request, "blog-single-post.html")

def page_about_us_view(request):
    return render(request, "page-about-us.html")   

def page_contact_view(request):
    return render(request, "page-contact.html")


def page_faq_view(request):
    return render(request, "page-faq.html")


def page_agents_view(request):
    return render(request, "page-agents.html")

def page_testimonials_view(request):
    return render(request, "page-testimonials.html")


def page_service_box_view(request):
    return render(request, "page-service-box.html")

def page_partners_view(request):
    return render(request, "page-partners.html")


def page_services_view(request):
    return render(request, "page-services.html")

def page_single_service_view(request):
    return render(request, "page-single-service.html")


def page_turt_view(request):
    return render(request, "page-404.html")

def page_portfolio_list_view(request):
    return render(request, "page-portfolio-list.html")


def single_project_view(request):
    return render(request, "single-project.html")  


