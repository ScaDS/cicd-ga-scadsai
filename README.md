# CICD and DevOps

This repository serves as playground for the CICD and DevOps workshop at ScaDS.AI GA 09.2025

## Fork and Clone the Github Repository

* Fork the repository into your GitHub account, copy the default branch `develop` only
* In your fork, enable Actions -> Workflows 
* Clone your fork locally
```bash
git clone https://github.com/path/to/your/fork.git
```
* You can now work on your fork

### Project Structure

- `app/` - Source code with gradio app, analysis modules and data
- `tests/` - Test files
- `scripts/` - Utility scripts
- `devops-conda-env.yml` - Conda environment file
- `pyproject.toml` - Python project and tools configuration
- `.github/workflows/ci.yml` - CICD configuration for Github Actions
- `.gitlab-ci.yml` - CICD configuration equivalent for GitLab
- `Dockerfile` - Dockerization of the application

## Local Development Setup

### Conda Environment Setup

Create (or update) and activate the conda environment using:

```bash
conda env update -f devops-conda-env.yml --prune
conda activate devops-env
```

### Development and Testing Requirements

Before submitting changes, complete these steps locally:

#### Code Style and Linting

Identifies code style violations and linting errors using ruff:

```bash
ruff check
```

Identifies code style violations and linting errors, tries to fix them automatically:

```bash
ruff check --fix
```

#### Test Execution and Test Coverage Verification

Runs implemented tests with pytest located in `tests` and creates test coverage reports for classes located in `app` as coverage.xml and in terminal:

```bash
pytest --cov=app --cov-report=xml --cov-report=term
```

Evaluates test coverage report to ensure all analysis modules have corresponding test implementations:

```bash
python scripts/check_test_coverage.py
```

#### Local CICD Testing with act

[act](https://nektosact.com/) allows to run GitHub Actions workflows locally inside Docker containers. This is useful for testing pipelines (e.g., .github/workflows/ci.yml) before pushing those changes to GitHub.

* Install act like described: https://nektosact.com/installation/index.html
* Make sure Docker is running on your system
* List available jobs for a workflow: ```act -l```
* Run all jobs as if pushing to the current branch: ```act push```
* See more in the docs: https://nektosact.com/usage/index.html

## Run the App

Runs the Gradio app locally:

```bash
python -m app.main
```
