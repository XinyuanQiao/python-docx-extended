"""Example usage of comment functionality in python-docx-extended."""

from docx import Document
from docx.oxml.comments import CT_Comments, CT_Comment, CT_CommentRangeStart, CT_CommentRangeEnd, CT_CommentReference


def basic_comment_creation_example():
    """Demonstrate basic comment creation at XML level."""
    print("=== Basic Comment Creation Example ===")
    
    # Create a comments container
    comments = CT_Comments.new()
    print(f"Created comments container: {comments.tag}")
    
    # Create individual comments
    comment1 = CT_Comment.new(1, "Alice Smith", "This needs revision", "AS")
    comment2 = CT_Comment.new(2, "Bob Johnson", "Good point", "BJ")
    
    # Add comments to container
    comments.append(comment1)
    comments.append(comment2)
    
    print(f"Added {len(list(comments))} comments")
    
    # Display comment details
    for comment in comments:
        print(f"Comment {comment.id}: {comment.author} - {comment.text_content}")


def comment_range_example():
    """Demonstrate comment range elements."""
    print("\n=== Comment Range Example ===")
    
    comment_id = 1
    
    # Create range elements for a comment
    range_start = CT_CommentRangeStart.new(comment_id)
    range_end = CT_CommentRangeEnd.new(comment_id)
    reference = CT_CommentReference.new(comment_id)
    
    print(f"Range start: {range_start.tag} (id={range_start.id})")
    print(f"Range end: {range_end.tag} (id={range_end.id})")
    print(f"Reference: {reference.tag} (id={reference.id})")


def document_integration_example():
    """Show how comments might integrate with document."""
    print("\n=== Document Integration Example ===")
    
    # Note: This is a conceptual example
    # In full implementation, this would integrate with Document class
    
    doc = Document()
    paragraph = doc.add_paragraph("This is some text that will have a comment.")
    
    print(f"Created document with paragraph: '{paragraph.text}'")
    print("Note: Full comment integration would require:")
    print("1. Adding comments part to document")
    print("2. Inserting comment range markers in content")
    print("3. Adding comment reference in the range")


if __name__ == "__main__":
    try:
        basic_comment_creation_example()
        comment_range_example()
        document_integration_example()
        
        print("\n=== Example completed successfully! ===")
        print("To run tests: pytest tests/test_comments.py")
        
    except Exception as e:
        print(f"Error running example: {e}")
        print("This is expected as the full implementation is not complete.") 