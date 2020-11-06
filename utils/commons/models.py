from django.db import models
from tinymce.models import HTMLField
from django.utils.html import mark_safe
from slugify import slugify
from django.core.exceptions import ValidationError


SOCIAL_CHOICES = (
	('android', 'android'),('apple', 'apple'),('behance', 'behance'),('dribbble', 'dribbble'),('envelope', 'email'),
	('facebook', 'facebook'),('flickr', 'flickr'),('foursquare', 'foursquare'),('google', 'google'),
	('instagram', 'instagram'),('linkedin', 'linkedin'),('meetup', 'meetup'),('pinterest', 'pinterest'),
	('reddit', 'reddit'),('rss', 'RSS'),('soundcloud', 'soundcloud'),('snapchat-ghost', 'snapchat'),
	('skype', 'skype'),('spotify', 'spotify'),('telegram', 'telegram'),('tumblr', 'tumblr'),('twitter', 'twitter'),
	('vimeo', 'vimeo'),('whatsapp', 'whatsapp'),('yahoo', 'yahoo'),('youtube-play', 'youtube'),
)

class Author(models.Model):
	name = models.CharField(max_length=128)
	designation = models.CharField(max_length=128)
	photo = models.ImageField(upload_to='images/authors')
	about = models.TextField()

	def __str__(self):
		return str(self.name)


class Post(models.Model):
	title = models.CharField(max_length=128)
	malayalam_title = models.CharField(max_length=128)
	slug = models.SlugField(unique=True,blank=True, null=True)
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
	cover_image = models.ImageField(upload_to='images/posts')
	content = HTMLField('Content')
	date = models.DateField()
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ('-published','-date')

	def __str__(self):
		return str(self.title)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    message = models.TextField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    order = models.IntegerField(unique=True)
    media = models.CharField(max_length=15,choices=SOCIAL_CHOICES)
    link = models.CharField(max_length=15)

    class Meta:
        ordering = ('order', )
        verbose_name = ('Social Media')
        verbose_name_plural = ('Social Medias')

    def __str__(self):
        return str(self.media)


class Slider(models.Model):
    subtitle = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    background = models.ImageField(upload_to='images/sliders')

    def __str__(self):
        return str(self.title)


class About(models.Model):
    description = models.TextField(default=ABOUT)
    address = models.TextField()
    email = models.EmailField(max_length=128,default="info@fresh8food.com")
    phone = models.CharField(max_length=128,default="+91 811 1818 954")
    working_hours = models.CharField(max_length=128,default="08:00AM – 06:00PM")

    class Meta:
        verbose_name = ('About')
        verbose_name_plural = ('About')

    def clean(self):
        if (About.objects.count() >= 1 and self.pk is None):
            raise ValidationError("You can only create one About. Try editing/removing one of the existing about.")

    def __str__(self):
        return str(self.email)


class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='images/testimonials')
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    order = models.IntegerField(unique=True)
    media = models.CharField(max_length=100,choices=SOCIAL_CHOICES)
    link = models.CharField(max_length=100)

    class Meta:
        ordering = ('order',)
        verbose_name = ('Social Media')
        verbose_name_plural = ('Social Medias')

    def __str__(self):
        return str(self.media)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return str(self.email)


class Page(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,blank=True, null=True)
    content = HTMLField()

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return str(self.title)


class Partner(models.Model):
    title = models.CharField(max_length=128)
    website = models.URLField(max_length=200,default="#")

    class Meta:
        ordering = ('-title',)

    def __str__(self):
        return str(self.title)
