import os
from datetime import datetime

import mcp
import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP  # Import FastMCP, the quickstart server base

load_dotenv()

mcp = FastMCP(title="Moodle MCP Server")

# Base URL for Moodle API
MOODLE_URL = os.getenv("MOODLE_URL", "https://odtuclass.metu.edu.tr")
MOODLE_TOKEN = os.getenv("MOODLE_TOKEN")


@mcp.tool()
def get_assignments():
    """Fetch assignments from Moodle API."""
    # Get assignments list
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "mod_assign_get_assignments",
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    return data


@mcp.tool()
def get_site_info():
    """Get Moodle site information including user details."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_webservice_get_site_info",
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_enrolled_courses():
    """Get list of enrolled courses."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_course_get_enrolled_courses_by_timeline_classification",
            "classification": "all",
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_course_contents(course_id: int):
    """Get contents of a specific course."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_course_get_contents",
            "courseid": str(course_id),
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_forum_discussions(forum_id: int):
    """Get forum discussions."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "mod_forum_get_forum_discussions",
            "forumid": str(forum_id),
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_assignment_submission(assign_id: int, user_id: str):
    """Get submission status for an assignment."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "mod_assign_get_submission_status",
            "assignid": str(assign_id),
            "userid": user_id,
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_calendar_events(course_id: int):
    """Get calendar events for a course."""
    current_timestamp = int(datetime.now().timestamp())
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_calendar_get_calendar_events",
            "events[courseids][0]": str(course_id),
            "options[timestart]": str(current_timestamp),
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_course_grades(course_id: int, user_id: str):
    """Get grade items for a course."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "gradereport_user_get_grade_items",
            "courseid": str(course_id),
            "userid": user_id,
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_messages(user_id: str, read: bool = False):
    """Get messages/notifications for a user."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_message_get_messages",
            "useridto": user_id,
            "type": "notifications",
            "read": "1" if read else "0",
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def mark_notification_read(notification_id: int):
    """Mark a notification as read."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_message_mark_notification_read",
            "notificationid": str(notification_id),
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_course_by_field(field: str, value: str):
    """Get course information by field (id or idnumber)."""
    response = requests.get(
        f"{MOODLE_URL}/webservice/rest/server.php",
        params={
            "wstoken": MOODLE_TOKEN,
            "wsfunction": "core_course_get_courses_by_field",
            "field": field,
            "value": value,
            "moodlewsrestformat": "json",
        },
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="stdio")
