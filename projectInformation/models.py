from django.db import models

# Create your models here.

class projectData(models.Model):
    project_title = models.TextField()
    project_technologies = models.TextField()
    technical_skillset_frontend = models.TextField()
    technical_skillset_backend = models.TextField()
    technical_skillset_databases	= models.TextField()
    technical_skillset_infrastructre	= models.TextField()
    other_information_availability = models.TextField()		

    def __str__(self):
        return self.project_title																