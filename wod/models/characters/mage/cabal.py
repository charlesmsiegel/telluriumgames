from wod.models.characters.human import Group

from .utils import PRIMARY_ABILITIES, weighted_random_faction


class Cabal(Group):
    type = "cabal"

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
        faction=None,
        chantry=0,
    ):
        from wod.models.characters.mage.mage import Mage

        if faction is None:
            mage_faction = weighted_random_faction()
        else:
            mage_faction = faction
        affiliation = None
        faction = None
        subfaction = None
        if mage_faction.parent is None:
            affiliation = mage_faction
        elif mage_faction.parent.parent is None:
            faction = mage_faction
        else:
            subfaction = mage_faction
        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            random_names=random_names,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Mage,
            character_kwargs={
                "affiliation": affiliation,
                "faction": faction,
                "subfaction": subfaction,
                "backgrounds": {"chantry": chantry},
            },
        )
