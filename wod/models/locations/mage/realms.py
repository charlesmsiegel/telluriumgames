from django.urls import reverse

from wod.models.locations.human import Location


class HorizonRealm(Location):
    type = "horizon_realm"

    def get_update_url(self):
        return reverse("wod:locations:mage:update_horizonrealm", args=[str(self.id)])

    def get_heading(self):
        return "mtas_heading"
