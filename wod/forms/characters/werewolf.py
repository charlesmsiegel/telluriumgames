from django import forms

from core.models import Language
from game.models.chronicle import Chronicle
from wod.models.characters.human import Archetype, MeritFlaw
from wod.models.characters.werewolf.garou import Gift, Tribe


class WerewolfCreationForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    concept = forms.CharField(label="Concept", max_length=100)
    chronicle = forms.ModelChoiceField(
        required=False,
        queryset=Chronicle.objects.filter(
            allowed_objects__name="Werewolf", allowed_objects__system="wod"
        ),
    )
    nature = forms.ModelChoiceField(queryset=Archetype.objects.all())
    demeanor = forms.ModelChoiceField(queryset=Archetype.objects.all())
    tribe = forms.ModelChoiceField(queryset=Tribe.objects.all())
    auspice = forms.ChoiceField(
        choices=[
            ("---", "---"),
            ("ragabash", "Ragabash"),
            ("theurge", "Theurge"),
            ("philodox", "Philodox"),
            ("galliard", "Galliard"),
            ("ahroun", "Ahroun"),
        ]
    )
    breed = forms.ChoiceField(
        choices=[
            ("---", "---"),
            ("homid", "Homid"),
            ("metis", "Metis"),
            ("lupus", "Lupus"),
        ],
    )


class WerewolfAbilitiesForm(forms.Form):
    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    primal_urge = forms.IntegerField(max_value=3, min_value=0)

    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)
    animal_ken = forms.IntegerField(max_value=3, min_value=0)
    larceny = forms.IntegerField(max_value=3, min_value=0)
    performance = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)

    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    rituals = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        kwargs["initial"] = self.char.get_abilities()
        super().__init__(*args, **kwargs)

    def assign(self):
        self.full_clean()
        for key in (
            list(self.char.get_talents().keys())
            + list(self.char.get_skills().keys())
            + list(self.char.get_knowledges().keys())
        ):
            if key == "do" and self.char.faction.name != "Akashayana":
                pass
            else:
                setattr(self.char, key, self.cleaned_data[key])


class WerewolfAdvantagesForm(forms.Form):
    contacts = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    allies = forms.IntegerField(max_value=5, min_value=0)
    ancestors = forms.IntegerField(max_value=5, min_value=0)
    fate = forms.IntegerField(max_value=5, min_value=0)
    fetish = forms.IntegerField(max_value=5, min_value=0)
    kinfolk_rating = forms.IntegerField(max_value=5, min_value=0)
    pure_breed = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    rites = forms.IntegerField(max_value=5, min_value=0)
    spirit_heritage = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        kwargs["initial"] = self.char.get_backgrounds()
        super().__init__(*args, **kwargs)

    def assign(self):
        self.full_clean()
        for key in self.char.get_backgrounds().keys():
            setattr(self.char, key, self.cleaned_data[key])


class WerewolfPowersForm(forms.Form):
    breed_gift = forms.ChoiceField(choices=[])
    auspice_gift = forms.ChoiceField(choices=[])
    tribe_gift = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")

        breed_gift_choices = [
            (x.pk, x.name)
            for x in Gift.objects.filter(rank=1).order_by("name")
            if self.char.breed in x.allowed["garou"]
        ]
        auspice_gift_choices = [
            (x.pk, x.name)
            for x in Gift.objects.filter(rank=1).order_by("name")
            if self.char.auspice in x.allowed["garou"]
        ]
        tribe_gift_choices = [
            (x.pk, x.name)
            for x in Gift.objects.filter(rank=1).order_by("name")
            if self.char.tribe.name in x.allowed["garou"]
        ]
        super().__init__(*args, **kwargs)
        self.fields["breed_gift"].choices = breed_gift_choices
        self.fields["auspice_gift"].choices = auspice_gift_choices
        self.fields["tribe_gift"].choices = tribe_gift_choices

    def assign(self):
        self.full_clean()
        gift1 = Gift.objects.get(pk=self.cleaned_data["breed_gift"])
        gift2 = Gift.objects.get(pk=self.cleaned_data["auspice_gift"])
        gift3 = Gift.objects.get(pk=self.cleaned_data["tribe_gift"])
        self.char.add_gift(gift1)
        self.char.add_gift(gift2)
        self.char.add_gift(gift3)


