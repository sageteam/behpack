from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView


from product.models import Product
from product.models import ProductGroup

from blog.models import News
from slovaki.models import SlovakiWebsiteContent
from slovaki.models import SlovakiAwardsContent
from slovaki.models import SlovakiNews
from slovaki.models import SlovakiProduct

from .models import WebsiteContent
from .models import AwardsContent

# Create your views here.


class HomeView(ListView):
    template_name = "website/index.html"
    model = WebsiteContent
    context_object_name = 'websitecontent_list'
    #additional information
    title = 'خانه'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['slovaki_website_content'] = SlovakiWebsiteContent.objects.all()
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['awards'] = AwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['groups'] = ProductGroup.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        return context


class AboutView(ListView):
    template_name = 'website/about.html'
    model = WebsiteContent
    context_object_name = 'websitecontent_list'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['slovaki_website_content'] = SlovakiWebsiteContent.objects.all()
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['awards'] = AwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['groups'] = ProductGroup.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        return context


class ContactView(ListView):
    template_name = 'website/contact.html'

    #additional information
    title = 'تماس با ما'
    model = WebsiteContent
    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['slovaki_website_content'] = SlovakiWebsiteContent.objects.all()
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['awards'] = AwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['groups'] = ProductGroup.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        return context

class AwardsView(ListView):
    template_name = 'website/awards.html'
    model = AwardsContent
    context_object_name = 'awards'

    def get_context_data(self, **kwargs):
        context = super(AwardsView, self).get_context_data(**kwargs)
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['groups'] = ProductGroup.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        return context
    

class BlogView(ListView):
    template_name = 'website/posts.html'
    model = News
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['groups'] = ProductGroup.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        return context



class BlogDetailView(DetailView):
    template_name = 'website/post.html'
    model = News
    context_object_name = 'post'


class SlovakiBlogDetailView(DetailView):
    template_name = 'website/post.html'
    model = SlovakiNews
    context_object_name = 'post'


class ProductView(ListView):
    template_name = 'website/products.html'
    model = Product
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['slovaki_awards'] = SlovakiAwardsContent.objects.all()
        context['awards'] = AwardsContent.objects.all()
        context['products'] = Product.objects.all()
        context['slovaki_products'] = SlovakiProduct.objects.all()
        context['news'] = News.objects.all()
        context['slovaki_news'] = SlovakiNews.objects.all()
        
        return context


class ProductDetailView(DetailView):
    template_name = 'website/product.html'
    model = Product
    context_object_name = 'product'
    #additional information
    title = 'لیست محصولات'


class SlovakiProductDetailView(DetailView):
    template_name = 'website/product.html'
    model = SlovakiProduct
    context_object_name = 'product'
    #additional information
    title = 'لیست محصولات'
