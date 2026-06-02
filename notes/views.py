from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import NoteForm
from .models import Note


def note_list(request):
    """Display all notes."""
    notes = Note.objects.all()

    return render(
        request,
        "notes/note_list.html",
        {"notes": notes},
    )


def note_create(request):
    """Create a new note."""
    if request.method == "POST":
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = NoteForm()

    return render(
        request,
        "notes/note_form.html",
        {"form": form},
    )


def note_update(request, pk):
    """Update an existing note."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        form = NoteForm(
            request.POST,
            instance=note,
        )

        if form.is_valid():
            form.save()
            return redirect("note_list")

    else:
        form = NoteForm(instance=note)

    return render(
        request,
        "notes/note_form.html",
        {"form": form},
    )


def note_delete(request, pk):
    """Delete a note."""
    note = get_object_or_404(Note, pk=pk)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(
        request,
        "notes/note_confirm_delete.html",
        {"note": note},
    )