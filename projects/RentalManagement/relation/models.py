from django.db import models

class OwnerRelation(models.Model):
    owner_name = models.CharField(max_length=100)
    # Assuming owner_id should be an AutoField as a primary key
    owner_id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.owner_name

class RenterRelation(models.Model):
    renter_name = models.CharField(max_length=50)
    # Use a more descriptive related_name
    owner_relation = models.ForeignKey(OwnerRelation, on_delete=models.CASCADE, related_name='renters')
    date_of_arrival = models.DateField()

    def __str__(self):
        return self.renter_name
