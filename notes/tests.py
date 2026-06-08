from django.test import TestCase
from django.urls import reverse

from .models import Note



class NoteModelTest(TestCase):
    """Tests for the Note model."""


    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )

    def test_note_title(self):
        self.assertEqual(
            self.note.title,
            "Test Note"
        )

    def test_note_content(self):
        self.assertEqual(
            self.note.content,
            "Test Content"
        )


class NoteViewTest(TestCase):
    """Tests for note views and CRUD functionality."""

    def setUp(self):
        self.note = Note.objects.create(
            title="Test Note",
            content="Test Content"
        )

    def test_note_list_view(self):

        response = self.client.get(
            reverse("note_list")
        )

        self.assertEqual(
            response.status_code,
            200
        )

        self.assertContains(
            response,
            "Test Note"
        )

    def test_create_note(self):

        self.client.post(
            reverse("note_create"),
            {
                "title": "New Note",
                "content": "New Content"
            }
        )

        self.assertEqual(
            Note.objects.count(),
            2
        )

    def test_update_note(self):

        self.client.post(
            reverse(
                "note_update",
                args=[self.note.id]
            ),
            {
                "title": "Updated Note",
                "content": "Updated Content"
            }
        )

        self.note.refresh_from_db()

        self.assertEqual(
            self.note.title,
            "Updated Note"
        )

    def test_delete_note(self):

        self.client.post(
            reverse(
                "note_delete",
                args=[self.note.id]
            )
        )

        self.assertEqual(
            Note.objects.count(),
            0
        )