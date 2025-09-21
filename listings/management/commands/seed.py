from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **kwargs):
        sample_listings = [
            {"title": "Beachfront Villa", "description": "A luxury villa by the sea", "price_per_night": 250.00, "location": "Mombasa"},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains", "price_per_night": 150.00, "location": "Naivasha"},
            {"title": "City Apartment", "description": "Modern apartment in the city center", "price_per_night": 100.00, "location": "Nairobi"},
        ]

        for data in sample_listings:
            listing, created = Listing.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
