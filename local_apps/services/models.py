from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Services(models.Model):
	service = models.CharField(max_length=144)
	name = models.CharField(max_length=144)
	nombre = models.CharField(max_length=144)
	en_slug = models.CharField(max_length=144, blank=True)
	es_slug = models.CharField(max_length=144, blank=True)
	context = RichTextField(blank=True)
	descripcion = RichTextField(blank=True)
	objectives = RichTextField(blank=True)
	objetivos = RichTextField(blank=True)
	benefits = RichTextField(blank=True)
	beneficios = RichTextField(blank=True)
	technology = RichTextField(blank=True)
	tecnologia = RichTextField(blank=True)
	process = RichTextField(blank=True)
	proceso = RichTextField(blank=True)
	slogan = RichTextField(blank=True)
	eslogan = RichTextField(blank=True)
	en_checklist = RichTextField(blank=True)
	es_checklist = RichTextField(blank=True)
	projects = RichTextField(blank=True)
	related = RichTextField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	background_image = models.ImageField(
		upload_to='projects/backgrounds/',
		width_field="background_image_height",
		height_field="background_image_width",
		blank=True,
	)
	background_image_height = models.IntegerField(default=0, blank=True,)
	background_image_width = models.IntegerField(default=0, blank=True,)
	large_image = models.ImageField(
		upload_to='projects/images/large/',
		width_field="large_image_height",
		height_field="large_image_width",
		blank=True,
	)
	large_image_height = models.IntegerField(default=0, blank=True,)
	large_image_width = models.IntegerField(default=0, blank=True,)
	short_image = models.ImageField(
		upload_to='projects/images/short/',
		width_field="short_image_height",
		height_field="short_image_width",
		blank=True,
	)
	short_image_height = models.IntegerField(default=0, blank=True,)
	short_image_width = models.IntegerField(default=0, blank=True,)

	def __str__(self):
		return self.procjet
   

	def es_get_unique_slug(self):
		slug = slugify(self.es_title)
		unique_slug = slug
		num = 1
		while Services.objects.filter(es_slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def en_get_unique_slug(self):
		slug = slugify(self.en_title)
		unique_slug = slug
		num = 1
		while Services.objects.filter(en_slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug
	
	def save(self, *args, **kwargs):
		if not self.es_slug:
			self.es_slug = self.es_get_unique_slug()
		if not self.en_slug:
			self.en_slug = self.en_get_unique_slug()
		super().save()

	class Meta:
		"""# Class Meta"""
		ordering = ["-created_at"]
		verbose_name = 'Services'
		# verbose_plural_name = 'Services'