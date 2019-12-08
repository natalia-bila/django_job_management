from django.db import models
from django.shortcuts import reverse

# Create your models here.
# constants for choices

NEW = 1
APPROVED = 2
CANCELED = 3
FINISHED = 4


class Company(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.name


class Manager(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,
                                related_name='managers')
    job = models.ManyToManyField(Job)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Employee(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

class Workplace(models.Model):
    employee = models.ForeignKey(
        Employee,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='workplaces'
    )
    manager = models.ForeignKey(
        Manager,
        on_delete=models.CASCADE,
        related_name='workplaces'
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='workplaces'
    )
    status = models.IntegerField(choices = (
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELED, 'Canceled'),
        (FINISHED, 'Finished')
    ), null=True, blank=True)

    class Meta:
        unique_together = [['employee', 'status']]

class Job(models.Model):
    title = models.CharField(max_length=256)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE,
                                related_name='jobs')
    description = models.CharField(max_length=1024, null=True,
                                blank=True)
    def __str__(self):
        return '{}: {}'.format(self.company.name,self.title)

    def get_absolute_url(self):
        return reverse('management:job-detail', args=[self.id])

class WorkTime(models.Model):
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.IntegerField(choices = (
        (NEW, 'New'),
        (APPROVED, 'Approved'),
        (CANCELED, 'Canceled')
    ), default=NEW)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE,
                                 related_name='worktimes')
    workplace = models.ForeignKey(Workplace, on_delete=models.CASCADE,
                                  related_name='worktimes')