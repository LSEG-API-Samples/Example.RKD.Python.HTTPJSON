# RKD Python Project Instructions

## Overview
This project contains Python scripts for the Knowledge Direct (RKD) API client. All code follows a functional, service-oriented architecture pattern with REST/WebSocket authentication and request handling.

---

## Code Quality Standards

### 1. **Function Organization**
- Use **function-based design** (no classes unless absolutely necessary for WebSocket handlers)
- Organize code in logical flow: **Credentials → Authentication → Service Requests**
- Always include `if __name__ == '__main__':` entry point in executable scripts
- Extract repeated logic into reusable helper functions (e.g., `doSendRequest()` for HTTP operations)

### 2. **Naming Conventions**
- Function names: `PascalCase` for API-related functions (e.g., `CreateAuthorization()`, `RetrieveQuotes()`)
- Variable names: `snake_case` for standard variables
- Constants: `UPPER_SNAKE_CASE`
- Avoid abbreviations; be explicit (e.g., `token_endpoint` not `tk_ep`)

### 3. **Documentation Requirements**
- **Legal notice**: Include the triple-quoted disclaimer block at the top of every file
- **Function docstrings**: Add docstrings to ALL functions in Google style:
  ```python
  def RetrieveQuotes(token, ric_list):
      """Fetch quote data for given RICs from the Quote service.
      
      Args:
          token (str): Authentication token from CreateAuthorization()
          ric_list (list): List of RIC codes (e.g., ['AAPL.O', 'IBM.N'])
          
      Returns:
          dict: JSON response containing quote data, or None on failure
      """
  ```
- **Section headers**: Use `## -------- Description --------` format for logical sections
- **Inline comments**: Explain *why*, not *what*; use `#` prefix

### 4. **Error Handling**
- Wrap HTTP requests in try-except blocks catching `requests.exceptions.RequestException`
- Check HTTP status codes: `if result.status_code == 200` for success
- Print descriptive error messages to aid debugging
- Exit gracefully with `sys.exit(1)` on fatal errors
- Always call `result.raise_for_status()` for non-200 responses

**Example pattern:**
```python
try:
    result = doSendRequest(url, headers, body)
    if result.status_code == 200:
        return result.json()
    else:
        print(f"Error: {result.status_code} - {result.text}")
        sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    sys.exit(1)
```

---

## Authentication Pattern (CRITICAL)

### Token-Based Authentication
1. **Credential Loading Priority:**
   - Environment variables from `.env` file (via `python-dotenv`)
   - User input via `getpass.getpass()` (passwords only, never print)
   - Fail gracefully if credentials unavailable

2. **Header Format:**
   - `X-Trkd-Auth-Token`: OAuth token from `CreateAuthorization()`
   - `X-Trkd-Auth-ApplicationID`: Application identifier
   - Include in all service requests

3. **Token Lifecycle:**
   - Call `CreateAuthorization()` once per session
   - Token expires (include expiration check if token returned expiry)
   - Handle token refresh if service requires re-authentication

**Example:**
```python
# Load credentials
username = os.getenv('TRKD_USERNAME')
password = getpass.getpass("Enter password: ")

# Get token
token = CreateAuthorization(username, password)

# Use token in all subsequent requests
headers = {
    'X-Trkd-Auth-Token': token,
    'X-Trkd-Auth-ApplicationID': app_id,
    'Content-Type': 'application/json'
}
```

---

## Code Style & Implementation

### Imports
- Group in standard order: standard library → third-party → local modules
- Place all imports at the top of file (except dynamic imports in specific functions)

### Logging
- Use `print()` statements for output (established pattern in project)
- Format informative messages for users running scripts
- Print errors to stderr; use explicit status messages

### HTTP Requests
- Use the `doSendRequest()` helper function to abstract POST logic
- Pass URL, headers dict, and JSON body separately
- Always set `'Content-Type': 'application/json'` in headers
- Use `json=` parameter in `requests.post()`, not `data=`

### Credential Management
- Never hardcode credentials in source code
- Always load from environment variables or user input
- Use `getpass.getpass()` for password input (doesn't echo to terminal)
- Load `.env` file at script start with `load_dotenv()`

---

## When Making Changes

### Adding New Features
1. Follow the function-first design pattern
2. Add docstrings immediately (required)
3. Implement error handling around HTTP operations
4. Test with both successful and failed API responses
5. Update README with usage examples

### Modifying Existing Functions
- Maintain the authentication pattern
- Keep `try-except` structure around requests
- Preserve section header comments
- Update docstrings if parameters/return values change

### Creating New Scripts
- Copy the legal disclaimer from existing files
- Include `if __name__ == '__main__':` entry point
- Organize: imports → functions → main block
- Load credentials early, authenticate once

---

## Dependencies
- `requests`: HTTP/REST operations
- `websocket-client`: WebSocket streaming (for *_wsstreaming*.py scripts)
- `python-dotenv`: Environment variable loading from `.env`
- `python-dateutil`: Date parsing and manipulation
- Standard library: `json`, `sys`, `os`, `getpass`, `threading`, `time`

---

## Explanation Principles
When working with this codebase, prioritize clarity and educational value:
- **Explain the 'why'**: Decisions about authentication flow, error handling, or architecture
- **Reference patterns**: Point to existing examples when introducing patterns
- **Be thorough**: Describe impacts on existing code or token lifecycle
- **Document trade-offs**: If suggesting alternatives, explain the rationale
