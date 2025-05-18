# Test Executor Service

This is the **Test Executor** microservice of the test automation platform. It receives JSON test configurations from the gateway, converts them into `.robot` files, runs them via Robot Framework, and returns the results.

## ⚙️ Features

- Converts JSON configs to `.robot` scripts
- Executes tests with Robot Framework
- Returns result logs and status
- Async support with Celery
- Supports custom keywords
- Modular service structure

## 📁 Project Structure

```bash
test_executor/
├── app/
│   ├── config/                     # Settings and configuration
│   ├── custom_energy_keywords/    # Custom Robot Framework keywords
│   ├── models/                    # Pydantic models
│   ├── results/                   # Result handling utilities
│   ├── routes/                    # API endpoints
│   ├── services/                  # Business logic and test conversion
│   ├── tasks/                     # Celery tasks
│   ├── main.py                    # FastAPI entry point
│   └── __init__.py
├── generated_tests/               # Auto-generated .robot test files
├── libraries/                     # Shared Robot Framework libraries
├── resources/                     # Resource files for Robot tests
├── results/                       # Output results (log.html, output.xml, etc.)
├── schemas/                       # Data schemas (if separate from models)
├── celery_app.py                  # Celery app instance
├── Dockerfile
├── .env
├── .gitignore
├── log.html
├── output.xml
├── report.html
├── requirements.txt
└── README.md
```


## 🚀 Running Locally
1. Clone the repo and set up a virtual environment:
```bash
git clone https://github.com/abdi-ali1/test_executor.git
cd test_executor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Start the API:

```bash
uvicorn app.main:app --reload
```

3. (Optional) Start Celery worker:
```bash
celery -A celery_app.celery worker --loglevel=info
```


## ✨ Example JSON Payload
Endpoint: POST /v1/execute/run

```json
{
  "json_config": {
    "name": "login_test",
    "steps": [
      { "keyword": "Open Browser", "args": ["https://example.com", "chrome"] },
      { "keyword": "Input Text", "args": ["id=username", "abdi"] },
      { "keyword": "Click Button", "args": ["id=submit"] }
    ],
    "context": {
      "headless": true
    }
  }
}
```

## ✨ Environment Variables
Endpoint: POST /v1/execute/run

```env
OUTPUT_DIR=./results
ROBOT_OPTIONS=--outputdir ./results
```

## 🔧 Tech Stack
* Python 3.10+
* FastAPI
* Robot Framework
* Celery
* httpx
* Pydantic


## 🔧 TODO / Roadmap
* Result persistence in PostgreSQL
* Execution monitoring endpoint
* File cleanup cron job
* Retry logic for flaky tests

## 👤 Author
Abdi Ali
GitHub: @abdi-ali1