class WerewolfFreebieForm(forms.Form):
    strength = forms.IntegerField(max_value=5, min_value=1)
    dexterity = forms.IntegerField(max_value=5, min_value=1)
    stamina = forms.IntegerField(max_value=5, min_value=1)
    charisma = forms.IntegerField(max_value=5, min_value=1)
    manipulation = forms.IntegerField(max_value=5, min_value=1)
    appearance = forms.IntegerField(max_value=5, min_value=1)
    perception = forms.IntegerField(max_value=5, min_value=1)
    intelligence = forms.IntegerField(max_value=5, min_value=1)
    wits = forms.IntegerField(max_value=5, min_value=1)

    alertness = forms.IntegerField(max_value=3, min_value=0)
    athletics = forms.IntegerField(max_value=3, min_value=0)
    brawl = forms.IntegerField(max_value=3, min_value=0)
    empathy = forms.IntegerField(max_value=3, min_value=0)
    expression = forms.IntegerField(max_value=3, min_value=0)
    intimidation = forms.IntegerField(max_value=3, min_value=0)
    streetwise = forms.IntegerField(max_value=3, min_value=0)
    subterfuge = forms.IntegerField(max_value=3, min_value=0)
    leadership = forms.IntegerField(max_value=3, min_value=0)
    primal_urge = forms.IntegerField(max_value=3, min_value=0)
    crafts = forms.IntegerField(max_value=3, min_value=0)
    drive = forms.IntegerField(max_value=3, min_value=0)
    etiquette = forms.IntegerField(max_value=3, min_value=0)
    firearms = forms.IntegerField(max_value=3, min_value=0)
    melee = forms.IntegerField(max_value=3, min_value=0)
    stealth = forms.IntegerField(max_value=3, min_value=0)
    animal_ken = forms.IntegerField(max_value=3, min_value=0)
    larceny = forms.IntegerField(max_value=3, min_value=0)
    performance = forms.IntegerField(max_value=3, min_value=0)
    survival = forms.IntegerField(max_value=3, min_value=0)
    academics = forms.IntegerField(max_value=3, min_value=0)
    computer = forms.IntegerField(max_value=3, min_value=0)
    investigation = forms.IntegerField(max_value=3, min_value=0)
    medicine = forms.IntegerField(max_value=3, min_value=0)
    science = forms.IntegerField(max_value=3, min_value=0)
    enigmas = forms.IntegerField(max_value=3, min_value=0)
    law = forms.IntegerField(max_value=3, min_value=0)
    occult = forms.IntegerField(max_value=3, min_value=0)
    rituals = forms.IntegerField(max_value=3, min_value=0)
    technology = forms.IntegerField(max_value=3, min_value=0)

    contacts = forms.IntegerField(max_value=5, min_value=0)
    mentor = forms.IntegerField(max_value=5, min_value=0)
    allies = forms.IntegerField(max_value=5, min_value=0)
    ancestors = forms.IntegerField(max_value=5, min_value=0)
    fate = forms.IntegerField(max_value=5, min_value=0)
    fetish = forms.IntegerField(max_value=5, min_value=0)
    kinfolk_rating = forms.IntegerField(max_value=5, min_value=0)
    pure_breed = forms.IntegerField(max_value=5, min_value=0)
    resources = forms.IntegerField(max_value=5, min_value=0)
    rites = forms.IntegerField(max_value=5, min_value=0)
    spirit_heritage = forms.IntegerField(max_value=5, min_value=0)
    totem = forms.IntegerField(max_value=5, min_value=0)

    rage = forms.IntegerField(max_value=10, min_value=0)
    gnosis = forms.IntegerField(max_value=10, min_value=0)
    willpower = forms.IntegerField(max_value=10, min_value=1)

    native_language = forms.ModelChoiceField(queryset=Language.objects.all())
    languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(), required=False
    )

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")

        kwargs["initial"] = self.char.get_attributes()
        kwargs["initial"].update(self.char.get_abilities())
        kwargs["initial"].update(self.char.get_backgrounds())
        kwargs["initial"]["willpower"] = self.char.tribe.willpower
        kwargs["initial"]["rage"] = self.char.rage
        kwargs["initial"]["gnosis"] = self.char.gnosis
        kwargs["initial"]["native_language"] = Language.objects.get(name="English")

        super().__init__(*args, **kwargs)
        for attribute in self.char.get_attributes().keys():
            self.fields[attribute] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, attribute)
            )
        for ability in self.char.get_abilities().keys():
            self.fields[ability] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, ability)
            )
        for bg in self.char.get_backgrounds().keys():
            self.fields[bg] = forms.IntegerField(
                max_value=5, min_value=getattr(self.char, bg)
            )
        self.fields["willpower"] = forms.IntegerField(
            max_value=10, min_value=self.char.tribe.willpower
        )
        self.fields["rage"] = forms.IntegerField(max_value=10, min_value=self.char.rage)
        self.fields["gnosis"] = forms.IntegerField(
            max_value=10, min_value=self.char.gnosis
        )

    def total_cost_freebies(self):
        self.full_clean()
        total = 0
        attr_total = 0
        for key, value in self.char.get_attributes().items():
            attr_total += self.cleaned_data[key] - value
        total += 5 * attr_total
        abb_total = 0
        for key, value in self.char.get_abilities().items():
            abb_total += self.cleaned_data[key] - value
        total += 2 * abb_total
        bg_total = 0
        for key, value in self.char.get_backgrounds().items():
            bg_total += self.cleaned_data[key] - value
        total += 1 * bg_total
        total += self.cleaned_data["willpower"] - self.char.tribe.willpower
        total += self.cleaned_data["rage"] - self.char.rage
        total += self.cleaned_data["gnosis"] - self.char.gnosis
        mf_keys = [
            x
            for x in self.data.keys()
            if x.startswith("form-") and (x.endswith("-mf") or x.endswith("-rating"))
            if self.data[x] not in ["", "---"]
        ]
        mf_values = [int(self.data[x]) for x in mf_keys]
        mfs = dict(zip(mf_keys, mf_values))
        values = [v for k, v in mfs.items() if "-rating" in k]
        flaw_total = sum(x for x in values if x < 0)
        merit_total = sum(x for x in values if x > 0)
        if flaw_total < -7:
            return False
        total += merit_total
        total += flaw_total
        if "languages" in self.cleaned_data:
            total += self.cleaned_data["languages"].count()
        return total

    def assign(self):
        self.full_clean()
        for key in list(self.char.get_attributes().keys()):
            setattr(self.char, key, self.cleaned_data[key])
        for key in (
            list(self.char.get_talents().keys())
            + list(self.char.get_skills().keys())
            + list(self.char.get_knowledges().keys())
        ):
            setattr(self.char, key, self.cleaned_data[key])
        for key in list(self.char.get_backgrounds().keys()):
            setattr(self.char, key, self.cleaned_data[key])
        self.char.willpower = self.data["willpower"]
        self.char.rage = self.data["rage"]
        self.char.gnosis = self.data["gnosis"]
        mf_keys = [
            x
            for x in self.data.keys()
            if x.startswith("form-") and (x.endswith("-mf") or x.endswith("-rating"))
            if self.data[x] not in ["", "---"]
        ]
        mf_values = [int(self.data[x]) for x in mf_keys]
        mfs = dict(zip(mf_keys, mf_values))
        num_mf = len(mfs) // 2
        new_mfs = {}
        for i in range(num_mf):
            new_mfs[mfs[f"form-{i}-mf"]] = mfs[f"form-{i}-rating"]
        for key, value in new_mfs.items():
            self.char.add_mf(MeritFlaw.objects.get(pk=key), value)
        self.char.languages.add(self.data["native_language"])
        if "languages" in self.data:
            self.char.languages.add(*self.data["languages"])


