"""Tasks for maintaining the project.

Execute 'invoke --list' for guidance on using Invoke
"""

import platform
from pathlib import Path
from typing import Any, List, Optional

from invoke import call, task
from invoke.context import Context
from invoke.runners import Result

ROOT_DIR = Path(__file__).parent
DOCS_BUILD_DIR = ROOT_DIR.joinpath("site")
PYTHON_TARGETS = [
    Path(__file__),
]
PYTHON_TARGETS_STR = " ".join([str(p) for p in PYTHON_TARGETS])
MOLECULE_DIR = ROOT_DIR / "molecule"
ROLES_DIR = ROOT_DIR / "roles"
PLAYBOOKS_DIR = ROOT_DIR / "playbooks"
META_DIR = ROOT_DIR / "meta"
ANSIBLE_TARGETS = [MOLECULE_DIR, ROLES_DIR, PLAYBOOKS_DIR, META_DIR]
ANSIBLE_TARGETS_STR = " ".join([str(t) for t in ANSIBLE_TARGETS])


def _run(c: Context, command: str, env: dict[str, Any] | None = None) -> Optional[Result]:
    return c.run(command, pty=platform.system() != "Windows", env=env)


@task()
def clean_python(c: Context) -> None:
    """Clean up python file artifacts."""
    _run(c, "find . -name '*.pyc' -exec rm -f {} +")
    _run(c, "find . -name '*.pyo' -exec rm -f {} +")
    _run(c, "find . -name '*~' -exec rm -f {} +")
    _run(c, "find . -name '__pycache__' -exec rm -fr {} +")


@task()
def clean_docs(c: Context) -> None:
    """Clean up files from documentation builds."""
    _run(c, f"rm -fr {DOCS_BUILD_DIR}")


@task(pre=[clean_python, clean_docs])
def clean(c: Context) -> None:
    """Run all clean sub-tasks."""


@task()
def install_hooks(c: Context) -> None:
    """Install pre-commit hooks."""
    _run(c, "poetry run pre-commit install")


@task()
def hooks(c: Context) -> None:
    """Run pre-commit hooks."""
    _run(c, "poetry run pre-commit run --all-files")


@task(
    help={
        "force": "Force overwriting an existing role or collection. (default: False)",
    }
)
def galaxy_install(c: Context, force: bool = False) -> None:
    """Install ansible-galaxy requirements."""
    install_options = ["--force"] if force else []
    _run(c, f"poetry run ansible-galaxy install -r requirements.yml {' '.join(install_options)}")


@task(name="format", help={"check": "Checks if source is formatted without applying changes"})
def format_(c: Context, check: bool = False) -> None:
    """Format code."""
    isort_options = ["--check-only", "--diff"] if check else []
    _run(c, f"poetry run isort {' '.join(isort_options)} {PYTHON_TARGETS_STR}")
    black_options = ["--diff", "--check"] if check else ["--quiet"]
    _run(c, f"poetry run black {' '.join(black_options)} {PYTHON_TARGETS_STR}")


@task()
def ruff(c: Context) -> None:
    """Run ruff."""
    _run(c, f"poetry run ruff check {PYTHON_TARGETS_STR}")


@task()
def security(c: Context) -> None:
    """Run security related checks."""
    _run(
        c,
        "poetry export --with dev --format=requirements.txt --without-hashes | "
        "poetry run safety check --stdin --full-report",
    )


@task()
def yamllint(c: Context) -> None:
    """Run yamllint, a linter for YAML files."""
    _run(c, f"poetry run yamllint -c {ROOT_DIR / '.yamllint'} {ROOT_DIR}")


@task()
def ansible_lint(c: Context) -> None:
    """Run ansible linter."""
    lint_options = ["--force-color", "-p", "-v", "--project-dir", str(ROOT_DIR)]
    _run(c, f"poetry run ansible-lint {' '.join(lint_options)} {ANSIBLE_TARGETS_STR}")


@task(pre=[ruff, security, call(format_, check=True), yamllint, ansible_lint])
def lint(c: Context) -> None:
    """Run all linting."""


@task()
def mypy(c: Context) -> None:
    """Run mypy."""
    _run(c, f"poetry run mypy {PYTHON_TARGETS_STR}")


@task()
def tests(c: Context) -> None:
    """Run ansible molecule test."""
    _run(c, "poetry run molecule test")


@task(
    help={
        "target": "Ansible playbook to run. (default: main)",
        "tag": "Only run plays and tasks tagged with these values",
        "skip_tag": "Only run plays and tasks whose tags do not match these values",
        "list_tags": "List all available tags",
        "ask_pass": "Ask for connection password",
        "ask_become_pass": "Ask for privilege escalation password",
    },
    iterable=["tag", "skip_tag"],
)
def playbook(
    c: Context,
    tag: List[str],
    skip_tag: List[str],
    list_tags: bool = False,
    target: str = "main",
    ask_pass: bool = False,
    ask_become_pass: bool = False,
) -> None:
    """Run Ansible playbooks, executing the defined tasks on the targeted hosts."""
    playbook_options = ["-i", "inventory"]
    if tag:
        playbook_options += ["--tags", f'"{ ",".join(tag) }"']
    if skip_tag:
        playbook_options += ["--skip-tags", f'"{ ",".join(skip_tag) }"']
    if list_tags:
        playbook_options.append("--list-tags")
    if ask_pass:
        playbook_options.append("--ask-pass")
    if ask_become_pass:
        playbook_options.append("--ask-become-pass")
    _run(c, f"poetry run ansible-playbook playbooks/{target}.yml {' '.join(playbook_options)}")


@task(
    help={
        "serve": "Build the docs watching for changes",
        "open_browser": "Open the docs in the web browser",
    }
)
def docs(c: Context, serve: bool = False, open_browser: bool = False) -> None:
    """Build documentation."""
    mkdocs_options = ["--clean"]
    if serve:
        if open_browser:
            mkdocs_options.append("--open")
        _run(c, f"mkdocs serve {' '.join(mkdocs_options)}")
    else:
        _run(c, f"mkdocs build {' '.join(mkdocs_options)}")


@task(
    help={
        "part": "Part of the version to be bumped.",
        "dry_run": "Don't write any files, just pretend. (default: False)",
    }
)
def version(c: Context, part: str, dry_run: bool = False) -> None:
    """Bump version."""
    bump_options = ["--dry-run"] if dry_run else []
    _run(c, f"poetry run bump2version {' '.join(bump_options)} {part}")
