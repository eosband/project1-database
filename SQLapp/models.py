from django.db import models
from django.conf import settings
from decimal import Decimal
import urllib
import json

# Create your models here.

class User(models.Model):
    display_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    def __str__(self):
        return self.username + " (id: " + str(self.id) + ")"

class Location(models.Model):
    userID = models.CharField(max_length=20, null=True)
    place_title = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5, null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, editable=False)
    longitude = models.DecimalField(max_digits=18, decimal_places=10, null=True, editable=False)

    def __str__(self):
        return "title: " + str(self.place_title) + " (id:" + str(self.userID) + ")"

    def save(self, *args, **kwargs):
        # args and kwargs had to be added to fix "force_insert" error when POSTing
        location = "%s, %s, %s %s" % (self.address, self.city, self.state, self.zip_code)
        # if (not self.latitude or not self.longitude)
        # the above is commented out for testing purposes
        self.latitude, self.longitude = self.geocode(location)
        super(Location, self).save()

    def geocode(self, location):
        location = urllib.parse.quote_plus(location)
        print(location)
        request = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (location, settings.GOOGLE_API_KEY)
        response = urllib.request.urlopen(request)
        data = json.loads(response.read().decode('utf8'))

        if data['status'] == 'OK':
            lat = data['results'][0]['geometry']['location']['lat']
            lng = data['results'][0]['geometry']['location']['lng']

            return Decimal(lat), Decimal(lng)
