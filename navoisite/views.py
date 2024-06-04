
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import View,TemplateView,ListView
from .models import Contact,NewsArticle,Elon


def home_view(request):
    return render(request, "index.html" )


# def blog_view(request):
#     return render(request, "blog.html")

class Blogview(TemplateView):
    template_name = "blog.html"
    model = NewsArticle
    

    def get_context_data(self,*args, **kwargs):
        context = super(Blogview, self).get_context_data(*args,**kwargs)
        context['NewsArticles'] = NewsArticle.objects.all()
    
        return context
    


# def blog_single_post_view(request,pk):
#     context={"news_article":NewsArticle.objects.filter(pk=pk)}
#     # print(context)
#     return render(request, template_name="blog-single-post.html",context=context)

from django.shortcuts import get_object_or_404



class SinglePost(TemplateView):
    template_name = "blog-single-post.html"
    model = NewsArticle
    context_object_name = "NewsArticle"

    def get_context_data(self, *args, **kwargs):
        context = super(SinglePost, self).get_context_data(*args, **kwargs)
        # Get the single NewsArticle based on the id (pk) provided in the URL
        news_article_id = self.kwargs.get('pk')
        context['NewsArticle'] = get_object_or_404(NewsArticle, pk=news_article_id)
        return context

    


def page_about_us_view(request):
    return render(request, "page-about-us.html")   


class ContactView(View):
    template_name = "page-contact.html"
    # form_class = ContactForm
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    
    
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('first_name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('description', '')
        subject = request.POST.get('subjact', '')
        contact = Contact(first_name=name,email=email,description=message,subjact=subject)
        # contact["form"] = self.form_class()
       
        contact.save()
        return HttpResponseRedirect(reverse('home-page'))


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



class Services(ListView):
    template_name = "page-services.html"
    model = Elon
    context_object_name = "Elonlar"
    paginate_by = 2

    # def get_context_data(self,*args, **kwargs):
    #     context = super(Services, self).get_context_data(*args,**kwargs)
    #     # context['Elonlar'] = Elon.objects.all()
    #     return context
    


# def page_single_service_view(request):
#     return render(request, "page-single-service.html")


from django.core.paginator import Paginator

class single_service(TemplateView):
    template_name = "page-single-service.html"
    model = Elon
    context_object_name = "Elon"

    def get_context_data(self, *args, **kwargs):
        context = super(single_service, self).get_context_data(*args, **kwargs)
       
        news_article_slug = self.kwargs.get('slug')
        context['Elonlar'] = get_object_or_404(Elon, slug=news_article_slug)
        return context



def page_turt_view(request):
    return render(request, "page-404.html")

def page_portfolio_list_view(request):
    return render(request, "page-portfolio-list.html")


def single_project_view(request):
    return render(request, "single-project.html")  


