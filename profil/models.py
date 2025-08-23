from django.db import models

class SocialMedia(models.Model):
  link = models.TextField()
  css_icon = models.CharField(max_length=20)

  def __str__(self):
    return self.css_icon

class Experience(models.Model):
  """
    example usage datefield in template:
    - March 2017 - July 2025 => {{ item.start_date|date:"F Y" }} – {{ item.end_date|date:"F Y" }}
  """

  start_year = models.DateField()
  end_year = models.DateField()
  job_title = models.CharField(max_length=50)
  job_desc = models.CharField(max_length=50)
  experience = models.TextField()

  def __str__(self):
    return self.job_title

class Education(models.Model):
  start_year = models.DateField()
  end_year = models.DateField()
  degree = models.CharField(max_length=50)
  major = models.CharField(max_length=50)
  experience = models.TextField()

  def __str__(self):
    return self.degree

class About(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(null=False, blank=False)
  address = models.TextField()
  postal_code = models.CharField(max_length=10)
  phone = models.CharField(max_length=15)
  email = models.CharField(max_length=100)
  desc = models.TextField()

  def __str__(self):
    return self.name

class Skill(models.Model):
  experience = models.TextField()
  css_icon = models.CharField(max_length=20)

  def __str__(self):
    return self.css_icon

class Interest(models.Model):
  desc = models.TextField()

  def __str__(self):
    return self.desc
