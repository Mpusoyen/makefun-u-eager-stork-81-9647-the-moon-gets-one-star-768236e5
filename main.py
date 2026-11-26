"""A one-star review of the Moon, saved to the make.fun output file.

No input is read; the program emits a single 114-character line
with no trailing newline at the end.
"""

import os


def build_review_line():
    """Return the review line, assembled from its three clauses."""
    rating = "1/5 stars."
    complaint = (
        "Promised moonlight romance; delivered a rock that "
        "photobombs telescopes and leaves at 4am."
    )
    verdict = "No re-orbit."
    return " ".join([rating, complaint, verdict])


def output_path():
    """Resolve where entry.txt goes from the environment."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def write_review(path):
    """Create parent dirs as needed and write the line verbatim."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(build_review_line())


if __name__ == "__main__":
    write_review(output_path())
