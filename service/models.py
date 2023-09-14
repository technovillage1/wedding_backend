from django.db import models
from django.core.validators import MinValueValidator
from phonenumber_field.modelfields import PhoneNumberField
from base.models import Region, District, BaseModel
from users.models import User


class ServiceType(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Service(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    people_count = models.PositiveIntegerField(validators=[MinValueValidator(0)], blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='districts', blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    phone_number = PhoneNumberField()
    additional_phone_number = PhoneNumberField(blank=True, null=True)
    telegram = models.URLField(max_length=250, blank=True, null=True)
    instagram = models.URLField(max_length=250, blank=True, null=True)
    youtube = models.URLField(max_length=250, blank=True, null=True)
    is_confirmed = models.BooleanField(default=False, blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

    def __str__(self):
        return self.title


class AttachmentChoice(models.TextChoices):
    IMAGE = 'image', 'image'
    VIDEO = 'video', 'video'


def get_attachment_path(instance, filename):
    return f"attachments/{instance.service_id}/{filename}"


class Attachment(BaseModel):
    attachment = models.FileField(upload_to=get_attachment_path)
    attachment_type = models.CharField(choices=AttachmentChoice.choices, max_length=50, default=AttachmentChoice.IMAGE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='attachments')

    def __str__(self):
        return f"{self.service.title}"

