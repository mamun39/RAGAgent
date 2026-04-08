# Promptfoo Eval Harness

This directory holds the baseline Promptfoo setup for exercising the local `POST /api/query` endpoint without using the Streamlit UI.

## Purpose

- provide a small, repeatable smoke test for the external query API
- establish the folder structure for future eval datasets, scenarios, and assertions
- keep the first eval step limited to harmless baseline checks

## Assumptions

- the FastAPI app is already running locally on `http://127.0.0.1:8000`
- the `POST /api/query` endpoint from Step 1 is available
- the local app is configured so it can answer a normal query

## Install Promptfoo

One option:

```powershell
npm install -g promptfoo
```

Or run it without a global install:

```powershell
npx promptfoo@latest --help
```

## Run The Smoke Eval

From the repository root:

```powershell
npx promptfoo@latest eval -c evals/promptfoo/promptfooconfig.yaml
```

## What The Baseline Covers

- sends a normal query to the local `POST /api/query` endpoint
- checks that the HTTP response is successful
- checks that the response body is valid JSON with the expected top-level fields
- checks that `answer` is non-empty

Adversarial suites, role-differential checks, and security-focused attack datasets will be added in later steps.
