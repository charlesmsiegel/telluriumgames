from django.urls import reverse

from wod.models.characters.human import Group


class Motley(Group):
    type = "motley"

    def get_heading(self):
        return "ctd_heading"

    def random(
        self,
        num_chars=None,
        new_characters=True,
        random_names=True,
        freebies=15,
        xp=0,
        user=None,
    ):
        from wod.models.characters.changeling.changeling import Changeling

        super().random(
            num_chars=num_chars,
            new_characters=new_characters,
            random_names=random_names,
            freebies=freebies,
            xp=xp,
            user=user,
            member_type=Changeling,
            character_kwargs={},
        )

    def get_update_url(self):
        return reverse(
            "wod:characters:changeling:update_motley", kwargs={"pk": self.pk}
        )
