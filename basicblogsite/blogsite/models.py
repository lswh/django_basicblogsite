from django.db import models

# Create your models here.

# Blog Main
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __unicode__(self):
        return self.name

# Blog Post
class Blogpost(models.Model):
    blog = models.ForeignKey(Blog)
    posttitle = models.CharField(max_length=255)
    bodytext = models.TextField()
    pub_date = models.DateField()
    mood = models.CharField(max_length=30)
    tags = models.TextField()
    
    def __unicode__(self):
        return self.posttitle

# music = models.
    # latitude = models.
    # longitude = models.
    # numberofcomments = models.IntegerField()
    #social media shares
    

# To Do List
# class Todolist(models.Model):

# Event Posting	
# class Events(models.Model):

