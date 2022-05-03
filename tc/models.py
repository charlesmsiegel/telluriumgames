import math
import random
from django.db import models
from accounts.models import TCProfile

# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MegaAttribute(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    specialties = models.JSONField(null=True)

    def __str__(self):
        return self.name


class Trick(models.Model):
    name = models.CharField(max_length=100)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(default="")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Edge(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(null=True)
    description = models.TextField(default="")
    prereq_attributes = models.ManyToManyField("AttributePrereq", blank=True)
    prereq_skills = models.ManyToManyField("SkillPrereq", blank=True)
    prereq_path_rating = models.IntegerField(default=0)
    prereq_edges = models.ManyToManyField(
        "EdgePrereq", blank=True, related_name="prereq_to"
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class EnhancedEdge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    prereq_edges = models.ManyToManyField("EdgePrereq", blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class MegaEdge(Edge):
    prereq_megaatt = models.ManyToManyField("MegaAttributePrereq", blank=True)
    prereq_quantum = models.IntegerField(default=0)  # TODO: Ensure that MegaEdges with Dots works: if -1 then DOTS
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name


class Path(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    skills = models.ManyToManyField(Skill, blank=True)
    edges = models.ManyToManyField(Edge, blank=True)
    type = models.CharField(
        max_length=3, choices=[("ORI", "Origin"), ("ROL", "Role"), ("SOC", "Society"),]
    )

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PathConnection(models.Model):
    name = models.CharField(max_length=100)
    path = models.ForeignKey("Path", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class PathConnectionRating(models.Model):
    character = models.ForeignKey(
        "Aberrant", on_delete=models.CASCADE, blank=True, null=True
    )
    path = models.ForeignKey("Path", null=True, blank=True, on_delete=models.CASCADE)
    path_connection = models.ForeignKey(
        "PathConnection", on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.character.name}, {self.path_connection}: {self.rating}"


class Tag(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(null=True)
    description = models.TextField(default="")
    permitted_powers = models.ManyToManyField("Power", blank=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# TODO Power Suites which consist of powers and sets of tags?
# TODO Increase chance of multiple dots in a single quantum power (increase odds of favoring things that already exist)
# TODO: Reduced Cost tag can be bought multiple times up to Cost for Power
# TODO: Sort lists alphabetically for display
# TODO: Make low ratings more probable than high ratings for edges and tags, maybe for each rating r duplicate it GCD(ratings)/r times?
class Power(models.Model):
    name = models.CharField(max_length=100)
    quantum_minimum = models.IntegerField(default=0)
    action = models.CharField(
        max_length=3, choices=[("REF", "Reflexive"), ("ORD", "Ordinary"),]
    )
    cost = models.IntegerField(default=0)
    dice_pool = models.CharField(default="", max_length=100)
    range = models.CharField(
        max_length=3,
        choices=[
            ("PER", "Personal"),
            ("CLO", "Close"),
            ("SHO", "Short"),
            ("MED", "Medium"),
            ("LON", "Long"),
            ("EXT", "Extreme"),
            ("VIS", "Visual"),
        ],
    )
    duration = models.CharField(
        max_length=4,
        choices=[
            ("INST", "Instantaneous"),
            ("CONC", "Concentration"),
            ("MAIN", "Maintained"),
            ("CONT", "Continuous"),
        ],
    )
    description = models.TextField(default="")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Option(models.Model):
    power = models.ForeignKey(Power, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="")


class Transformation(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(
        max_length=3,
        choices=[("LOW", "Low Level"), ("MED", "Medium Level"), ("HIG", "High"),],
    )
    description = models.TextField(default="")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Aberrant(models.Model):
    name = models.CharField(max_length=100, default="")
    player = models.ForeignKey(
        TCProfile,
        on_delete=models.CASCADE,
        related_name="characters",
        blank=True,
        null=True,
    )
    concept = models.CharField(max_length=100, default="")

    short_term_aspiration_1 = models.TextField(default="")
    short_term_aspiration_2 = models.TextField(default="")
    long_term_aspiration = models.TextField(default="")

    paths = models.ManyToManyField(
        "PathConnection", blank=True, related_name="characters_on_path", through=PathConnectionRating
    )

    attributes = models.ManyToManyField(
        Attribute, through="AttributeRating", blank=True
    )
    favored_approach = models.CharField(
        max_length=3,
        choices=[("FOR", "Force"), ("FIN", "Finesse"), ("RES", "Resilience"),],
        default="FOR",
    )
    megaattributes = models.ManyToManyField(
        MegaAttribute, through="MegaAttributeRating", blank=True
    )
    skills = models.ManyToManyField(Skill, through="SkillRating", blank=True)
    edges = models.ManyToManyField(
        Edge, related_name="edges_of", through="EdgeRating", blank=True
    )
    enhanced_edges = models.ManyToManyField(
        EnhancedEdge, related_name="edges_of", blank=True
    )

    moment_of_inspiration = models.TextField(default="")
    defense = models.IntegerField(default=1)
    bruised_levels = models.IntegerField(default=2)
    injured_levels = models.IntegerField(default=2)
    maimed_levels = models.IntegerField(default=1)

    quantum = models.IntegerField(default=1)
    quantum_points = models.IntegerField(default=10)
    transcendence = models.IntegerField(default=0)
    flux = models.IntegerField(default=0)
    transformations = models.ManyToManyField(Transformation, blank=True)
    megaedges = models.ManyToManyField(
        "MegaEdge", related_name="megaedges_of", through="MegaEdgeRating", blank=True
    )
    powers = models.ManyToManyField(Power, through="PowerRating", blank=True)

    xp = models.IntegerField(default=0)
    xp_spending = models.TextField(default="")

    class Meta:
        ordering = ('name',)

    def setup(self):
        for att in Attribute.objects.all():
            AttributeRating.objects.create(
                attribute=att, character=self, rating=1,
            )
        for matt in MegaAttribute.objects.all():
            MegaAttributeRating.objects.create(
                megaattribute=matt, character=self, rating=0
            )
        for skill in Skill.objects.all():
            SkillRating.objects.create(
                skill=skill, character=self, rating=0,
            )

    def random_concept(self, name=None):
        if name is None:
            self.name = "Test 1"
        else:
            self.name = name
        self.concept = "Nova Character"

    def random_aspirations(self):
        self.short_term_aspiration_1 = "Short Term 1"
        self.short_term_aspiration_2 = "Short Term 2"
        self.long_term_aspiration = "Long Term"
        self.save()

    def random_paths(self):
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="ORI")))
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="ROL")))
        self.add_random_path_dot(sublist=list(Path.objects.filter(type="SOC")))
        for path in PathConnectionRating.objects.filter(character=self):
            skills = list(path.path.skills.all())
            skills = list(SkillRating.objects.filter(character=self, skill__in=skills))
            count = 0
            while count < 3:
                if self.add_random_skill(sublist=skills):
                    count += 1
            total_diff = 2
            while total_diff > 0:
                # print(total_diff)
                result = self.add_random_edge(sublist=list(path.path.edges.all()))
                if result != False:
                    diff, (edge, rating) = result
                    diff = int(diff)
                    if diff <= total_diff:
                        self.apply_edge(edge, rating)
                        total_diff -= diff

    def random_skills(self):
        count = 0
        while count < 6:
            if self.add_random_skill():
                count += 1
        high_skills = SkillRating.objects.filter(character=self, rating__gte=3)
        for skill_rating in high_skills:
            for _ in range(skill_rating.rating - 2):
                self.add_random_skill_trick(sublist=[skill_rating])
        self.add_random_skill_trick()
        for skill in SkillRating.objects.filter(character=self, rating__gte=3):
            self.add_random_skill_specialty(sublist=[skill])

    def random_attributes(self):
        types = ["physical", "mental", "social"]
        random.shuffle(types)
        point_dict = {
            types[0]: 6,
            types[1]: 4,
            types[2]: 2,
        }
        physical = [
            AttributeRating.objects.get(attribute__name="Might", character=self),
            AttributeRating.objects.get(attribute__name="Dexterity", character=self),
            AttributeRating.objects.get(attribute__name="Stamina", character=self),
        ]
        mental = [
            AttributeRating.objects.get(attribute__name="Intellect", character=self),
            AttributeRating.objects.get(attribute__name="Cunning", character=self),
            AttributeRating.objects.get(attribute__name="Resolve", character=self),
        ]
        social = [
            AttributeRating.objects.get(attribute__name="Presence", character=self),
            AttributeRating.objects.get(attribute__name="Manipulation", character=self),
            AttributeRating.objects.get(attribute__name="Composure", character=self),
        ]
        force = [
            AttributeRating.objects.get(attribute__name="Intellect", character=self),
            AttributeRating.objects.get(attribute__name="Might", character=self),
            AttributeRating.objects.get(attribute__name="Presence", character=self),
        ]
        finesse = [
            AttributeRating.objects.get(attribute__name="Cunning", character=self),
            AttributeRating.objects.get(attribute__name="Dexterity", character=self),
            AttributeRating.objects.get(attribute__name="Manipulation", character=self),
        ]
        resilience = [
            AttributeRating.objects.get(attribute__name="Resolve", character=self),
            AttributeRating.objects.get(attribute__name="Stamina", character=self),
            AttributeRating.objects.get(attribute__name="Composure", character=self),
        ]
        while sum([x.rating for x in physical]) < point_dict["physical"] + 3:
            self.add_random_attribute(sublist=physical)
        while sum([x.rating for x in mental]) < point_dict["mental"] + 3:
            self.add_random_attribute(sublist=mental)
        while sum([x.rating for x in social]) < point_dict["social"] + 3:
            self.add_random_attribute(sublist=social)

        approach = random.choice([force, finesse, resilience])
        for att in approach:
            if att.rating < 5:
                self.add_random_attribute(sublist=[att])
            else:
                for arena in [physical, social, mental]:
                    if att in arena:
                        self.add_random_attribute(
                            sublist=[x for x in arena if att != x]
                        )

    def apply_template(self, xp=150):
        force = [
            AttributeRating.objects.get(attribute__name="Intellect", character=self),
            AttributeRating.objects.get(attribute__name="Might", character=self),
            AttributeRating.objects.get(attribute__name="Presence", character=self),
        ]
        finesse = [
            AttributeRating.objects.get(attribute__name="Cunning", character=self),
            AttributeRating.objects.get(attribute__name="Dexterity", character=self),
            AttributeRating.objects.get(attribute__name="Manipulation", character=self),
        ]
        resilience = [
            AttributeRating.objects.get(attribute__name="Resolve", character=self),
            AttributeRating.objects.get(attribute__name="Stamina", character=self),
            AttributeRating.objects.get(attribute__name="Composure", character=self),
        ]
        approach = []
        if self.favored_approach == "FOR":
            approach = force
        elif self.favored_approach == "FIN":
            approach = finesse
        elif self.favored_approach == "RES":
            approach = resilience
        self.add_random_attribute(sublist=approach)

        total_diff = 1
        while total_diff > 0:
            result = self.add_random_edge(sublist=Edge.objects.filter(name__in=["Fame", "Alternate Identity"]))
            if result != False:
                diff, (edge, rating) = result
                diff = int(diff)
                if diff <= total_diff:
                    self.apply_edge(edge, rating)
                    total_diff -= diff
        
        self.xp = xp

    def final_touches(self):
        self.spend_xp()
        stamina = AttributeRating.objects.get(
            character=self, attribute__name="Stamina"
        )
        if stamina.rating >= 3:
            self.injured_levels += 1
        if stamina.rating >= 5:
            self.bruised_levels += 1
        self.defense = 1

    def spend_xp(self):
        costs = {
            "attribute": 10,
            "edge": 3,
            "path edge": 2,
            "enhanced edge": 6,
            "skill": 5,
            "skill trick": 3,
            "specialty": 3,
            "path": 18,
            "mega attribute": 6,
            "mega edge": 6,
            "power tag": 12,
            "quantum": 16,
            "quantum power": 6,
        }
        cost_options = []
        cost_options.extend(["attribute"] * 1)
        cost_options.extend(["edge"] * 1)
        cost_options.extend(["path edge"] * 1)
        cost_options.extend(["enhanced edge"] * 1)
        cost_options.extend(["skill"] * 1)
        cost_options.extend(["skill trick"] * 1)
        cost_options.extend(["specialty"] * 1)
        cost_options.extend(["path"] * 1)
        cost_options.extend(["mega attribute"] * 3)
        cost_options.extend(["mega edge"] * 5)
        cost_options.extend(["power tag"] * 10)
        cost_options.extend(["quantum"] * 5)
        cost_options.extend(["quantum power"] * 15)
        while self.xp > 10:
            if random.random() < 0.15:
                transcendence = True
            else:
                transcendence = False
            choice = random.choice(cost_options)
            chance = random.random()
            cost = costs[choice]
            chosen = None
            if self.transformations.count() < self.quantum * 2:
                if chance < 0.05:
                    transformations = list(Transformation.objects.filter(level="MED"))
                    transformations = [
                        x
                        for x in transformations
                        if x not in self.transformations.all()
                    ]
                    chosen = random.choice(transformations)
                    cost -= 6
                elif chance < 0.15:
                    transformations = list(Transformation.objects.filter(level="LOW"))
                    transformations = [
                        x
                        for x in transformations
                        if x not in self.transformations.all()
                    ]
                    chosen = random.choice(transformations)
                    cost -= 3
            if choice == "attribute":
                if self.add_random_attribute():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Attribute ({cost}), "
            elif choice == "edge":
                result = self.add_random_edge()
                if result != False:
                    diff, (edge, rating) = result
                    diff = int(diff)
                    cost *= diff
                    if cost <= self.xp:
                        self.pay_cost(cost, chosen)
                        self.apply_edge(edge, rating)
                        self.xp_spending = self.xp_spending + f"Edge ({cost}), "
            elif choice == "path edge":
                path_edges = []
                for pathconnrating in PathConnectionRating.objects.filter(character=self):
                    path_edges.extend(list(pathconnrating.path.edges.all()))
                result = self.add_random_edge(sublist=path_edges)
                if result != False:
                    diff, (edge, rating) = result
                    diff = int(diff)
                    cost *= diff
                    if cost <= self.xp:
                        self.pay_cost(cost, chosen)
                        self.apply_edge(edge, rating)
                        self.xp_spending = self.xp_spending + f"Path Edge ({cost}), "
            elif choice == "enhanced edge":
                if self.add_random_enhanced_edge():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Enhanced Edge ({cost}), "
            elif choice == "skill":
                if self.add_random_skill():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Skill ({cost}), "
            elif choice == "skill trick":
                if self.add_random_skill_trick():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Skill Trick ({cost}), "
            elif choice == "specialty":
                if self.add_random_skill_specialty():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Skill Specialty ({cost}), "
            elif choice == "path":
                self.add_random_path_dot()
                self.pay_cost(cost, chosen)
                self.xp_spending = self.xp_spending + f"Path Dot ({cost}), "
            elif choice == "mega attribute":
                if not transcendence:
                    cost *= 2
                if self.xp >= cost:
                    if self.add_random_mega_attribute():
                        self.pay_cost(cost, chosen)
                        self.xp_spending = self.xp_spending + f"Mega Attribute ({cost}), "
                    if transcendence:
                        self.add_transcendance()
            elif choice == "mega edge":
                diff, (edge, rating) = self.add_random_mega_edge()
                diff = int(diff)
                cost *= diff
                if not transcendence:
                    cost *= 2
                if cost <= self.xp:
                    self.apply_mega_edge(edge, rating)
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Mega Edge ({cost}), "
                    if transcendence:
                        self.add_transcendance()
            elif choice == "power tag":
                result = self.add_random_power_tag()
                if result != False:
                    diff, (power, tag, rating) = result
                    diff = int(diff)
                    cost *= diff
                    if cost <= self.xp:
                        self.apply_power_tag(power, tag, rating)
                        self.pay_cost(cost, chosen)
                        self.xp_spending = self.xp_spending + f"Power Tag ({cost}), "
                        if transcendence:
                            self.add_transcendance()
            elif choice == "quantum":
                if self.add_quantum():
                    self.pay_cost(cost, chosen)
                    self.xp_spending = self.xp_spending + f"Quantum ({cost}), "
            elif choice == "quantum power":
                if not transcendence:
                    cost *= 2
                if self.xp >= cost:
                    if self.add_random_power():
                        self.pay_cost(cost, chosen)
                        self.xp_spending = self.xp_spending + f"Power ({cost}), "
                    if transcendence:
                        self.add_transcendance()
            cost_options = [x for x in cost_options if costs[x] <= self.xp]
            self.save()
        self.xp_spending = self.xp_spending[:-2]
        self.save()

    def random(self, name=None, xp=150):
        self.setup()
        self.random_concept(name=name)
        self.random_aspirations()
        self.random_paths()
        self.random_skills()
        self.random_attributes()
        self.apply_template(xp=xp)
        self.final_touches()
        self.compute_quantum_points()
        self.mega_attribute_cleanup()
        self.save()

    def mega_attribute_cleanup(self):
        mega_int_edges = [
            "Iron Will",
            "Lightning Calculator",
            "Photographic Memory",
            "Speed Reading",
        ]
        mega_int_edges = [Edge.objects.get(name=x) for x in mega_int_edges]
        mega_cun_edges = ["Keen Sense"]
        mega_cun_edges = [Edge.objects.get(name=x) for x in mega_cun_edges]
        mega_man_edges = ["Animal Ken", "Skilled Liar", "Striking", "Wealth"]
        mega_man_edges = [Edge.objects.get(name=x) for x in mega_man_edges]
        mega_com_edges = ["Always Prepared", "Covert", "Danger Sense", "Iron Will"]
        mega_com_edges = [Edge.objects.get(name=x) for x in mega_com_edges]
        megaint = MegaAttributeRating.objects.get(
            character=self, megaattribute__name="Mega-Intellect"
        ).rating
        while megaint > 0:
            diff, (edge, rating) = self.add_random_edge(sublist=mega_int_edges)
            diff = int(diff)
            if diff <= megaint:
                megaint -= diff
                self.apply_edge(edge, rating)
        megacun = MegaAttributeRating.objects.get(
            character=self, megaattribute__name="Mega-Cunning"
        ).rating
        while megacun > 0:
            diff, (edge, rating) = self.add_random_edge(sublist=mega_cun_edges)
            diff = int(diff)
            if diff <= megacun:
                megacun -= diff
                self.apply_edge(edge, rating)
        megaman = MegaAttributeRating.objects.get(
            character=self, megaattribute__name="Mega-Manipulation"
        ).rating
        while megaman > 0:
            diff, (edge, rating) = self.add_random_edge(sublist=mega_man_edges)
            diff = int(diff)
            if diff <= megaman:
                megaman -= diff
                self.apply_edge(edge, rating)
        megacom = MegaAttributeRating.objects.get(
            character=self, megaattribute__name="Mega-Composure"
        ).rating
        while megacom > 0:
            if (
                megacom >= 2
                and EdgeRating.objects.filter(
                    character=self, edge__name="Iron Will", rating=3
                ).count()
                > 0
            ):
                if self.enhanced_edges.filter(name="Indomitable").count() == 0:
                    self.enhanced_edges.add(
                        EnhancedEdge.objects.get(name="Indomitable")
                    )
            diff, (edge, rating) = self.add_random_edge(sublist=mega_com_edges)
            diff = int(diff)
            if diff <= megacom:
                megacom -= diff
                self.apply_edge(edge, rating)

    def compute_quantum_points(self):
        self.quantum_points = 10 + 5 * self.quantum

    def pay_cost(self, cost, transformation):
        self.xp -= cost
        if transformation is not None:
            self.transformations.add(transformation)
            self.save()

    def weight_rating_list(self, rating_list):
        new_list = []
        for x in rating_list:
            for _ in range(x.rating + 1):
                new_list.append(x)
        return new_list

    def add_random_attribute(self, sublist=None):
        if sublist is None:
            sublist = list(AttributeRating.objects.filter(character=self, rating__lt=5))
        else:
            sublist = [x for x in sublist if x.rating < 5]
        sublist = self.weight_rating_list(sublist)
        if len(sublist) > 0:
            attribute = random.choice(sublist)
            attribute.rating += 1
            attribute.save()
            return True
        else:
            return False

    def add_random_edge(self, sublist=None):
        if sublist is None:
            sublist = list(Edge.objects.all())
            mega_edges = MegaEdge.objects.all()
            sublist = [x for x in sublist if x not in mega_edges]
            path_edges = []
            for path in PathConnectionRating.objects.filter(character=self):
                path_edges.extend(list(path.path.edges.all()))
            sublist = [x for x in sublist if x not in path_edges]
        prereq_satisfied = []
        for edge in sublist:
            attribute_prereqs = edge.prereq_attributes.all()
            skill_prereqs = edge.prereq_skills.all()
            edge_prereqs = edge.prereq_edges.all()
            path_prereq = edge.prereq_path_rating
            satisfied = True
            for att_prereq in attribute_prereqs:
                x = AttributeRating.objects.get(
                    character=self, attribute=att_prereq.attribute
                )
                satisfied = satisfied and (x.rating >= att_prereq.rating)
            for skill_prereq in skill_prereqs:
                x = SkillRating.objects.get(character=self, skill=skill_prereq.skill)
                satisfied = satisfied and (x.rating >= skill_prereq.rating)
            for edge_prereq in edge_prereqs:
                if edge_prereq.edge in self.edges.all():
                    x = EdgeRating.objects.get(character=self, edge=edge_prereq.edge)
                    satisfied = satisfied and (x.rating >= edge_prereq.rating)
                else:
                    satisfied = satisfied and False
            paths = PathConnectionRating.objects.filter(character=self)
            if path_prereq > 0:
                satisfied = satisfied and any(
                    [x.rating > path_prereq for x in paths if edge in x.path.edges.all()]
                )
            if satisfied:
                prereq_satisfied.append(edge)
        rating_pairs = []
        current_edges = EdgeRating.objects.filter(character=self)
        for edge in prereq_satisfied:
            # print(edge.ratings)
            # print(ratings_to_list(edge.ratings))
            ratings = self.rating_prob_fix(list(map(int, ratings_to_list(edge.ratings))))
            # print(ratings)
            if edge in current_edges:
                ratings = [
                    x for x in ratings if x > current_edges.get(edge=edge).rating
                ]
            for r in ratings:
                rating_pairs.append((edge, r))
        if len(rating_pairs) != 0:
            choice = random.choice(rating_pairs)
            diff = choice[-1]
            diff = int(diff)
            if edge in self.edges.all():
                edge_rating = EdgeRating.objects.get(character=self, edge=edge)
                diff -= edge_rating.rating
            return diff, choice
        else:
            return False

    def apply_edge(self, edge, rating):
        if edge in self.edges.all():
            edge_rating = EdgeRating.objects.get(character=self, edge=edge)
            edge_rating.rating = rating
            edge_rating.save()
        else:
            EdgeRating.objects.create(character=self, edge=edge, rating=rating)

    def add_random_enhanced_edge(self):
        enhanced_edges = list(EnhancedEdge.objects.all())
        possible = []
        for ee in enhanced_edges:
            prereqs = ee.prereq_edges.all()
            valid = True
            for prereq in prereqs:
                edge = prereq.edge
                rating = prereq.rating
                valid = valid and (
                    EdgeRating.objects.filter(
                        character=self, edge=edge, rating__gte=rating
                    ).count()
                    > 0
                )
                if valid:
                    possible.append(ee)
        possible = [x for x in possible if x not in self.enhanced_edges.all()]
        if len(possible) == 0:
            return False
        else:
            ee = random.choice(possible)
            self.enhanced_edges.add(ee)
            self.save()
            return True

    def random_change_approach(self):
        approaches = ["FOR", "FIN", "RES"]
        approaches = [x for x in approaches if x != self.favored_approach]
        self.favored_approach = random.choice(approaches)
        self.save()

    def add_random_skill(self, sublist=None):
        if sublist is None:
            sublist = list(SkillRating.objects.filter(character=self, rating__lt=5))
        else:
            sublist = [x for x in sublist if x.rating < 5]
        sublist = self.weight_rating_list(sublist)
        if len(sublist) > 0:
            skill = random.choice(sublist)
            skill.rating += 1
            skill.save()
            return True
        else:
            return False

    def add_random_skill_trick(self, sublist=None):
        if sublist is None:
            sublist = SkillRating.objects.filter(character=self, rating__gt=0)
        sublist = [
            x
            for x in sublist
            if Trick.objects.filter(skill=x.skill).count() > x.tricks.count()
        ]
        if len(sublist) == 0:
            return False
        skill = random.choice(sublist)
        possible_tricks = list(Trick.objects.filter(skill=skill.skill))
        possible_tricks = [x for x in possible_tricks if x not in skill.tricks.all()]
        new_trick = random.choice(possible_tricks)
        skill.tricks.add(new_trick)
        skill.save()
        return True

    def add_random_skill_specialty(self, sublist=None):
        if sublist is None:
            sublist = list(
                SkillRating.objects.filter(character=self, rating__gte=3, specialty="")
            )
        if len(sublist) == 0:
            return False
        skill = random.choice(sublist)
        specialties = skill.skill.specialties[1:-1].replace("'", "").replace("\"", "").split(",")
        if len(specialties) == 0:
            specialties = ["Something"]
        skill.specialty = random.choice(specialties)
        skill.save()

    def add_random_path_dot(self, sublist=None):
        if sublist is None:
            sublist = list(Path.objects.all())
        if self.paths.count() >= 5:
            sublist = [x.path for x in PathConnectionRating.objects.filter(character=self)]
        path = random.choice(sublist)
        if PathConnectionRating.objects.filter(character=self, path=path).count() > 0:
            connection_rating = PathConnectionRating.objects.get(
                character=self, path=path
            )
            connection_rating.rating += 1
            connection_rating.save()
        else:
            connection = random.choice(PathConnection.objects.filter(path=path))
            PathConnectionRating.objects.create(
                character=self, path=path, path_connection=connection, rating=1
            )

    def add_random_mega_attribute(self, sublist=None):
        if sublist is None:
            sublist = list(
                MegaAttributeRating.objects.filter(
                    character=self, rating__lt=self.quantum
                )
            )
        else:
            sublist = [x for x in sublist if x.rating < 5]
        sublist = self.weight_rating_list(sublist)
        if len(sublist) > 0:
            attribute = random.choice(sublist)
            attribute.rating += 1
            attribute.save()
            return True
        else:
            return False

    def add_transcendance(self):
        self.transcendence += 1
        self.save()

    def add_random_mega_edge(self, sublist=None):
        if sublist is None:
            sublist = list(MegaEdge.objects.all())
        prereq_satisfied = []
        for edge in sublist:
            attribute_prereqs = edge.prereq_attributes.all()
            mega_attribute_prereqs = edge.prereq_megaatt.all()
            skill_prereqs = edge.prereq_skills.all()
            edge_prereqs = edge.prereq_edges.all()
            path_prereq = edge.prereq_path_rating
            prereq_quantum = edge.prereq_quantum
            satisfied = True
            for att_prereq in attribute_prereqs:
                x = AttributeRating.objects.get(
                    character=self, attribute=att_prereq.attribute
                )
                satisfied = satisfied and (x.rating >= att_prereq.rating)
            for skill_prereq in skill_prereqs:
                x = SkillRating.objects.get(character=self, skill=skill_prereq.skill)
                satisfied = satisfied and (x.rating >= skill_prereq.rating)
            for edge_prereq in edge_prereqs:
                if edge_prereq.edge in self.edges.all():
                    x = EdgeRating.objects.get(character=self, edge=edge_prereq.edge)
                    satisfied = satisfied and (x.rating >= edge_prereq.rating)
                else:
                    satisfied = satisfied and False
            for mega_att_prereq in mega_attribute_prereqs:
                x = MegaAttributeRating.objects.get(
                    character=self, megaattribute=mega_att_prereq.megaattribute
                )
                satisfied = satisfied and (x.rating >= mega_att_prereq.rating)
            paths = PathConnectionRating.objects.filter(character=self)
            paths = [x.path for x in paths]
            if path_prereq > 0:
                satisfied = satisfied and any(
                    [x.rating > path_prereq for x in paths if edge in x.edges]
                )
            if prereq_quantum > 0:
                satisfied = satisfied and (self.quantum >= prereq_quantum)
            if satisfied:
                prereq_satisfied.append(edge)
        rating_pairs = []
        current_edges = EdgeRating.objects.filter(character=self)
        for edge in prereq_satisfied:
            ratings = self.rating_prob_fix(list(map(int, ratings_to_list(edge.ratings))))
            if edge in current_edges:
                ratings = [
                    x for x in ratings if x > current_edges.get(edge=edge).rating
                ]
            for r in ratings:
                if prereq_quantum == -1:
                    if r <= self.quantum:
                        rating_pairs.append((edge, r))
                else:
                    rating_pairs.append((edge, r))
        choice = random.choice(rating_pairs)
        diff = choice[-1]
        if edge in self.edges.all():
            edge_rating = MegaEdgeRating.objects.get(character=self, megaedge=edge)
            diff -= edge_rating
        return diff, choice

    def apply_mega_edge(self, mega_edge, rating):
        if mega_edge in self.megaedges.all():
            edge_rating = MegaEdgeRating.objects.get(character=self, megaedge=mega_edge)
            edge_rating.rating = rating
            edge_rating.save()
        else:
            MegaEdgeRating.objects.create(
                character=self, megaedge=mega_edge, rating=rating
            )

    def add_random_power_tag(self):
        power = PowerRating.objects.filter(character=self).order_by("?").first()

        if power is None:
            return False

        tags_on_power = TagRating.objects.filter(power=power)
        tags_on_power_pairs = [(x.tag, x.rating) for x in tags_on_power]

        all_tags = Tag.objects.all()
        all_tags = [x for x in all_tags if power.power in x.permitted_powers.all()]

        all_tag_ratings = [(x, r) for x in all_tags for r in self.rating_prob_fix(list(map(int, ratings_to_list(x.ratings))))]

        valid_pairs = []

        for tag, rating in all_tag_ratings:
            if tag in [x[0] for x in tags_on_power_pairs]:
                r = [x[1] for x in tags_on_power_pairs if x[0] == tag][0]
                if rating > r:
                    valid_pairs.append((tag, rating))
            else:
                valid_pairs.append((tag, rating))
        tag, rating = random.choice(valid_pairs)
        diff = rating
        if tag in power.tags.all():
            diff -= TagRating.objects.get(power=power, tag=tag).rating
        return diff, (power, tag, rating)

    def apply_power_tag(self, power, tag, rating):
        if tag in power.tags.all():
            tag_rating = TagRating.objects.get(power=power, tag=tag)
            tag_rating.rating = rating
            tag_rating.save()
        else:
            TagRating.objects.create(power=power, tag=tag, rating=rating)

    def add_quantum(self):
        if self.quantum < 5:
            self.quantum += 1
            self.save()
            return True
        return False

    def add_random_power(self):
        all_powers = list(Power.objects.filter(quantum_minimum__lte=self.quantum))
        all_powers_had = list(PowerRating.objects.filter(character=self))
        for power in all_powers_had:
            for i in range(power.rating):
                for j in range(len(all_powers)):
                    all_powers.append(power.power)

        new_power = random.choice(all_powers)

        powers_had = self.powers.all()
        if new_power in powers_had:
            powerrating = PowerRating.objects.get(character=self, power=new_power)
            if powerrating.rating == self.quantum:
                return False
            powerrating.rating += 1
            powerrating.save()
            return True
        else:
            PowerRating.objects.create(character=self, power=new_power, rating=1)
            return True

    def rating_prob_fix(self, ratings):
        total = abs(math.prod(ratings))
        new_ratings = []
        for r in ratings:
            if r != 0:
                num = abs(int(total/r))
            else:
                num = abs(int(total))
            for _ in range(num):
                new_ratings.append(r)
        return new_ratings

    def __str__(self):
        return self.name


# RATINGS
class AttributeRating(models.Model):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, blank=True, null=True
    )
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.character}: {self.attribute}: {self.rating}"


