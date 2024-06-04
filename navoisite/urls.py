from django.urls import path
from .views import home_view,Blogview,SinglePost,page_about_us_view,page_agents_view,page_service_box_view,page_partners_view,Services,single_service,page_turt_view,ContactView
urlpatterns = [
    path('',home_view, name="home-page"),
    path('blog/', Blogview.as_view(), name="blog-page"),
    path('blog-single-post/<slug:slug>/', SinglePost.as_view(), name='single-post'),  
    path('page-about-us/',page_about_us_view, name="about-us-page"),
    path("contact/",ContactView.as_view(),name="contact-page"),
    path('page-agents/',page_agents_view, name="agents-page"),
    path('page-service-box/',page_service_box_view, name="service-box-page"),  
    path('page-partners/',page_partners_view, name="partners-page"),
    path('page-services/',Services.as_view(), name="services-page"),
    path('page-single-service/<slug:slug>/',single_service.as_view(), name="single-service-page"), 
    path('^<path:path>/', page_turt_view, name="404-page"),
]