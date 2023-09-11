"""REPOSITORIES - NOTES
Notes repositores for database operations
"""

from app.models.notes import Notes
from app.repository.base import BaseRepository


class NotesRepository(BaseRepository):
    schema_model = Notes
    collection_name = "notesCol"
