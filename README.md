# CICD and DevOps

This repository serves as playground for the CICD and DevOps workshop at ScaDS.AI GA 09.2025

## Fork and Clone the Github Repository

* Fork the repository into your GitHub account
* Clone your fork locally
```bash
git clone https://github.com/path/to/your/fork.git
```

### Project Structure

- `app/` - Source code with gradio app, analysis modules and data
- `tests/` - Test files
- `scripts/` - Utility scripts
- `devops-conda-env.yml` - Conda environment file
- `pyproject.toml` - Python project and tools configuration
- `.github/workflows/ci.yml` - CICD configuration for Github Actions
- `gitlab-ci.yml` - CICD configuration equivalent for GitLab

## Local Development Setup

### Conda Environment Setup

Create (or update) and activate the conda environment using:

```bash
conda env update -f devops-conda-env.yml --prune
conda activate dataweek-devops-env
```

### Development and Testing Requirements

Before submitting changes, complete these steps locally:

#### Code Style and Linting

```bash
ruff check
```
Identifies code style violations and linting errors using ruff.

```bash
ruff check --fix
```
Identifies code style violations and linting errors, tries to fix them automatically.

#### Test Execution and Test Coverage Verification

```bash
pytest --cov=app --cov-report=xml --cov-report=term
```
Runs implemented tests with pytest located in `tests`.

Checks test coverage for implemented classes and creates coverage reports as xml and in terminal.

```bash
python scripts/check_test_coverage.py
```
Evaluates test coverage report to ensure all analysis modules have corresponding test implementations.

## Run the App

```bash
python -m app.main
```
Run the Gradio app locally.
