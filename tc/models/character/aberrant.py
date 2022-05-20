from django.db import models

from tc.models.character.human import Edge, Human


# Create your models here.
class Aberrant(Human):
    type = "aberrant"

    mega_intellect = models.IntegerField(default=0)
    mega_cunning = models.IntegerField(default=0)
    mega_resolve = models.IntegerField(default=0)
    mega_might = models.IntegerField(default=0)
    mega_dexterity = models.IntegerField(default=0)
    mega_stamina = models.IntegerField(default=0)
    mega_presence = models.IntegerField(default=0)
    mega_manipulation = models.IntegerField(default=0)
    mega_composure = models.IntegerField(default=0)

    def add_mega_attribute(self, attribute):
        pass

    def total_megaedges(self):
        pass

    def add_quantum(self):
        pass

    def update_quantum_points(self):
        pass
        
        # self.fail("Quantum of 1")
        # self.fail("One dot in favored approach")
        # self.fail("Either 1 dot of Fame or 1 dot of Alternate Identity Edge")
        # self.fail("150 XP")
        # self.fail("Check spend_xp?")


class MegaEdge(Edge):
    type = "megaedge"
