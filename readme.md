Repository to practice basic llm integrations for local and online environments, chats, models and data manipulation.

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
cp .env.example .env  # fill in GEMINI_API_KEY, LOCAL_LLM_API_KEY, GROQ_API_KEY as needed
```

## Deactivate

`deactivate`

## Layout

- `src/ai_exercises/services/` — thin wrappers around each LLM backend (Gemini, local LM Studio).
- `src/ai_exercises/exercises/` — one module per exercise, each with a `main()` entry point.
- `data/raw/` — input files consumed by the exercises; `data/generated/` — their (gitignored) output.
- `tests/` — pytest suite; tests that require a live external service are marked `integration`.

## Running an exercise

Each exercise is installed as a console script (see `[project.scripts]` in `pyproject.toml`), e.g.:

```
product-revenue
questions-and-answers
reviews-challenge
```

Or run a module directly: `python -m ai_exercises.exercises.product_revenue`.

## Tests

```
pytest            # unit tests only (integration tests are skipped automatically)
pytest -m integration   # also run tests that need a live local LLM server
```
