from app.pkg.schema.book import (
    BookSchema,
    CreateBookSchema,
    UpdateBookSchema,
    DeleteBookByNameSchema,
    GetBookByNameSchema,
)
from app.pkg.schema.author import (
    BookSchema,
    CreateAuthorSchema,
    AuthorSchema,
    DeleteAuthorByNameSchema,
    GetAuthorByNameSchema,
    UpdateAuthorSchema,
)

__all__ = [
    # Book Schemas
    "BookSchema",
    "CreateBookSchema",
    "UpdateBookSchema",
    "DeleteBookByNameSchema",
    "GetBookByNameSchema",
    # Author Schemas
    "AuthorSchema",
    "CreateAuthorSchema",
    "DeleteAuthorByNameSchema",
    "GetAuthorByNameSchema",
    "UpdateAuthorSchema",
]
