from itertools import product
from unittest import mock
from unittest.mock import Mock

from core.models import Language
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils.timezone import now
from wod.models.characters import (
    Cabal,
    Character,
    HumanCharacter,
    Instrument,
    Mage,
    MageFaction,
    MeritFlaw,
    Paradigm,
    Practice,
    Resonance,
    Rote,
)
from wod.templatetags.dots import dots


# Create your tests here.
class TestCharacter(TestCase):
    """Tests the Base Character class"""

    def setUp(self):
        self.player = User.objects.create_user(username="User1", password="12345")
        self.character = Character(player=self.player.wod_profile, name="Test")

    def test_has_concept(self):
        self.assertFalse(self.character.has_concept())
        self.character.concept = "Test"
        self.assertTrue(self.character.has_concept())

    def test_status(self):
        self.character.status = "Un"
        self.assertEqual(self.character.get_status_display(), "Unfinished")
        self.character.status = "Sub"
        self.assertEqual(self.character.get_status_display(), "Submitted")
        self.character.status = "App"
        self.assertEqual(self.character.get_status_display(), "Approved")
        self.character.status = "Ret"
        self.assertEqual(self.character.get_status_display(), "Retired")
        self.character.status = "Dec"
        self.assertEqual(self.character.get_status_display(), "Deceased")

    def test_is_minor(self):
        minor_character = Character(
            player=self.player.wod_profile, name="Test", minor=True
        )
        self.assertTrue(minor_character.minor)
        self.assertFalse(self.character.minor)

    def test_string_rep(self):
        self.assertEqual(str(self.character), "Test")

    def test_has_name(self):
        self.assertTrue(self.character.has_name())
        self.assertFalse(Character(player=self.player.wod_profile, name="").has_name())

    def test_absolute_url(self):
        self.assertEqual(
            self.character.get_absolute_url(), f"/wod/characters/{self.character.id}/"
        )

    def test_mark_character_approval(self):
        self.assertEqual(self.character.status, "Un")
        self.character.mark_complete()
        self.assertEqual(self.character.status, "Sub")
        self.character.mark_approved()
        self.assertEqual(self.character.status, "App")
        self.character.mark_retired()
        self.assertEqual(self.character.status, "Ret")
        self.character.mark_deceased()
        self.assertEqual(self.character.status, "Dec")


