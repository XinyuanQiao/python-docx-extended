"""Comments-related XML element classes."""

from __future__ import annotations

from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from docx.oxml.simpletypes import ST_DecimalNumber, ST_String
from docx.oxml.xmlchemy import BaseOxmlElement, ZeroOrMore, RequiredAttribute, OptionalAttribute


class CT_Comments(BaseOxmlElement):
    """``<w:comments>`` element, container for comment elements."""
    
    comment = ZeroOrMore('w:comment')

    @classmethod
    def new(cls) -> 'CT_Comments':
        """Return a new ``<w:comments>`` element."""
        return parse_xml(cls._comments_xml())

    @staticmethod
    def _comments_xml():
        return (
            f'<w:comments {nsdecls("w")}>\n'
            '</w:comments>'
        )


class CT_Comment(BaseOxmlElement):
    """``<w:comment>`` element, representing a single comment."""
    
    id: int = RequiredAttribute('w:id', ST_DecimalNumber)  # pyright: ignore[reportAssignmentType]
    author: str = RequiredAttribute('w:author', ST_String)  # pyright: ignore[reportAssignmentType]
    date: str | None = OptionalAttribute('w:date', ST_String)  # pyright: ignore[reportAssignmentType]
    initials: str | None = OptionalAttribute('w:initials', ST_String)  # pyright: ignore[reportAssignmentType]

    @classmethod
    def new(cls, comment_id: int, author: str, text: str, initials: str | None = None) -> 'CT_Comment':
        """Return a new ``<w:comment>`` element."""
        initials_attr = f' w:initials="{initials}"' if initials else ''
        return parse_xml(cls._comment_xml(comment_id, author, text, initials_attr))

    @staticmethod
    def _comment_xml(comment_id: int, author: str, text: str, initials_attr: str = ''):
        return (
            f'<w:comment {nsdecls("w")} w:id="{comment_id}" w:author="{author}"{initials_attr}>\n'
            f'  <w:p><w:r><w:t>{text}</w:t></w:r></w:p>\n'
            '</w:comment>'
        )

    @property
    def text_content(self) -> str:
        """Return the text content of this comment."""
        # Simple implementation - get text from all <w:t> elements
        return ''.join(t.text or '' for t in self.xpath('.//w:t'))


class CT_CommentRangeStart(BaseOxmlElement):
    """``<w:commentRangeStart>`` element."""
    
    id: int = RequiredAttribute('w:id', ST_DecimalNumber)  # pyright: ignore[reportAssignmentType]

    @classmethod
    def new(cls, comment_id: int) -> 'CT_CommentRangeStart':
        """Return a new ``<w:commentRangeStart>`` element."""
        return parse_xml(f'<w:commentRangeStart {nsdecls("w")} w:id="{comment_id}"/>')


class CT_CommentRangeEnd(BaseOxmlElement):
    """``<w:commentRangeEnd>`` element."""
    
    id: int = RequiredAttribute('w:id', ST_DecimalNumber)  # pyright: ignore[reportAssignmentType]

    @classmethod
    def new(cls, comment_id: int) -> 'CT_CommentRangeEnd':
        """Return a new ``<w:commentRangeEnd>`` element."""
        return parse_xml(f'<w:commentRangeEnd {nsdecls("w")} w:id="{comment_id}"/>')


class CT_CommentReference(BaseOxmlElement):
    """``<w:commentReference>`` element."""
    
    id: int = RequiredAttribute('w:id', ST_DecimalNumber)  # pyright: ignore[reportAssignmentType]

    @classmethod
    def new(cls, comment_id: int) -> 'CT_CommentReference':
        """Return a new ``<w:commentReference>`` element."""
        return parse_xml(f'<w:commentReference {nsdecls("w")} w:id="{comment_id}"/>') 