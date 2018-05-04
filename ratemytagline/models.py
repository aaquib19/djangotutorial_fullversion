from django.db import models


class tagLine(models.Model):
    tagline = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,default="test")
    numberOfVotes = models.IntegerField(default = 0)
    def isPopular(self):
        if(self.numberOfVotes > 5):
            return True
        else:
            return False
    def __str__(self):
        return self.tagline
