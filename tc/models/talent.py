from django.db import models

# Create your models here.
class Attribute(models.Model):
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
        ordering = ("name",)

    def __str__(self):
        return self.name


class Edge(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.JSONField(null=True, default=list)
    description = models.TextField(default="")
    prereq_attributes = models.ManyToManyField("AttributePrereq", blank=True)
    prereq_skills = models.ManyToManyField("SkillPrereq", blank=True)
    prereq_path_rating = models.IntegerField(default=0)
    prereq_edges = models.ManyToManyField(
        "EdgePrereq", blank=True, related_name="prereq_to"
    )

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class EnhancedEdge(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    prereq_edges = models.ManyToManyField("EdgePrereq", blank=True)

    class Meta:
        ordering = ("name",)

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
        ordering = ("name",)

    def __str__(self):
        return self.name


class PathConnection(models.Model):
    name = models.CharField(max_length=100)
    path = models.ForeignKey("Path", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ("name",)

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
