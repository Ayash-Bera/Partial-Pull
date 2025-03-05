# Vacuum

A simple tool to perform sparse checkouts from Git repositories, allowing you to clone only specific folders or files from a repository.

## Installation

You can install Vacuum using pip:

```bash
pip install vacuum
```

## Usage

```bash
vacuum https://github.com/username/repository
```

When prompted, enter the subdirectories or file paths you want to clone, separated by commas.

Example:

```
Enter the subdirectories (or file paths) to clone, separated by commas: src/components, README.md, docs/api
```

## Features

- Clone only specific folders or files from a Git repository
- Simple interactive interface
- Supports both main and master branches
- Perfect for when you only need parts of a large repository

## License

MIT
