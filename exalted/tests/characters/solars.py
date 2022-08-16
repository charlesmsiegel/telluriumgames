from django.contrib.auth.models import User
from django.test import TestCase

from exalted.models.characters.solars import Solar, Charm
from exalted.models.characters.utils import ABILITIES


# Create your tests here.
class TestSolar(TestCase):
    def setUp(self):
        self.solar = Solar.objects.create(name="Test Solar")
        for i in range(10):
            for min_ability in range(5):
                for min_essence in range(5):
                    for ability in ABILITIES:
                        Charm.objects.create(name=f"{ability.title()} Charm {i}", ability=ability, min_ability=min_ability, min_essence=min_essence)
    
    def test_set_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.assertTrue(self.solar.set_cast("dawn"))
        self.assertTrue(self.solar.has_caste())

    def test_has_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.solar.set_cast("dawn")
        self.assertTrue(self.solar.has_caste())
        
    def test_caste_abilities(self):
        self.solar.set_cast("dawn")
        self.assertEqual(self.solar.caste_abilities, ["archery", "awareness", "brawl", "martial arts", "dodge", "melee", "resistance", "thrown", "war"])
        self.solar.set_cast("zenith")
        self.assertEqual(self.solar.caste_abilities, ["athletics", "integrity", "performance", "lore", "presence", "resistance", "survival", "war"])
        self.solar.set_cast("twilight")
        self.assertEqual(self.solar.caste_abilities, ["bureaucracy", "craft", "integrity", "investigation", "linguistics", "lore", "medicine", "occult"])
        self.solar.set_cast("night")
        self.assertEqual(self.solar.caste_abilities, ["athletics", "awareness", "dodge", "investigation", "larceny", "ride", "stealth", "socialize"])
        self.solar.set_cast("eclipse")
        self.assertEqual(self.solar.caste_abilities, ["bureaucracy", "larceny", "linguistics", "occult", "presence", "ride", "sail", "socialize"])
        
    def test_add_favored_ability(self):
        self.solar.add_favored_ability("occult")
        self.assertEqual(self.solar.favored_abilites, ["occult"])
        self.assertGreaterEqual(self.solar.occult, 1)
        
    def test_has_favored_abilities(self):
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("occult")
        self.assertGreaterEqual(self.solar.occult, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("awareness")
        self.assertGreaterEqual(self.solar.awareness, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("war")
        self.assertGreaterEqual(self.solar.war, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("athletics")
        self.assertGreaterEqual(self.solar.athletics, 1)
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.add_favored_ability("brawl")
        self.assertGreaterEqual(self.solar.brawl, 1)
        self.assertTrue(self.solar.has_favored_abilities())
        
    def test_set_supernal_ability(self):
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_cast("dawn")
        self.assertFalse(self.solar.has_supernal_ability())
        self.assertFalse(self.solar.set_supernal_ability("occult"))
        self.assertTrue(self.solar.set_supernal_ability("archery"))
        self.assertTrue(self.solar.has_supernal_ability())
        
    def test_has_supernal_ability(self):
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_cast("dawn")
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.set_supernal_ability("archery")
        self.assertTrue(self.solar.has_supernal_ability())
        
    def test_add_charm(self):
        self.fail()
        
    def test_has_charms(self):
        self.fail()
        
    def test_filter_charms(self):
        self.fail()
        
    def test_set_limit_trigger(self):
        self.fail()
        
    def test_has_limit_trigger(self):
        self.fail()
        
    def test_bonus_point_costs(self):
        self.fail()


class TestRandomSolar(TestCase):
    def setUp(self):
        self.solar = Solar.objects.create(name="Test Solar")
        for i in range(10):
            for min_ability in range(5):
                for min_essence in range(5):
                    for ability in ABILITIES:
                        Charm.objects.create(name=f"{ability.title()} Charm {i}", ability=ability, min_ability=min_ability, min_essence=min_essence)

    def test_random_caste(self):
        self.assertFalse(self.solar.has_caste())
        self.solar.random_caste()
        self.assertTrue(self.solar.has_caste())

    def test_random_favored_abilities(self):
        self.assertFalse(self.solar.has_favored_abilities())
        self.solar.random_favored_abilities()
        self.assertTrue(self.solar.has_favored_abilities())
        
    def test_random_supernal_ability(self):
        self.assertFalse(self.solar.has_supernal_ability())
        self.solar.random_supernal_ability()
        self.assertTrue(self.solar.has_supernal_ability())
        
    def test_random_charm(self):
        num_charms = self.solar.charms.count()
        self.assertTrue(self.solar.random_charm())
        self.assertEqual(self.solar.charms.count(), num_charms + 1)
        
    def test_random_charms(self):
        self.assertFalse(self.solar.has_charms())
        self.solar.random_charms()
        self.assertTrue(self.solar.has_charms())
        
    def test_random_limit_trigger(self):
        self.assertFalse(self.solar.has_limit_trigger())
        self.solar.random_limit_trigger()
        self.assertTrue(self.solar.has_limit_trigger())
        
    def test_random(self):
        xp = 0
        
        self.assertFalse(self.solar.has_name())
        self.assertFalse(self.solar.has_concept())
        self.assertFalse(self.solar.has_caste())
        self.assertFalse(self.solar.has_attributes())
        self.assertFalse(self.solar.has_abilities())
        self.assertFalse(self.solar.has_favored_abilities())
        self.assertFalse(self.solar.has_supernal_ability())
        self.assertFalse(self.solar.has_specialties())
        self.assertFalse(self.solar.has_charms())
        self.assertFalse(self.solar.has_merits())
        self.assertFalse(self.solar.has_intimacies())
        self.assertFalse(self.solar.has_limit_trigger())
        self.assertEqual(self.solar.bonus_points, 21)
        self.assertFalse(self.solar.has_finishing_touches())
        self.solar.random(xp=xp)
        self.assertTrue(self.solar.has_caste())
        self.assertTrue(self.solar.has_name())
        self.assertTrue(self.solar.has_concept())
        self.assertTrue(self.solar.has_attributes())
        self.assertTrue(self.solar.has_abilities())
        self.assertTrue(self.solar.has_favored_abilities())
        self.assertTrue(self.solar.has_supernal_ability())
        self.assertTrue(self.solar.has_specialties())
        self.assertTrue(self.solar.has_charms())
        self.assertTrue(self.solar.has_merits())
        self.assertTrue(self.solar.has_intimacies())
        self.assertTrue(self.solar.has_limit_trigger())
        self.assertEqual(self.solar.bonus_points, 0)
        self.assertTrue(self.solar.has_finishing_touches())
