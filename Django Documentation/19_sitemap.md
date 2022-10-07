## The sitemap framework
A sitemap is an XML file on your website that tells search-engine indexers how frequently your pages change and how “important” certain pages are in relation to other pages on your site. This information helps search engines index your site.

To install the sitemap app, follow these steps:

- Add ```django.contrib.sitemaps``` to your ```INSTALLED_APPS``` setting.
- Make sure your TEMPLATES setting contains a DjangoTemplates backend whose APP_DIRS options is set to True. It’s in there by default, so you’ll only need to change this if you’ve changed that setting.
- Make sure you’ve installed the sites framework and add Django sitemaps to installed apps
    ```
    INSTALLED_APPS = [
        ...
        'django.contrib.sites',
        'django.contrib.sitemaps',
    ]
    ```
- Add site id
    ```
    SITE_ID = 1
    ```
- Create a Django ```sitemap.py``` file
    ```
    from django.contrib.sitemaps import Sitemap
    from django.urls import reverse
    
    from products.models import Product

    class StaticSitemap(Sitemap):
        changefreq = "yearly"
        priority = 1
        protocol = 'https'
    
        def items(self):
            return [
                'web:index',
                'web:about',
                'web:products',
                'web:updates',
                'web:careers',
                'web:contact'
            ]
    
        def location(self, item):
            return reverse(item)
    
    
    class FeaturedProductSitemap(Sitemap):
        changefreq = "weekly"
        priority = 0.80
        protocol = 'https'
    
        def items(self):
            return Product.objects.filter(is_featured=True)
    
        def lastmod(self, obj):
            return obj.pub_date
    
        def location(self,obj):
            return '/product/%s' % (obj.slug)
    ```
- Add the Django sitemap URL
    ```
    from django.contrib.sitemaps.views import sitemap
    from web.sitemaps import StaticSitemap, FeaturedProductSitemap
    from django.views.generic import TemplateView
    
    sitemaps = {
        'static':StaticSitemap,
        'featured_products' : FeaturedProductSitemap,
    }
    urlpatterns = (
        [
            ...
            path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
        ]
        + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    )
    ```
- The Django sitemap is now available at http://127.0.0.1:8000/sitemap.xml
