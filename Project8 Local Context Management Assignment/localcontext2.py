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
class StudentProfile(BaseModel):
    student_id: str
    student_name: str
    current_semester: int
    total_courses: int

student = StudentProfile(
    student_id="STU-456",
    student_name="Hassan Ahmed",
    current_semester=4,
    total_courses=5
)

# ------------------ Tool ------------------
@function_tool
def get_student_info(wrapper: RunContextWrapper[StudentProfile]):
    s = wrapper.context
    return {
        "student_id": s.student_id,
        "student_name": s.student_name,
        "current_semester": s.current_semester,
        "total_courses": s.total_courses
    }
    # OR return f"Student {s.student_name} (ID: {s.student_id}) is in semester {s.current_semester} with {s.total_courses} courses."

# ------------------ Agent ------------------
student_agent = Agent(
    name="Student Agent",
    instructions=(
        "You are a helpful academic assistant. "
        "When the user asks for student details, use the get_student_info tool "
        "to provide student ID, name, semester, and total courses."
    ),
    tools=[get_student_info]
)

# ------------------ Runner ------------------
async def main():
    result = await Runner.run(
        starting_agent=student_agent,
        input="Please tell me the student details.",
        run_config=config,
        context=student  # local context
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

# uv run localcontext2.py

