import json
from pathlib import Path
from datetime import datetime


def save_report(result):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"research_{timestamp}.json"
    file_path = reports_dir / filename

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(
                result.model_dump(),
                file,
                ensure_ascii=False,
                indent=4
            )

        print(f"\nReport saved to: {file_path}")

    except OSError as error:
        print(f"Error saving report: {error}")