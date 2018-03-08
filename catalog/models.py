from django.db import models

# Create your models here.

class Location(models.Model):
    """
    Model representing a employee location (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a employee location (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Employee(models.Model):
    """
    Model representing a employee (but not a specific copy of a employee).
    """
    Name = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because employee can only have one department, but departments can have multiple employees
    # Department as a string rather than object because it hasn't been declared yet in the file.
    iin = models.CharField('IIN',max_length=13, help_text='13 Character <a href="https://www.iin-international.org/content/what-iin">IIN number</a>')
    location = models.ManyToManyField(Location, help_text='Select a location for this employee')
    # ManyToManyField used because location can contain many employees. Employees can cover many locations.
    # Location class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.Name
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this employee.
        """
        return reverse('employee-detail', args=[str(self.id)])

class Department(models.Model):
    """
    Model representing an department.
    """
    name = models.CharField(max_length=50)
  
    
    class Meta:
        ordering = ["name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular department instance.
        """
        return reverse('department-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '{0}, {0}'.format(self.name)