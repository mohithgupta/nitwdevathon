from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf=models.FileField(upload_to='books/pdfs/')

    def _str_(self):
        return self.title
    def delete(self,*args,**kwargs):
        self.pdf.delete()
        super().delete(*args,**kwargs)

