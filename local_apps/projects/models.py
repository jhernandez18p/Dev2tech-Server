from django.db import models
from django.utils.text import slugify

# Create your models here.
class Procjets(models.Model):
	procjet = models.CharField(max_length=144)
	name = models.CharField(max_length=144)
	nombre = models.CharField(max_length=144)
	en_slug = models.CharField(max_length=144, blank=True)
	es_slug = models.CharField(max_length=144, blank=True)
	context = models.TextField()
	descripcion = models.TextField()
	requirements = models.TextField()
	requisito = models.TextField()
	objectives = models.TextField()
	objetivos = models.TextField()
	benefits = models.TextField()
	beneficios = models.TextField()
	technology = models.TextField()
	tecnologia = models.TextField()
	process = models.TextField()
	proceso = models.TextField()
	result = models.TextField()
	resultado = models.TextField()
	# customer = models.TextField()
	# cliente = models.TextField()
	# customer_testimonial = models.TextField()
	# cliente_testimonio = models.TextField()
	started = models.TextField()
	iniciado = models.TextField()
	finished = models.TextField()
	finalizado = models.TextField()
	slogan = models.TextField()
	eslogan = models.TextField()
	state = models.TextField()
	estado = models.TextField()
	service = models.TextField()
	servicio = models.TextField()
	business_type = models.TextField()
	tipo_empresa = models.TextField()
	en_checklist = models.TextField()
	es_checklist = models.TextField()
	technologies = models.TextField()
	screenshots = models.TextField()
	related = models.TextField()
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
		while Procjets.objects.filter(es_slug=unique_slug).exists():
			unique_slug = '{}-{}'.format(slug, num)
			num += 1
		return unique_slug

	def en_get_unique_slug(self):
		slug = slugify(self.en_title)
		unique_slug = slug
		num = 1
		while Procjets.objects.filter(en_slug=unique_slug).exists():
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