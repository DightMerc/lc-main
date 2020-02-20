from django.db import models

class ProjectCategory(models.Model):
    title = models.CharField("Название", max_length=255, blank=False, null=False)

    def __str__(self):
        return f"{self.id}: {title}"


class Project(models.Model):
    title = models.CharField("Название", max_length=255, blank=False, null=False)

    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)

    description = models.TextField("Описание", null=False, blank=False)

    image = models.ImageField("Фото", upload_to="media/projects/photo")

    feedback = models.TextField("Отзыв клиента", null=True, blank=True)

    def __str__(self):
        return f"{self.id}: {title}"


# class TitleTE
