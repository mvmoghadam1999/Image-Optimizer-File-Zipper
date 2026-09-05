from pathlib import Path
import shutil


def create_zip_archive(
    input_path: str | Path,
    output_zip: str | Path,
) -> None:
    """
    Create a ZIP archive from a file or directory.

    Args:
        input_path: Path to the file or directory to compress.
        output_zip: Path of the output ZIP file.
    """
    input_path = Path(input_path)
    output_zip = Path(output_zip)

    output_zip.parent.mkdir(parents=True, exist_ok=True)

    archive_base = output_zip.with_suffix("")

    shutil.make_archive(
        str(archive_base),
        "zip",
        root_dir=input_path,
    )

    print(f"ZIP archive created at: {output_zip}")


def main() -> None:
    input_path = ""
    output_zip = ""

    create_zip_archive(
        input_path=input_path,
        output_zip=output_zip,
    )


if __name__ == "__main__":
    main()
