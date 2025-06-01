"""Unit tests for comment functionality."""

from __future__ import annotations

import pytest

from docx.oxml.comments import CT_Comments, CT_Comment, CT_CommentRangeStart, CT_CommentRangeEnd, CT_CommentReference


class TestCT_Comments:
    """Test CT_Comments XML element class."""

    def test_new_creates_empty_comments_element(self):
        """CT_Comments.new() creates a new empty comments element."""
        comments = CT_Comments.new()
        assert comments.tag.endswith('comments')
        assert len(list(comments)) == 0

    def test_can_add_comment_element(self):
        """Can add comment elements to comments container."""
        comments = CT_Comments.new()
        comment = CT_Comment.new(1, "Test Author", "Test comment text")
        comments.append(comment)
        assert len(list(comments)) == 1


class TestCT_Comment:
    """Test CT_Comment XML element class."""

    def test_new_creates_comment_with_required_attributes(self):
        """CT_Comment.new() creates comment with required attributes."""
        comment = CT_Comment.new(1, "Test Author", "Test comment text")
        assert comment.tag.endswith('comment')
        assert comment.id == 1
        assert comment.author == "Test Author"

    def test_new_creates_comment_with_initials(self):
        """CT_Comment.new() can create comment with initials."""
        comment = CT_Comment.new(1, "Test Author", "Test comment text", "TA")
        assert comment.initials == "TA"

    def test_text_content_returns_comment_text(self):
        """Comment.text_content returns the text content."""
        comment = CT_Comment.new(1, "Test Author", "Test comment text")
        # This might need adjustment based on actual XML structure
        text_content = comment.text_content
        assert "Test comment text" in text_content


class TestCT_CommentRangeStart:
    """Test CT_CommentRangeStart XML element class."""

    def test_new_creates_range_start_element(self):
        """CT_CommentRangeStart.new() creates range start element."""
        range_start = CT_CommentRangeStart.new(1)
        assert range_start.tag.endswith('commentRangeStart')
        assert range_start.id == 1


class TestCT_CommentRangeEnd:
    """Test CT_CommentRangeEnd XML element class."""

    def test_new_creates_range_end_element(self):
        """CT_CommentRangeEnd.new() creates range end element."""
        range_end = CT_CommentRangeEnd.new(1)
        assert range_end.tag.endswith('commentRangeEnd')
        assert range_end.id == 1


class TestCT_CommentReference:
    """Test CT_CommentReference XML element class."""

    def test_new_creates_reference_element(self):
        """CT_CommentReference.new() creates reference element."""
        reference = CT_CommentReference.new(1)
        assert reference.tag.endswith('commentReference')
        assert reference.id == 1


class TestCommentIntegration:
    """Integration tests for comment functionality."""

    def test_create_comment_workflow(self):
        """Test basic comment creation workflow."""
        # Create comments container
        comments = CT_Comments.new()
        
        # Create a comment
        comment = CT_Comment.new(1, "John Doe", "This is a test comment", "JD")
        
        # Add comment to container
        comments.append(comment)
        
        # Verify comment was added
        assert len(list(comments)) == 1
        
        # Verify comment properties
        added_comment = list(comments)[0]
        assert added_comment.id == 1
        assert added_comment.author == "John Doe"
        assert added_comment.initials == "JD"

    def test_comment_range_elements(self):
        """Test comment range start/end elements."""
        range_start = CT_CommentRangeStart.new(1)
        range_end = CT_CommentRangeEnd.new(1)
        reference = CT_CommentReference.new(1)
        
        # All should have same ID
        assert range_start.id == range_end.id == reference.id == 1 