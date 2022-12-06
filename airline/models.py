from django.db import models

# Create your models here.
class Passenger_Info(models.Model):
    name = models.CharField(max_length = 60)
    email = models.CharField(max_length = 100)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female')
    ]
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
    phone = models.PositiveIntegerField()
    ID_CHOICES = [
        ('NIN', 'NIN'),
        ('voters', "Voter's Card"),
        ('visa', 'Visa')
    ]
    id_type = models.CharField(max_length = 10, choices = ID_CHOICES)
    passport = models.ImageField()

    def __str__(self):
        return self.name


class Flight(models.Model):
    Airline_choices = [
        ('Emirates', 'Emirates Airline'),
        ('Airik', 'Airik Airline'),
        ('Peace', 'Peace Airline'),
        ('New Benin', 'New Benin Airline'),
        ('Danfo','Danfo Airline')
    ]
    Airline = models.CharField(max_length = 30, choices = Airline_choices)
    Origin_Choices = [
        ('ABUJA','Abuja'),
        ('KANO','Kano'),
        ('LAGOS', 'Lagos'),
        ('ABIA', 'Abia')

    ]
    Flying_From = models.CharField(max_length = 50, choices = Origin_Choices)

    Destination_Choices = [
        ('ENUGU', 'Enugu'),
        ('EDO','Edo'),
        ('KOGI', 'Kogi'),
        ('KWARA','Kwara')
    ]
    Flying_To = models.CharField(max_length = 50, choices = Destination_Choices)
    Depature_date = models.DateField()

    Adult_Choices = [
        ('One','1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
        ('Six', '6'),
        ('Seven', '7'),
        ('Eight', '8'),
        ('Nine', '9')
    ]
    Adult = models.CharField (max_length = 30, choices = Adult_Choices)


    Child_Choices = [
        ('One','1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
        ('Six', '6'),
        ('Seven', '7'),
        ('Eight', '8'),
        ('Nine', '9')
    ]
    Child = models.CharField(max_length = 30, choices = Child_Choices)

    Infant_Choices = [
        ('One','1'),
        ('Two', '2'),
        ('Three', '3'),
        ('Four', '4'),
        ('Five', '5'),
        ('Six', '6'),
        ('Seven', '7'),
        ('Eight', '8'),
        ('Nine', '9')
    ]
    Infant = models.CharField(max_length = 30, choices = Infant_Choices)

    def __str__(self):
        return self.Airline


