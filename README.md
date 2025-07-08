# Moodle MCP

A Moodle integration using FastMCP that provides a set of tools to interact with Moodle's Web Services API. This project allows programs like Claude or Cursor to interact with Moodle.

## Features

- Fetch assignments
- Get site information
- Access enrolled courses
- View course contents
- Get forum discussions
- Check assignment submissions
- View calendar events
- Access course grades
- Handle messages and notifications
- Look up course information

## Prerequisites

- Python 3.7+
- Moodle instance with Web Services enabled
- Moodle API token

## Installation

1. Clone the repository:
```bash
git clone https://github.com/gecitemre/moodle-mcp.git
cd moodle-mcp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Moodle configuration:
```env
MOODLE_URL=https://your-moodle-instance.com
MOODLE_TOKEN=your_moodle_token
```

## Usage

Run the MCP server:

```bash
python main.py
```

## Environment Variables

- `MOODLE_URL`: The base URL of your Moodle instance
- `MOODLE_TOKEN`: Your Moodle Web Services API token

## License

MIT 