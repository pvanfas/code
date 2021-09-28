from django.db import models
from django.utils.html import mark_safe
from django.core.exceptions import ValidationError
from uuid import uuid4
from accounts.models import User


class BaseModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid4, editable=False, blank=True)
	created = models.DateTimeField(db_index=True,auto_now_add=True)
	updated = models.DateTimeField(auto_now_add=True)
	creator = models.ForeignKey("accounts.User",blank=True,related_name="creator_%(class)s_objects",on_delete=models.CASCADE)
	is_active = models.BooleanField(default=True)

	class Meta:
		abstract = True

		
class About(models.Model):
    title = models.CharField(max_length=128)
    phone = models.CharField(max_length=128,default="+91 0000 000 000")
    description = models.TextField()
    address = models.TextField()
    email = models.EmailField(max_length=128,blank=True,null=True)
	
    class Meta:
        verbose_name = ('About')
        verbose_name_plural = ('About')

    def clean(self):
        if (About.objects.count() >= 1 and self.pk is None):
            raise ValidationError("You can only create one About. Try editing/removing one of the existing about.")

    def __str__(self):
        return str("Change Your About")
      

class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='images/testimonials')
    content = models.TextField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    order = models.IntegerField(unique=True)
    media = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('order',)
        verbose_name = ('Social Media')
        verbose_name_plural = ('Social Medias')

    def __str__(self):
        return str(self.media)


class Contact(models.Model):
    name = models.CharField(max_length=120)
    timestamp = models.DateTimeField(db_index=True,auto_now_add=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=120,blank=True,null=True)
    place = models.CharField(max_length=120,blank=True,null=True)
    message = models.TextField()

    def __str__(self):
        return str(self.name)
    

class Author(models.Model):
    name = models.CharField(max_length=128)
	email = models.EmailField(blank=True,null=True)
    photo = models.ImageField(upload_to='images/authors')
    about = models.TextField()

    def __str__(self):
        return str(self.name)
		

class Blog(models.Model):
    CATEGORY_CHOICES = (('personal', 'Personal'),('business', 'Business'))
    
    auto_id = models.PositiveIntegerField(db_index=True,unique=True)
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True,blank=True, null=True)
    
    category = models.CharField(max_length=128,choices=CATEGORY_CHOICES,default="personal")
	author = models.ForeignKey(Author,on_delete=models.CASCADE)
    
    featured_image = models.ImageField(upload_to='images/blog/featured_image/')
    content = models.TextField()
    video_url = models.URLField()
	assign_to  = models.ManyToManyField('employees.Employee')
    
    timestamp = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'web_blog'
        verbose_name = ('Blog')
        verbose_name_plural = ('Blogs')

    def __str__(self):
        return f'{self.title} by {self.author}'
	
    def delete(self, *args, **kwargs):
        storage, path = self.featured_image.storage, self.featured_image.path
        super(Blog, self).delete(*args, **kwargs)
        storage.delete(path)


class Registration(models.Model):
	GENDER_CHOICE = (('male','Male'),('female','Female'))
	
	id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
	date_added = models.DateTimeField(db_index=True,auto_now_add=True)
	full_name = models.CharField(max_length=128)
	phone_number = models.CharField(max_length=10)
	whatsapp_number = models.CharField(max_length=128,blank=True,null=True)
	place = models.CharField(max_length=128,blank=True,null=True)
	gender = models.CharField(max_length=128,choices=GENDER_CHOICE)

	class Meta:
		ordering = ('-date_added',)

	def __str__(self):
		return str(self.full_name)
