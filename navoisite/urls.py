from django.urls import path
from .views import home_view,Blogview,SinglePost,page_about_us_view,page_faq_view,page_agents_view,page_testimonials_view,page_service_box_view,page_partners_view,page_services_view,page_single_service_view,page_turt_view,page_portfolio_list_view,single_project_view,ContactView




urlpatterns = [
    path('',home_view, name="home-page"),
    
    path('blog/', Blogview.as_view(), name="blog-page"),
    # path('blog-single-post/<int:pk>',blog_single_post_view, name="single-post-page"),
    path('blog-single-post/<int:pk>/', SinglePost.as_view(), name='single-post'),    path('page-about-us/',page_about_us_view, name="about-us-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('page-faq',page_faq_view, name="faq-page"),
    path('page-agents/',page_agents_view, name="agents-page"),
    path('page-testimonials/',page_testimonials_view, name="testimonials-page"),
    path('page-service-box/',page_service_box_view, name="service-box-page"),  
    path('page-partners/',page_partners_view, name="partners-page"),
    path('page-services/',page_services_view, name="services-page"),
    path('page-single-service/',page_single_service_view, name="single-service-page"), #page_turt_view
    path('page-turt/',page_turt_view, name="404-page"),
    path('page-portfolio-list/',page_portfolio_list_view, name="portfolio-list-page"),
    path('single-project/',single_project_view, name="single-project-page"),
]