class TestHumanCharacter(TestCase):
    """Tests the HumanCharacter Base Class"""

    def setUp(self):
        self.user = User.objects.create_user(username="Test")
        self.character = HumanCharacter.objects.create(
            name="Testchar", player=self.user.wod_profile
        )

    def test_has_attributes(self):
        for attribute in [
            "strength",
            "dexterity",
            "stamina",
            "perception",
            "intelligence",
            "wits",
            "charisma",
            "manipulation",
            "appearance",
        ]:
            self.assertTrue(hasattr(self.character, attribute))

    def test_has_attribute_specialties(self):
        for attribute in [
            "strength",
            "dexterity",
            "stamina",
            "perception",
            "intelligence",
            "wits",
            "charisma",
            "manipulation",
            "appearance",
        ]:
            self.assertTrue(hasattr(self.character, attribute + "_specialty"))

    def test_merits_and_flaws(self):
        merit1 = MeritFlaw.objects.create(name="TestMerit1", cost=2)
        merit2 = MeritFlaw.objects.create(name="TestMerit2", cost=3)
        flaw1 = MeritFlaw.objects.create(name="TestFlaw1", cost=-3)
        flaw2 = MeritFlaw.objects.create(name="TestFlaw2", cost=-2)
        self.assertEqual(self.character.merits_and_flaws.count(), 0)
        self.character.merits_and_flaws.add(merit1)
        self.assertEqual(self.character.merits_and_flaws.count(), 1)
        self.assertEqual(self.character.merit_cost(), 2)
        self.assertEqual(self.character.flaw_cost(), 0)
        self.character.merits_and_flaws.add(merit2)
        self.assertEqual(self.character.merits_and_flaws.count(), 2)
        self.assertEqual(self.character.merit_cost(), 5)
        self.assertEqual(self.character.flaw_cost(), 0)
        self.character.merits_and_flaws.add(flaw1)
        self.assertEqual(self.character.merits_and_flaws.count(), 3)
        self.assertEqual(self.character.merit_cost(), 5)
        self.assertEqual(self.character.flaw_cost(), -3)
        self.character.merits_and_flaws.add(flaw2)
        self.assertEqual(self.character.merits_and_flaws.count(), 4)
        self.assertEqual(self.character.merit_cost(), 5)
        self.assertEqual(self.character.flaw_cost(), -5)

    def test_languages(self):
        english = Language.objects.create(name="English")
        self.assertEqual(self.character.languages.count(), 0)
        self.character.languages.add(english)
        self.assertEqual(self.character.languages.count(), 1)

    def test_archetype_options(self):
        keys = [
            "ACT",
            "BEN",
            "CON",
            "CRU",
        ]
        values = [
            "Activist",
            "Benefactor",
            "Contrary",
            "Crusader",
        ]
        for key, value in zip(keys, values):
            self.character.nature = key
            self.assertEqual(self.character.get_nature_display(), value)

    def test_random_archetypes(self):
        self.character.random_nature()
        self.character.random_demeanor()
        self.assertNotEqual(self.character.nature, "")
        self.assertNotEqual(self.character.demeanor, "")

    def test_random_attributes(self):
        self.character.random_attributes(7, 5, 3)
        triple = [
            self.character.mental_attribute_sum(),
            self.character.physical_attribute_sum(),
            self.character.social_attribute_sum(),
        ]
        triple.sort(key=lambda x: -x)
        self.assertEqual(triple, [10, 8, 6])

    def test_background_points(self):
        self.assertEqual(self.character.background_points, 5)

    def test_has_archetypes(self):
        self.assertFalse(self.character.has_archetypes())
        self.character.nature = "ACT"
        self.character.demeanor = "TRI"
        self.assertTrue(self.character.has_archetypes())

    def test_physical_attribute_sum(self):
        self.character.strength = 1
        self.character.dexterity = 2
        self.character.stamina = 3
        self.assertEqual(self.character.physical_attribute_sum(), 6)
        self.character.stamina = 2
        self.assertEqual(self.character.physical_attribute_sum(), 5)

    def test_mental_attribute_sum(self):
        self.character.perception = 1
        self.character.intelligence = 2
        self.character.wits = 3
        self.assertEqual(self.character.mental_attribute_sum(), 6)
        self.character.wits = 2
        self.assertEqual(self.character.mental_attribute_sum(), 5)

    def test_social_attribute_sum(self):
        self.character.charisma = 1
        self.character.manipulation = 2
        self.character.appearance = 3
        self.assertEqual(self.character.social_attribute_sum(), 6)
        self.character.appearance = 2
        self.assertEqual(self.character.social_attribute_sum(), 5)

    def test_add_damage(self):
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), 0)
        self.character.add_aggravated()
        self.assertEqual(self.character.current_health_levels, "AB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_lethal()
        self.assertEqual(self.character.current_health_levels, "ALB")
        self.assertEqual(self.character.get_wound_penalty(), -1)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -2)
        self.character.add_bashing()
        self.assertEqual(self.character.get_wound_penalty(), -5)
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALBBBBB")
        self.character.add_bashing()
        self.assertEqual(self.character.current_health_levels, "ALLBBBB")
        self.character.add_aggravated()
        self.assertEqual(self.character.get_wound_penalty(), -1000)

    def test_freebie_count(self):
        self.assertEqual(self.character.freebies, 15)

    def test_has_finishing_touches(self):
        self.assertFalse(self.character.has_finishing_touches())
        self.character.age = 18
        self.character.date_of_birth = now()
        self.character.hair = "Black"
        self.character.eyes = "Brown"
        self.character.ethnicity = "White"
        self.character.nationality = "American"
        self.character.height = "5'11\""
        self.character.weight = "150 lbs"
        self.character.sex = "Male"
        self.character.description = "Hardcore Asshole"
        self.assertTrue(self.character.has_finishing_touches())

    def test_has_history(self):
        self.assertFalse(self.character.has_history())
        self.character.childhood = "Was a kid, it sucked."
        self.character.history = "Got older."
        self.character.goals = "Get older still."
        self.assertTrue(self.character.has_history())

    def test_notes_field(self):
        self.assertEqual(self.character.notes, "")
        self.character.notes = "This is a note."
        self.assertNotEqual(self.character.notes, "")

    def test_get_mental_attributes(self):
        self.fail()

    def test_get_physical_attributes(self):
        self.fail()

    def test_get_social_attributes(self):
        self.fail()