class MegaAttributeRating(models.Model):
    megaattribute = models.ForeignKey(
        MegaAttribute, on_delete=models.CASCADE, blank=True, null=True
    )
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.character}: {self.megaattribute}: {self.rating}"

class SkillRating(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=True, null=True)
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=1)
    tricks = models.ManyToManyField(Trick, blank=True)
    specialty = models.CharField(max_length=100)

    def __str__(self):
        s = f"{self.character}: {self.skill}: {self.rating}"
        if self.specialty != "":
            s += f" ({self.specialty})"
        if self.tricks.count() > 0:
            tricks = ", ".join([x.name for x in list(self.tricks.all())])
            s += f" {tricks}"
        return s

class EdgeRating(models.Model):
    edge = models.ForeignKey(Edge, on_delete=models.CASCADE, blank=True, null=True)
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.edge.name}: {self.rating}"


class MegaEdgeRating(models.Model):
    megaedge = models.ForeignKey(
        MegaEdge, on_delete=models.CASCADE, blank=True, null=True
    )
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.megaedge.name}: {self.rating}"


class PowerRating(models.Model):
    character = models.ForeignKey(
        Aberrant, on_delete=models.CASCADE, blank=True, null=True
    )
    power = models.ForeignKey(Power, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, through="TagRating")
    rating = models.IntegerField(default=0)
    options = models.ManyToManyField(Option, blank=True)

class TagRating(models.Model):
    tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE)
    power = models.ForeignKey(
        PowerRating, blank=True, null=True, on_delete=models.CASCADE
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.tag.name}: {self.rating}"


# PREREQS
class AttributePrereq(models.Model):
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.attribute} {self.rating}"


class MegaAttributePrereq(models.Model):
    megaattribute = models.ForeignKey(
        MegaAttribute, on_delete=models.CASCADE, blank=True, null=True
    )
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.megaattribute} {self.rating}"


class SkillPrereq(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.skill} {self.rating}"


class EdgePrereq(models.Model):
    edge = models.ForeignKey(Edge, on_delete=models.CASCADE, blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.edge}: {self.rating}"


def ratings_to_list(s):
    return s[1:-1].split(",")