class WerewolfDescriptionForm(forms.Form):
    age = forms.IntegerField(required=False)
    apparent_age = forms.IntegerField(required=False)
    age_of_first_change = forms.IntegerField(required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(), required=False)
    hair = forms.CharField(required=False)
    eyes = forms.CharField(required=False)
    ethnicity = forms.CharField(required=False)
    nationality = forms.CharField(required=False)
    height = forms.CharField(required=False)
    weight = forms.CharField(required=False)
    sex = forms.CharField(required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)

    childhood = forms.CharField(widget=forms.Textarea, required=False)
    history = forms.CharField(widget=forms.Textarea, required=False)
    goals = forms.CharField(widget=forms.Textarea, required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)

    first_change = forms.CharField(widget=forms.Textarea, required=False)

    def __init__(self, *args, **kwargs):
        self.char = kwargs.pop("character")
        super().__init__(*args, **kwargs)

    def complete(self):
        self.full_clean()
        if self.cleaned_data["age_of_first_change"] is None:
            return False
        if self.cleaned_data["age"] is None:
            return False
        if self.cleaned_data["apparent_age"] is None:
            return False
        if self.cleaned_data["date_of_birth"] is None:
            return False
        if self.cleaned_data["hair"] is None:
            return False
        if self.cleaned_data["eyes"] is None:
            return False
        if self.cleaned_data["ethnicity"] is None:
            return False
        if self.cleaned_data["nationality"] is None:
            return False
        if self.cleaned_data["height"] is None:
            return False
        if self.cleaned_data["weight"] is None:
            return False
        if self.cleaned_data["sex"] is None:
            return False
        if self.cleaned_data["description"] is None:
            return False
        if self.cleaned_data["childhood"] is None:
            return False
        if self.cleaned_data["history"] is None:
            return False
        if self.cleaned_data["goals"] is None:
            return False
        if self.cleaned_data["notes"] is None:
            return False
        if self.cleaned_data["first_change"] is None:
            return False
        return True