def mage_setup(player):
    for i in range(5):
        Mage.objects.create(name=f"Character {i}", player=player.wod_profile)

    for i in range(15):
        Instrument.objects.create(name=f"Instrument {i}")

    for i in range(5):
        practice = Practice.objects.create(name=f"Practice {i}")
        practice.instruments.set(Instrument.objects.all())
        practice.save()

    for i in range(3):
        paradigm = Paradigm.objects.create(name=f"Paradigm {i}")
        paradigm.practices.set(Practice.objects.all())
        paradigm.save()

    trad = MageFaction.objects.create(name="Traditions")
    MageFaction.objects.create(name="Akashayana", parent=trad)

    for faction in MageFaction.objects.exclude(parent=None):
        faction.paradigms.set(Paradigm.objects.all())
        faction.practices.set(Practice.objects.all())
        faction.save()
        MageFaction.objects.create(name=f"sub-{faction.name}", parent=faction)

    for i in range(5):
        MeritFlaw.objects.create(name=f"Merit {i}", cost=i)
        MeritFlaw.objects.create(name=f"Flaw {i}", cost=-i)


class TestMage(TestCase):
    """Class that Tests Mage Characters"""

    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        self.character = Mage.objects.create(
            name="Test Character", player=self.player.wod_profile
        )
        mage_setup(self.player)

    def test_background_number(self):
        self.assertEqual(self.character.background_points, 7)

    def test_total_knowledges(self):
        self.character.academics = 1
        self.character.computer = 2
        self.character.cosmology = 4
        self.character.enigmas = 2
        self.character.science = 3
        self.assertEqual(self.character.total_knowledges(), 12)

    def test_total_talents(self):
        self.character.alertness = 1
        self.character.awareness = 2
        self.character.art = 4
        self.character.leadership = 2
        self.character.subterfuge = 3
        self.assertEqual(self.character.total_talents(), 12)

    def test_total_skills(self):
        self.character.crafts = 1
        self.character.research = 2
        self.character.stealth = 4
        self.character.technology = 2
        self.character.meditation = 3
        self.assertEqual(self.character.total_skills(), 12)

    def test_total_backgrounds(self):
        self.character.allies = 3
        self.character.avatar = 4
        self.character.resources = 1
        self.character.sanctum = 2
        self.assertEqual(self.character.total_backgrounds(), 12)
        self.character.wonder = 2
        self.assertEqual(self.character.total_backgrounds(), 14)

    def test_check_only_technocracy_backgrounds(self):
        player = User.objects.create_user(username="TechPlayer")
        technocracy = MageFaction.objects.create(name="Technocratic Union")
        itx = MageFaction.objects.create(name="Iteration X", parent=technocracy)
        tech_character = Mage.objects.create(
            name="TechCharacter",
            player=player.wod_profile,
            affiliation=technocracy,
            faction=itx,
        )
        traditions = MageFaction.objects.create(name="Traditions")
        ooh = MageFaction.objects.create(name="Order of Hermes", parent=traditions)
        trad_character = Mage.objects.create(
            name="TradCharacter",
            player=player.wod_profile,
            affiliation=traditions,
            faction=ooh,
        )
        tech_character.secret_weapons = 3
        trad_character.secret_weapons = 3
        self.assertTrue(tech_character.consistency_check())
        self.assertFalse(trad_character.consistency_check())
        tech_character.secret_weapons = 0
        trad_character.secret_weapons = 0
        tech_character.requisitions = 3
        trad_character.requisitions = 3
        self.assertTrue(tech_character.consistency_check())
        self.assertFalse(trad_character.consistency_check())

    def test_batini_no_entropy(self):
        player = User.objects.create_user(username="TechPlayer")
        disparates = MageFaction.objects.create(name="Disparates")
        batini = MageFaction.objects.create(name="Ahl-i-Batin", parent=disparates)
        batini_character = Mage.objects.create(
            name="BatiniCharacter",
            player=player.wod_profile,
            faction=batini,
            affiliation=disparates,
        )
        traditions = MageFaction.objects.create(name="Traditions")
        cult = MageFaction.objects.create(name="Cult of Ecstasy", parent=traditions)
        cult_character = Mage.objects.create(
            name="CultCharacter",
            player=player.wod_profile,
            faction=cult,
            affiliation=traditions,
        )
        batini_character.entropy = 3
        cult_character.entropy = 3
        self.assertTrue(cult_character.consistency_check())
        self.assertFalse(batini_character.consistency_check())

    def test_affinity_sphere_dot(self):
        self.character.set_affinity("For")
        self.assertEqual(self.character.forces, 1)

    def test_akashics_only_do(self):
        player = User.objects.create_user(username="TechPlayer")
        disparates = MageFaction.objects.create(name="Disparates")
        batini = MageFaction.objects.create(name="Ahl-i-Batin", parent=disparates)
        batini_character = Mage.objects.create(
            name="BatiniCharacter",
            player=player.wod_profile,
            faction=batini,
            affiliation=disparates,
        )
        traditions = MageFaction.objects.create(name="Traditions")
        akashic = MageFaction.objects.create(name="Akashayana", parent=traditions)
        akashic_character = Mage.objects.create(
            name="AkashicCharacter",
            player=player.wod_profile,
            faction=akashic,
            affiliation=traditions,
        )
        batini_character.do = 3
        akashic_character.do = 3
        akashic_character.awareness = 2
        akashic_character.meditation = 2
        akashic_character.academics = 2
        self.assertTrue(akashic_character.consistency_check())
        self.assertFalse(batini_character.consistency_check())

    def test_do_dot_requirements(self):
        player = User.objects.create_user(username="AkashicPlayer")
        akashic = MageFaction.objects.create(name="Akashayana")
        char = Mage.objects.create(player=player.wod_profile, faction=akashic)
        char.do = 3
        self.assertFalse(char.consistency_check())
        char.do = 1
        char.awareness = 2
        self.assertTrue(char.consistency_check())
        char.cosmology = 3
        self.assertTrue(char.consistency_check())
        char.do = 2
        self.assertTrue(char.consistency_check())
        char.do = 3
        self.assertFalse(char.consistency_check())

    def test_sphere_specialties(self):
        spheres = [
            "correspondence",
            "forces",
            "time",
            "life",
            "spirit",
            "matter",
            "prime",
            "mind",
            "entropy",
        ]
        for sphere in spheres:
            self.assertTrue(hasattr(self.character, f"{sphere}_specialty"))

    def test_sphere_names(self):
        spheres = [
            "correspondence",
            "forces",
            "time",
            "life",
            "spirit",
            "matter",
            "prime",
            "mind",
            "entropy",
        ]
        for sphere in spheres:
            self.assertTrue(hasattr(self.character, f"{sphere}"))
        self.assertEqual(self.character.get_corr_name_display(), "Correspondence")
        self.assertEqual(self.character.get_spirit_name_display(), "Spirit")
        self.assertEqual(self.character.get_prime_name_display(), "Prime")
        self.character.corr_name = "DAT"
        self.character.prime_name = "PU"
        self.character.spirit_name = "DS"
        self.assertEqual(self.character.get_corr_name_display(), "Data")
        self.assertEqual(
            self.character.get_spirit_name_display(), "Dimensional Science"
        )
        self.assertEqual(self.character.get_prime_name_display(), "Primal Utility")

    def test_check_affiliation_compatible(self):
        technocracy = MageFaction.objects.create(name="Technocratic Union")
        traditions = MageFaction.objects.create(name="Traditions")
        ooh = MageFaction.objects.create(name="Order of Hermes", parent=traditions)
        itx = MageFaction.objects.create(name="Iteration X", parent=technocracy)
        criamon = MageFaction.objects.create(name="House Criamon", parent=ooh)
        tmm = MageFaction.objects.create(name="Time-Motion Managers", parent=itx)

        counter = 0
        chars = {}
        for aff, fact, sub in product(
            [traditions, technocracy], [ooh, itx], [criamon, tmm]
        ):
            chars[counter] = Mage.objects.create(
                name=f"TCharacter {counter}",
                player=self.player.wod_profile,
                affiliation=aff,
                faction=fact,
                subfaction=sub,
            )
            counter += 1

        for i in [0, 7]:
            self.assertTrue(chars[i].consistency_check())
        for i in [1, 2, 3, 4, 5, 6]:
            self.assertFalse(chars[i].consistency_check())

    def test_resonance(self):
        resonance = Resonance.objects.create(name="Resonance1")
        self.character.add_resonance_dot(resonance)
        self.assertEqual(self.character.resonance.count(), 1)
        self.assertEqual(self.character.total_resonance(), 1)
        self.character.add_resonance_dot(resonance)
        self.assertEqual(self.character.resonance.count(), 1)
        self.assertEqual(self.character.total_resonance(), 2)
        resonance2 = Resonance.objects.create(name="Resonance2")
        self.assertEqual(self.character.resonance.count(), 1)
        self.character.add_resonance_dot(resonance2)
        self.assertEqual(self.character.resonance.count(), 2)
        self.assertEqual(self.character.total_resonance(), 3)

    def test_rotes(self):
        self.assertEqual(self.character.rote_points, 6)
        self.character.arete = 3
        self.character.forces = 3
        self.character.prime = 2
        self.character.life = 1
        rote = Rote.objects.create(name="Test Rote", forces=3)
        rote2 = Rote.objects.create(name="Test Rote 2", forces=4)
        rote3 = Rote.objects.create(name="Test Rote 3", life=1)
        rote4 = Rote.objects.create(name="Test Rote 4", matter=3)
        rote5 = Rote.objects.create(name="Test Rote 5", forces=3)
        self.character.learn_rote(rote)
        self.assertEqual(self.character.rotes.count(), 1)
        self.assertEqual(self.character.rote_points, 3)
        self.character.learn_rote(rote2)
        self.assertEqual(self.character.rotes.count(), 1)
        self.assertEqual(self.character.rote_points, 3)
        self.character.learn_rote(rote3)
        self.assertEqual(self.character.rotes.count(), 2)
        self.assertEqual(self.character.rote_points, 2)
        self.character.learn_rote(rote4)
        self.assertEqual(self.character.rotes.count(), 2)
        self.assertEqual(self.character.rote_points, 2)
        self.character.learn_rote(rote5)
        self.assertEqual(self.character.rotes.count(), 2)
        self.assertEqual(self.character.rote_points, 2)

    def test_starting_wp_5(self):
        self.assertGreaterEqual(self.character.willpower, 5)

    def test_random_faction(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mage.random_faction()
        self.assertTrue(mage.consistency_check())
        self.assertIsNotNone(mage.faction)
        self.assertIsNotNone(mage.affiliation)

    def test_random_essence(self):
        self.character.random_essence()
        self.assertIsNotNone(self.character.essence)

    def test_random_affinity_sphere(self):
        self.character.random_affinity()
        self.assertIsNotNone(self.character.affinity_sphere)

    def test_total_spheres(self):
        tmp = Mage()
        tmp.forces = 2
        self.assertEqual(tmp.total_spheres(), 2)
        tmp.matter = 3
        self.assertEqual(tmp.total_spheres(), 5)
        tmp.matter = 2
        tmp.life = 1
        self.assertEqual(tmp.total_spheres(), 5)

    def test_random_abilities(self):
        character = Mage.objects.create(
            name="Character", player=self.player.wod_profile
        )
        character.random_abilities(13, 9, 5)
        self.assertTrue(character.check_starting_abilities())
        for ability in character.abilities():
            self.assertLessEqual(getattr(character, ability), 3)
        character2 = Mage.objects.create(
            name="Character2", player=self.player.wod_profile
        )
        character2.random_abilities(17, 13, 9)
        self.assertFalse(character2.check_starting_abilities())
        for ability in character2.abilities():
            self.assertLessEqual(getattr(character2, ability), 3)

    def test_random_arete_and_spheres(self):
        self.character.random_arete()
        self.character.random_affinity()
        # affinity = self.character.spheres[
        #     self.character.sphere_key.index(self.character.affinity_sphere)
        # ].lower()
        self.character.random_spheres(6)
        self.assertEqual(self.character.total_spheres(), 6)

    def test_random_backgrounds(self):
        self.character.random_backgrounds()
        self.assertEqual(self.character.background_points, 0)
        self.assertEqual(self.character.total_backgrounds(), 7)

    def test_freebies(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mage.random_arete()
        self.assertEqual(mage.freebies, 15 - 4 * (mage.arete - 1))
        mage.freebies = 15
        mage.random()
        self.assertEqual(mage.freebie_cost("Strength"), 5)
        self.assertEqual(mage.freebie_cost("Awareness"), 2)
        self.assertEqual(mage.freebie_cost("Forces"), 7)
        self.assertEqual(mage.freebie_cost("Arete"), 4)
        self.assertEqual(mage.freebie_cost("Willpower"), 1)
        self.assertEqual(mage.freebie_cost("Quintessence"), 1)
        self.assertEqual(mage.freebie_cost("Allies"), 1)
        self.assertEqual(mage.freebie_cost("Merit 3"), 3)
        self.assertEqual(mage.freebie_cost("Something Unreal"), 0)
        self.assertEqual(mage.freebies, 0)

    def test_xp(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mage.random()
        self.assertEqual(mage.xp, 0)
        mage.xp = 50
        mage.save()
        self.assertEqual(mage.xp_cost("Strength"), mage.strength * 4)
        mage.alertness = 0
        mage.awareness = 1
        self.assertEqual(mage.xp_cost("Alertness"), 3)
        self.assertEqual(mage.xp_cost("Awareness"), 2 * mage.awareness)
        mage.affinity_sphere = "For"
        mage.forces = 1
        mage.life = 1
        mage.matter = 0
        mage.save()
        self.assertEqual(mage.xp_cost("Forces"), 7 * mage.forces)
        self.assertEqual(mage.xp_cost("Life"), 8 * mage.life)
        self.assertEqual(mage.xp_cost("Matter"), 10)
        self.assertEqual(mage.xp_cost("Arete"), 8 * mage.arete)
        self.assertEqual(mage.xp_cost("Willpower"), mage.willpower)
        self.assertEqual(mage.xp_cost("Something Else"), 0)
        arete = mage.arete
        mage.spend_xp("Arete")
        self.assertEqual(mage.arete, arete + 1)
        self.assertEqual(mage.spent_xp, f"arete {mage.arete}")
        self.assertEqual(mage.xp, 50 - 8 * arete)

    def test_random_focus(self):
        self.character.random_focus()
        self.assertGreaterEqual(self.character.paradigms.count(), 1)
        self.assertGreaterEqual(self.character.practices.count(), 1)
        self.assertEqual(self.character.instruments.count(), 7)

    def test_has_mage_history(self):
        self.assertFalse(self.character.has_mage_history())
        self.character.awakening = "Young"
        self.character.seekings = "Several"
        self.character.quiets = "None"
        self.character.age_of_awakening = 13
        self.character.avatar_description = "The Random Graph"
        self.assertTrue(self.character.has_mage_history())

    def test_random_faction_assigns_subfaction(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = [0.01]
        with mock.patch("random.random", mocker):
            mage.random_faction()
        self.assertIsNotNone(mage.subfaction)

    def test_random_freebies_chooses_a_flaw(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = ["Flaw 1", "Merit 2"]
        mage.freebies = 1
        with mock.patch("random.choice", mocker):
            mage.random_freebies()
        self.assertNotEqual(mage.merits_and_flaws.filter(cost__lt=0).count(), 0)

    def test_random_freebies_chooses_quintessence(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = ["quintessence"]
        mage.freebies = 1
        with mock.patch("random.choice", mocker):
            mage.random_freebies()
        self.assertEqual(mage.quintessence, 4)

    def test_spending_xp_is_logged(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mage.xp = 50
        mage.spend_xp("Strength")
        self.assertEqual(mage.spent_xp, "strength 2")
        mage.spend_xp("Alertness")
        self.assertEqual(mage.spent_xp, "strength 2, alertness 1")

    def test_focus_multiple(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = [0.01, 1, 0.01, 1]
        with mock.patch("random.random", mocker):
            mage.random_focus()
        self.assertGreaterEqual(mage.paradigms.count(), 2)
        self.assertGreaterEqual(mage.practices.count(), 2)

    def test_rejecting_too_many_flaws(self):
        mage = Mage.objects.create(
            name="Random Character", player=self.player.wod_profile
        )
        mocker = Mock()
        mocker.side_effect = ["Flaw 4", "Flaw 3", "arete", "arete", "awareness"]
        mage.freebies = 1
        with mock.patch("random.choice", mocker):
            mage.random_freebies()
        self.assertNotEqual(mage.merits_and_flaws.filter(cost__lt=0).count(), 0)
        self.assertEqual(mage.merits_and_flaws.filter(cost__lt=0).count(), 2)

    def test_get_talents(self):
        self.fail()

    def test_get_skills(self):
        self.fail()

    def test_get_knowledges(self):
        self.fail()

    def test_abilities(self):
        self.fail()

    def test_backgrounds(self):
        self.fail()

    def test_get_spheres(self):
        self.fail()

    def test_add_resonance_dot(self):
        self.fail()

    def test_total_resonance(self):
        self.fail()

    def test_learn_rote(self):
        self.fail()

    def test_check_starting_abilities(self):
        self.fail()

    def test_total_flaws(self):
        self.fail()

    def test_freebie_cost(self):
        self.fail()

    def test_random_freebies(self):
        self.fail()

    def test_xp_cost(self):
        self.fail()

    def test_random(self):
        self.fail()

    def test_spend_xp(self):
        self.fail()


class TestMageView(TestCase):
    """Manages Tests for the MageView and Template"""

    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.mage = Mage.objects.create(
            name="Test Mage", player=User.objects.get(username="Test User").wod_profile
        )

    def test_mage_status_code(self):
        """Tests that the page exists"""
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertEqual(response.status_code, 200)

    def test_mage_template(self):
        """Tests that the correct template is loaded"""
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/detail.html")


class TestMageCreateView(TestCase):
    """Manages Tests for the MageCreateView and Template"""

    def test_correct_template(self):
        response = self.client.get("/wod/characters/mage/create/")
        self.assertTemplateUsed(response, "wod/characters/mage/create.html")


class TestMageUpdateView(TestCase):
    """Manages Tests for the MageUpdateView and Template"""

    def setUp(self) -> None:
        User.objects.create_user("Test User", "test@user.com", "testpass")
        self.mage = Mage.objects.create(
            name="Test Mage", player=User.objects.get(username="Test User").wod_profile
        )

    def test_correct_template(self):
        response = self.client.get(f"/wod/characters/mage/{self.mage.id}/update/")
        self.assertTemplateUsed(response, "wod/characters/mage/update.html")


class TestSingleDetailView(TestCase):
    """Test to expand as needed that the general detail view is parsing type correctly"""

    def setUp(self) -> None:
        self.player = User.objects.create_user(username="test_player")
        self.mage = Mage.objects.create(
            name="mage_character_test", player=self.player.wod_profile
        )

    def test_correct_templates(self):
        response = self.client.get(f"/wod/characters/{self.mage.id}/")
        self.assertTemplateUsed(response, "wod/characters/mage/detail.html")

    def test_redirect(self):
        human = HumanCharacter.objects.create(
            name="test_human_character", player=self.player.wod_profile
        )
        response = self.client.get(f"/wod/characters/{human.id}/", follow=True)
        self.assertTemplateUsed(response, "wod/characters/index.html")


class TestFilters(TestCase):
    """Manage Test of custom filters"""

    def test_value(self):
        self.assertEqual(len(dots(3, maximum=5)), 5)
        self.assertEqual(len(dots(7, maximum=5)), 10)


class TestCabal(TestCase):
    """Manage Test of Cabal"""

    def setUp(self):
        self.player = User.objects.create_user(username="Player")
        mage_setup(self.player)

    def test_cabal_creation(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.members.set(Mage.objects.all())
        cabal.leader = Mage.objects.first()
        cabal.save()
        self.assertEqual(cabal.members.count(), 5)
        self.assertIsNotNone(cabal.leader)

    def test_random_cabal(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        cabal.random(5, new_characters=False)
        self.assertEqual(cabal.members.count(), 5)
        for mage in Mage.objects.all():
            self.assertIn(mage, cabal.members.all())
        cabal = Cabal.objects.create(name="Cabal 2")
        cabal.random(5, new_characters=True)
        self.assertEqual(cabal.members.count(), 5)

    def test_exception(self):
        cabal = Cabal.objects.create(name="Cabal 10")
        with self.assertRaises(ValueError):
            cabal.random(10, new_characters=False)

    def test_str(self):
        cabal = Cabal.objects.create(name="Cabal 1")
        self.assertEqual(str(cabal), "Cabal 1")


class TestMageFaction(TestCase):
    """Manage Test of Mage Faction"""

    def test_affinities(self):
        faction = MageFaction.objects.create(name="Faction 1", parent=None)
        faction.affinities = ["forces", "correspondence"]
        self.assertEqual(len(faction.affinities), 2)
        faction.affinities = faction.affinities + ["life"]
        self.assertEqual(len(faction.affinities), 3)
        faction.affinities.append("prime")
        self.assertEqual(len(faction.affinities), 4)
        faction.affinities.pop()
        self.assertEqual(len(faction.affinities), 3)

    def test_str(self):
        faction = MageFaction.objects.create(name="Faction 1", parent=None)
        self.assertEqual(str(faction), "Faction 1")


class TestPractice(TestCase):
    """Manage Test of Practice"""

    def test_abilities(self):
        practice = Practice.objects.create(name="Practice 1")
        practice.abilities = ["martial_arts", "awareness"]
        self.assertEqual(len(practice.abilities), 2)

    def test_str(self):
        practice = Practice.objects.create(name="Practice 1")
        self.assertEqual(str(practice), "Practice 1")


class TestInstrument(TestCase):
    """Manage Test of Instrument"""

    def test_str(self):
        instrument = Instrument.objects.create(name="Instrument 1")
        self.assertEqual(str(instrument), "Instrument 1")


class TestParadigm(TestCase):
    """Manage Test of Paradigm"""

    def test_str(self):
        paradigm = Paradigm.objects.create(name="Paradigm 1")
        self.assertEqual(str(paradigm), "Paradigm 1")


class TestIndexView(TestCase):
    """Manage Test of IndexView"""

    def setUp(self) -> None:
        for i in range(5):
            User.objects.create_user(username=f"Player {i}")

    def test_index_status_code(self):
        response = self.client.get("/wod/characters/")
        self.assertEqual(response.status_code, 200)

    def test_index_template(self):
        response = self.client.get("/wod/characters/")
        self.assertTemplateUsed(response, "wod/characters/index.html")

    def test_index_post(self):
        for i in range(5):
            player = User.objects.get(username=f"Player {i}")
            for j in range(3):
                Mage.objects.create(
                    name=f"Mage {5*j+i}",
                    player=player.wod_profile,
                    status=Mage.status_keys[i],
                )
        response = self.client.post("/wod/characters/")
        for i in range(15):
            self.assertContains(response, f"Mage {i}")
        for i in range(5):
            self.assertContains(response, f"Player {i}")
        for status in Character.statuses:
            self.assertContains(response, status)


class TestResonance(TestCase):
    """Manage Test of Resonance"""

    def test_str(self):
        resonance = Resonance.objects.create(name="Resonance 1")
        self.assertEqual(str(resonance), "Resonance 1")
