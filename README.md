# HR Skills - Claude Code Skills Collection

A curated collection of Claude Code skills for productivity and development.

## 🚀 Featured Skill: FastAPI Builder

**Progressive FastAPI development from hello world to production-ready applications.**

### Key Features
- **4 Progressive Templates:** Minimal → Standard → Auth → Production
- **Auto-generate CRUD endpoints** for any model
- **Complete authentication** with JWT, user management
- **Production-ready** with Docker, tests, deployment guides
- **Multiple databases:** SQLite, PostgreSQL, MongoDB

### Quick Start
```bash
# Create a new FastAPI project
python3 .claude/skills/fastapi-builder/scripts/init_project.py my-api --template minimal

# Generate CRUD endpoints
python3 .claude/skills/fastapi-builder/scripts/generate_crud.py Product --fields "name:str,price:float"

# Run your API
cd my-api
pip install -r requirements.txt
fastapi dev main.py
```

**Templates:**
- **Minimal** - Hello world (2 files) - Learn FastAPI basics
- **Standard** - Database + CRUD (14 files) - SQLAlchemy integration
- **Auth** - JWT authentication (24 files) - Protected routes
- **Production** - Docker + Tests (33 files) - Deployment ready

📚 **[View Full Documentation](.claude/skills/fastapi-builder/SKILL.md)**

---

## 📚 All Available Skills

| Skill | Purpose |
|-------|---------|
| **fastapi-builder** ⭐ | Progressive FastAPI development with 4 templates, CRUD generator, auth, testing, and Docker deployment |
| **browser-use** | Browser automation using Playwright MCP for web scraping, testing, and form submission |
| **context7-efficient** | Token-efficient library documentation fetcher with 77% token savings |
| **doc-coauthoring** | Structured workflow for co-authoring documentation, proposals, and technical specs |
| **docx** | Word document creation and editing with tracked changes and formatting |
| **internal-comms** | Templates for status reports, newsletters, FAQs, and incident reports |
| **pdf** | PDF manipulation: extract text, merge, split, fill forms |
| **pptx** | PowerPoint presentation creation and editing |
| **skill-creator** | Guide for creating new Claude Code skills |
| **theme-factory** | Style artifacts with 10 pre-set themes or custom generation |
| **xlsx** | Spreadsheet operations with formulas, formatting, and analysis |

---

## 🎯 Installation

### Clone Repository
```bash
git clone https://github.com/harisrehman155/hr-skills.git
cd hr-skills
```

### Use Skills
Skills are located in `.claude/skills/` directory. Each skill is ready to use immediately.

---

## 📖 Usage

Each skill contains:
- **SKILL.md** - Main documentation and usage guide
- **scripts/** - Executable helper scripts
- **references/** - Detailed guides and patterns
- **assets/** - Templates, boilerplate code, resources

Example:
```bash
# FastAPI Builder - Create project
python3 .claude/skills/fastapi-builder/scripts/init_project.py my-app --template production

# FastAPI Builder - Generate CRUD
python3 .claude/skills/fastapi-builder/scripts/generate_crud.py Task --fields "title:str,done:bool"
```

---

## 🛠️ Repository Structure

```
hr-skills/
├── README.md
└── .claude/
    └── skills/
        ├── fastapi-builder/          ⭐ Full FastAPI development workflow
        │   ├── SKILL.md
        │   ├── scripts/
        │   │   ├── init_project.py
        │   │   └── generate_crud.py
        │   ├── references/
        │   │   ├── database-patterns.md
        │   │   ├── auth-guide.md
        │   │   ├── testing-guide.md
        │   │   └── deployment.md
        │   └── assets/
        │       └── templates/
        │           ├── minimal/
        │           ├── standard/
        │           ├── auth/
        │           └── production/
        ├── browser-use/
        ├── context7-efficient/
        ├── skill-creator/
        └── ... (other skills)
```

---

## 🔗 Resources

- **FastAPI:** [fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- **Claude Code:** [claude.com/claude-code](https://claude.com/claude-code)
- **Learning Material:** [AI Native Development](https://ai-native.panaversity.org/docs/AI-Tool-Landscape/claude-code-features-and-workflows)

---

## 👤 Author

**Haris Rehman**
- GitHub: [@harisrehman155](https://github.com/harisrehman155)

---

Built with ❤️ using Claude Code
# Task-Management-API-Skills-Development
