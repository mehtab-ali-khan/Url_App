from django.core.management.base import BaseCommand

from api.models import Url


class Command(BaseCommand):
    help = "Seed URLs"

    def handle(self, *args, **kwargs):
        TOTAL_URLS = 10

        base_urls = [
            "https://google.com/search?q=",
            "https://youtube.com/watch?v=",
            "https://wikipedia.org/wiki/",
            "https://amazon.com/dp/",
        ]

        urls_to_create = []

        for i in range(TOTAL_URLS):
            base = base_urls[i % len(base_urls)]
            unique_url = f"{base}{i}"
            urls_to_create.append(Url(url=unique_url))

        Url.objects.bulk_create(urls_to_create)

        self.stdout.write(self.style.SUCCESS(f"{TOTAL_URLS} URLs inserted"))
