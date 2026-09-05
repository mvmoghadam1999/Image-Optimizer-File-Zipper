from pathlib import Path
from PIL import Image


SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".bmp", ".gif"}


def reduce_image_quality(
    input_image_path: str | Path,
    output_image_path: str | Path,
    quality: int = 50,
    resize_factor: float = 0.8,
) -> None:
    """
    Resize and reduce the quality of an image.

    Args:
        input_image_path: Path to the input image.
        output_image_path: Path where the optimized image will be saved.
        quality: Output image quality (1-100).
        resize_factor: Factor used to resize the image.
    """
    input_image_path = Path(input_image_path)
    output_image_path = Path(output_image_path)

    with Image.open(input_image_path) as image:
        width, height = image.size

        new_width = int(width * resize_factor)
        new_height = int(height * resize_factor)

        resized_image = image.resize(
            (new_width, new_height),
            Image.Resampling.LANCZOS,
        )

        resized_image.save(
            output_image_path,
            quality=quality,
        )

    print(f"Optimized image saved to: {output_image_path}")


def process_images_in_folder(
    input_folder_path: str | Path,
    output_folder_path: str | Path,
    quality: int = 50,
    resize_factor: float = 0.8,
) -> None:
    """
    Process all supported images in a folder.

    Args:
        input_folder_path: Folder containing the original images.
        output_folder_path: Folder where optimized images will be saved.
        quality: Output image quality (1-100).
        resize_factor: Factor used to resize images.
    """
    input_folder = Path(input_folder_path)
    output_folder = Path(output_folder_path)

    output_folder.mkdir(parents=True, exist_ok=True)

    for image_path in input_folder.iterdir():
        if image_path.is_file() and image_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            output_image_path = output_folder / image_path.name

            reduce_image_quality(
                input_image_path=image_path,
                output_image_path=output_image_path,
                quality=quality,
                resize_factor=resize_factor,
            )


def main() -> None:
    input_folder_path = ""
    output_folder_path = ""

    process_images_in_folder(
        input_folder_path=input_folder_path,
        output_folder_path=output_folder_path,
        quality=50,
        resize_factor=0.8,
    )


if __name__ == "__main__":
    main()
