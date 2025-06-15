from audioop import error


def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["code"],
        "source": "flake8",
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "passed" if not errors else "failed",
        "errors": [
            {
                "line": error["line_number"],
                "column": error["column_number"],
                "message": error["text"],
                "name": error["code"],
                "source": "flake8",
            }
            for error in errors
        ]
    }


def format_linter_report(linter_report: dict) -> list:
    return [
        {
            "path": path,
            "status": "passed" if not error_list else "failed",
            "errors": [
                {
                    "line": error["line_number"],
                    "column": error["column_number"],
                    "message": error["text"],
                    "name": error["code"],
                    "source": "flake8",
                }
                for error in error_list
            ]
        }
        for path, error_list in linter_report.items()
    ]
