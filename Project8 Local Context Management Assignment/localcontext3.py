from main import config
from pydantic import BaseModel
from agents import (
    Agent,
    Runner,
    RunContextWrapper,
    function_tool
)
import asyncio
import rich


# ------------------ Model ------------------
class LibraryBook(BaseModel):
    book_id: str
    book_title: str
    author_name: str
    is_available: bool

library_book = LibraryBook(
    book_id="BOOK-123",
    book_title="Python Programming",
    author_name="John Smith",
    is_available=True
)

# ------------------ Tool ------------------
@function_tool
def get_book_info(wrapper: RunContextWrapper[LibraryBook]):
    b = wrapper.context
    return {
        "book_id": b.book_id,
        "book_title": b.book_title,
        "author_name": b.author_name,
        "is_available": "Yes" if b.is_available else "No"
    }
    # OR return f"Book '{b.book_title}' by {b.author_name} (ID: {b.book_id}) is {'available' if b.is_available else 'not available'}."

# ------------------ Agent ------------------
library_agent = Agent(
    name="Library Agent",
    instructions=(
        "You are a helpful library assistant. "
        "When the user asks for book details, use the get_book_info tool "
        "to provide book ID, title, author, and availability status."
    ),
    tools=[get_book_info]
)

# ------------------ Runner ------------------
async def main():
    result = await Runner.run(
        starting_agent=library_agent,
        input="Please tell me the book details.",
        run_config=config,
        context=library_book  # local library book context
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run localcontext3.py

