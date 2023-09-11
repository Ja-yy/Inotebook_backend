"""ENDPOINT - NOTES
Endpoints for notes 
"""
from typing import List

from bson.objectid import ObjectId
from fastapi import APIRouter, Depends

from app.models.notes import CreateNote, NoteBase, Notes, UpdateNote
from app.repository.notes import NotesRepository
from app.utils.auth.auth_barare import get_user_id

router = APIRouter(prefix="/notes", tags=["Notes"])


# Retrieve all notes for a user : GET "/all"
@router.get("/all", response_model=List[Notes])
async def get_all_notes(user_id: ObjectId = Depends(get_user_id)):
    """
    Retrieves all notes for a user.

    Args:
        user_id (ObjectId, optional): The unique identifier of the user. Defaults to the user ID obtained from the authentication token.

    Returns:
        List[Notes]: A list of notes associated with the user.
    """
    db = NotesRepository()
    notes_res = await db.filter({"user_id": user_id}, is_one=False)
    return notes_res


# Create a new note : POST "/add"
@router.post("/add", response_model=NoteBase)
async def create_note(
    note: CreateNote,
    user_id: ObjectId = Depends(get_user_id),
):
    """
    Creates a new note for a user.

    Args:
        note (CreateNote): The data for creating a new note.
        user_id (ObjectId, optional): The unique identifier of the user. Defaults to the user ID obtained from the authentication token.

    Returns:
        NoteBase: The created note.
    """

    db = NotesRepository()
    note.user_id = user_id
    db_obj = await db.create(note)
    return db_obj


# Update an existing note : PATCH "/update/{note_id}"
@router.patch("/update/{note_id}", response_model=UpdateNote)
async def update_note(
    note_id: str, update_obj: UpdateNote, user_id: ObjectId = Depends(get_user_id)
):
    """
    Deletes a note with the specified ID.

    Args:
        note_id (str): The unique identifier of the note to be deleted.
        user_id (ObjectId, optional): The unique identifier of the user. Defaults to the user ID obtained from the authentication token.

    Returns:
        NoteBase: The deleted note.
    """

    db = NotesRepository()

    return_obj = await db.update(
        {"_id": ObjectId(note_id), "user_id": user_id}, update_obj
    )
    return return_obj


# Delete a note : DELETE "/delete/{note_id}"
@router.delete("/delete/{note_id}", response_model=NoteBase)
async def delete_note(note_id: str, user_id: ObjectId = Depends(get_user_id)):
    db = NotesRepository()
    return_obj = await db.delete({"_id": ObjectId(note_id), "user_id": user_id})
    return return_obj


# Retrieve notes with a specific tag : GET "/tag/{tag}"
@router.get("/tag/{tag}", response_model=List[NoteBase])
async def get_note_by_tag(tag: str, user_id: ObjectId = Depends(get_user_id)):
    """
    Retrieves notes with a specific tag for a user.

    Args:
        tag (str): The tag to filter notes by.
        user_id (ObjectId, optional): The unique identifier of the user. Defaults to the user ID obtained from the authentication token.

    Returns:
        List[NoteBase]: A list of notes that have the specified tag."""

    db = NotesRepository()
    user_notes = await db.filter(
        {"tag": tag, "user_id": user_id},
        is_one=False,
    )
    return user_notes


# Retrieve a list of unique tags associated with a user's notes : GET "/tags/list"
@router.get(
    "/tags/list",
)
async def list_tags(user_id: ObjectId = Depends(get_user_id)):
    """
    Retrieves a list of unique tags associated with a user's notes.

    Args:
        user_id (ObjectId, optional): The unique identifier of the user. Defaults to the user ID obtained from the authentication token.

    Returns:
        dict: A dictionary containing a list of unique tags associated with the user's notes.
            Example: {"tags": ["work", "personal", "ideas"]}
    """

    db = NotesRepository()
    notes_res = await db.filter(
        filters={"user_id": user_id},
        is_one=False,
    )
    tags = list(set(item.get("tag") for item in notes_res))
    return {"tags": tags}
