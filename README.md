# Devtools

A lightweight collection of personal CLI tools for Python projects.

Currently includes utilities for inspecting project size, virtual environments,
and disk usage, designed to work seamlessly with `uv`.

## Installation

### Local Development

```bash
uv sync
```

### Use In Another Project

```bash
uv add git+https://github.com/musicalchemist/devtools.git
```

## Available Commands

### `space`

Inspect disk usage for your current project.

```bash
uv run space
```

Output includes:

- Total project size
- `.venv` size
- Largest installed packages
- `uv` cache size
- Disk usage summary

## Project Structure

```text
devtools/
  src/devtools/
    check_space.py
  pyproject.toml
```

## Requirements

- Python 3.13+
- `uv`

Install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Philosophy

This repo is meant to be:

- Simple
- Reusable across projects
- Focused on developer productivity

Instead of copying scripts between projects, install once and reuse everywhere.

## Future Tools

Planned commands:

- `clean` - remove caches and temp files
- `envinfo` - show Python and environment details
- `tree` - clean project tree output
- `depsize` - dependency size breakdown

## License

MIT
