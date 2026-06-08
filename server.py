from fastmcp import FastMCP
from datetime import datetime
import os

mcp = FastMCP("Demo MCP Server")

# Statically defined user data
USERS = {
    "john.doe@example.com": {
        "fullname": "John Doe",
        "phone": "+1-202-555-0143",
        "email": "john.doe@example.com",
        "address": "123 Maple Street, Springfield, IL, USA",
        "designation": "Senior Software Engineer",
    },
    "jane.smith@example.com": {
        "fullname": "Jane Smith",
        "phone": "+1-202-555-0199",
        "email": "jane.smith@example.com",
        "address": "456 Oak Avenue, Austin, TX, USA",
        "designation": "Product Manager",
    },
    "alex.kim@example.com": {
        "fullname": "Alex Kim",
        "phone": "+91-98765-43210",
        "email": "alex.kim@example.com",
        "address": "789 Park Lane, Kolkata, WB, India",
        "designation": "Data Scientist",
    },
}


@mcp.tool()
def get_user_details(email: str) -> dict:
    """Return user details (fullname, phone, email, address, designation) for a given email ID."""
    user = USERS.get(email.lower().strip())
    if not user:
        return {"error": f"No user found with email: {email}"}
    return user


@mcp.tool()
def get_current_time() -> dict:
    """Return the current server time."""
    now = datetime.now()
    return {
        "iso": now.isoformat(),
        "readable": now.strftime("%Y-%m-%d %H:%M:%S"),
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)