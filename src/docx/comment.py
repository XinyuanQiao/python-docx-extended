"""Comment objects for representing document comments."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from docx.oxml.comments import CT_Comment


class Comment:
    """Represents a single comment in a Word document."""

    def __init__(self, comment_element: CT_Comment):
        """Create Comment object from CT_Comment element."""
        self._element = comment_element

    @property
    def id(self) -> int:
        """Comment ID."""
        return self._element.id

    @property
    def author(self) -> str:
        """Comment author."""
        return self._element.author

    @property
    def text(self) -> str:
        """Comment text content."""
        return self._element.text_content

    @property
    def initials(self) -> str | None:
        """Comment author initials."""
        return getattr(self._element, 'initials', None)

    @property
    def date(self) -> str | None:
        """Comment creation date."""
        return getattr(self._element, 'date', None)

    def __repr__(self) -> str:
        return f'<Comment id={self.id} author="{self.author}">'


class Comments:
    """Collection of Comment objects for a document."""

    def __init__(self, comments_part):
        """Create Comments collection from CommentsPart."""
        self._comments_part = comments_part

    def add_comment(self, author: str, text: str, initials: str | None = None) -> Comment:
        """Add a new comment to the document."""
        comment_id = self._comments_part.get_next_comment_id()
        comment_element = self._comments_part.add_comment(comment_id, author, text, initials)
        return Comment(comment_element)

    def get_by_id(self, comment_id: int) -> Comment | None:
        """Get comment by ID."""
        comment_element = self._comments_part.get_comment_by_id(comment_id)
        return Comment(comment_element) if comment_element else None

    def remove_by_id(self, comment_id: int) -> bool:
        """Remove comment by ID. Return True if found and removed."""
        return self._comments_part.remove_comment(comment_id)

    def __iter__(self):
        """Iterate over all comments."""
        comments_list = self._comments_part.comments_element.xpath('.//w:comment')
        for comment_element in comments_list:
            yield Comment(comment_element)

    def __len__(self) -> int:
        """Return number of comments."""
        comments_list = self._comments_part.comments_element.xpath('.//w:comment')
        return len(comments_list) 