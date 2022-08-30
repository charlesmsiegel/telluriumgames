from wod.models.locations.human import Location
from django.urls import reverse


class HorizonRealm(Location):
    type = "horizon_realm"

    def get_update_url(self):
        return reverse("wod:locations:mage:update_horizonrealm", args=[str(self.id)])
