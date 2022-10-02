from django.urls import reverse

from wod.models.locations.human import Location


class HorizonRealm(Location):
    type = "horizon_realm"

    class Meta:
        verbose_name = "Horizon Realm"
        verbose_name_plural = "Horizon Realms"

    def get_update_url(self):
        return reverse("wod:locations:mage:update_horizonrealm", args=[str(self.id)])

    def get_heading(self):
        return "mtas_heading"
