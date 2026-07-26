# ⚡ CodePulse — Codebase Health & Time Machine Visualizer

> An interactive full-stack developer tool built with **Python**, **FastAPI**, and **Chart.js** to analyze AST code complexity and track codebase evolution across Git commit history.

---

## 🌟 Key Features

- 📊 **AST Code Analysis:** Parses Python files using standard Abstract Syntax Tree (`ast`) to detect functions, classes, and line counts.
- 📉 **Cyclomatic Complexity Scoring:** Utilizes `radon` to compute cyclomatic complexity scores for functions and classes in real-time.
- 🕒 **Git Time Machine:** Integrates with `GitPython` to extract commit history, author metadata, timestamps, and commit messages.
- 🎨 **Interactive Dark-Mode Dashboard:** Responsive frontend built with **Tailwind CSS** and **Chart.js** providing visual bar charts and detailed complexity breakdowns.
- ⚡ **Asynchronous REST API:** High-performance backend powered by **FastAPI** with auto-generated OpenAPI documentation.

---

## 🛠️ Tech Stack

| Domain | Technologies Used |
| :--- | :--- |
| **Backend** | Python 3.11+, FastAPI, Uvicorn, Radon, GitPython, AST |
| **Frontend** | HTML5, Tailwind CSS, JavaScript (Fetch API), Chart.js |
| **VCS / Tools** | Git, GitHub, VS Code |

---

## 🚀 Getting Started Locally

Follow these step-by-step instructions to get a local copy up and running on your machine.

### Prerequisites
Make sure you have **Python 3.10+** and **Git** installed on your system.

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<YOUR-GITHUB-USERNAME>/code-pulse.git
cd code-pulse