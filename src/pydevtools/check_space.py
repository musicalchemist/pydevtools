from pathlib import Path
import subprocess


def shell(command: str) -> str:
    try:
        return subprocess.check_output(
            command,
            shell=True,
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except subprocess.CalledProcessError:
        return "Not found"


def section(title: str) -> None:
    print(f"\n{'=' * 60}")
    print(title)
    print("=" * 60)


def main() -> None:
    project = Path.cwd()

    section("Project Size")
    print(shell(f"du -sh {project}"))

    section(".venv Size")
    print(shell("du -sh .venv 2>/dev/null || echo '.venv not found'"))

    section("Largest Packages")
    print(shell("du -sh .venv/lib/python*/site-packages/* 2>/dev/null | sort -hr | head -n 15"))

    section("uv Cache Size")
    print(shell("du -sh ~/.cache/uv 2>/dev/null || echo 'uv cache not found'"))

    section("Disk Space")
    print(shell("df -h ."))

    print("\nDone.")


if __name__ == "__main__":
    main()