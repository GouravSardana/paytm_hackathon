from django.db import models

class Patient_Detail(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adhar = models.IntegerField(null=True, blank=True)
    email= models.EmailField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.adhar

class Doctor_Detail(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    photo=models.ImageField(upload_to='pic_folder/', default='pic_folder/None/no-img.jpg')
    adhar = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.first_name