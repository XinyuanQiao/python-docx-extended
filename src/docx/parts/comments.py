"""Comments part, containing document-level comment definitions."""

from __future__ import annotations

from typing import TYPE_CHECKING

from docx.opc.part import XmlPart
from docx.oxml.comments import CT_Comments

if TYPE_CHECKING:
    from docx.opc.package import OpcPackage
    from docx.opc.packuri import PackURI
    from docx.oxml.comments import CT_Comment


class CommentsPart(XmlPart):
    """Proxy for comments.xml part containing document comments."""

    def __init__(self, partname: PackURI, content_type: str, element: CT_Comments, package: OpcPackage):
        super(CommentsPart, self).__init__(partname, content_type, element, package)

    @classmethod
    def new(cls):
        """Return newly created CommentsPart object."""
        # This would need to be implemented to create a new comments part
        pass

    @property
    def comments_element(self) -> CT_Comments:
        """CT_Comments element at root of comments.xml part."""
        return self._element

    def add_comment(self, comment_id: int, author: str, text: str, initials: str | None = None) -> CT_Comment:
        """Add a new comment to this comments part."""
        from docx.oxml.comments import CT_Comment
        comment = CT_Comment.new(comment_id, author, text, initials)
        self.comments_element.append(comment)
        return comment

    def get_comment_by_id(self, comment_id: int) -> CT_Comment | None:
        """Return comment with given ID, None if not found."""
        comments_list = self.comments_element.xpath('.//w:comment')
        for comment in comments_list:
            if hasattr(comment, 'id') and comment.id == comment_id:
                return comment
        return None

    def remove_comment(self, comment_id: int) -> bool:
        """Remove comment with given ID. Return True if found and removed."""
        comment = self.get_comment_by_id(comment_id)
        if comment is not None:
            self.comments_element.remove(comment)
            return True
        return False

    def get_next_comment_id(self) -> int:
        """Return next available comment ID."""
        comments_list = self.comments_element.xpath('.//w:comment')
        existing_ids = [getattr(comment, 'id', 0) for comment in comments_list if hasattr(comment, 'id')]
        return max(existing_ids, default=0) + 1 