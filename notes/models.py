from django.db import models


class Note(models.Model):
    """
    Represents a sticky note containing a title and content.

    Notes can be created, viewed, edited, and deleted through
    the Sticky Notes application.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        """
        Return the note title as its string representation.

        :return: The title of the note.
        """
        return self.title