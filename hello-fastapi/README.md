# Hello FastAPI

A minimal FastAPI Hello World application using uv for dependency management.

## Project Structure

```
hello-fastapi/
├── main.py           # FastAPI application
├── pyproject.toml    # Project dependencies (uv)
└── requirements.txt  # Legacy pip requirements (optional)
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- uv (already installed at `~/.local/bin/uv`)

To add uv to your PATH permanently, add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then restart your shell or run: `source ~/.bashrc`

### Running the Application

1. Navigate to the project directory:
   ```bash
   cd hello-fastapi
   ```

2. Activate the virtual environment created by uv:
   ```bash
   source .venv/bin/activate
   ```

3. Start the development server:
   ```bash
   fastapi dev main.py
   ```

   Or run directly with uv:
   ```bash
   ~/.local/bin/uv run fastapi dev main.py
   ```

4. Open your browser and visit:
   - API: http://127.0.0.1:8000
   - Interactive docs: http://127.0.0.1:8000/docs
   - Alternative docs: http://127.0.0.1:8000/redoc

## Available Endpoints

- `GET /` - Returns a Hello World message
- `GET /health` - Health check endpoint

## Managing Dependencies

### Add a new dependency

```bash
~/.local/bin/uv add <package-name>
```

### Remove a dependency

```bash
~/.local/bin/uv remove <package-name>
```

### Update dependencies

```bash
~/.local/bin/uv sync
```

### Lock dependencies

```bash
~/.local/bin/uv lock
```

## Next Steps

- Add more endpoints in `main.py`
- Add a database (SQLAlchemy)
- Add authentication
- Add tests

For more advanced features, check out the other fastapi-builder templates:
- `standard` - Includes database and CRUD operations
- `auth` - Includes JWT authentication
- `production` - Includes Docker, tests, and production configuration
