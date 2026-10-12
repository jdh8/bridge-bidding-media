"""Export the SVG source cards to PNGs and an overview. Run from any directory."""

from pathlib import Path
import shutil
import subprocess

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parent
BG = "#101f29"


def main():
    assert shutil.which("inkscape"), "Inkscape is required to render SVGs."
    svg_paths = sorted((ROOT / "svg").glob("*.svg"))
    assert svg_paths, "No SVG source cards found in svg/."
    (ROOT / "png").mkdir(exist_ok=True)
    overview = Image.new("RGB", (1440, ((len(svg_paths) + 2) // 3) * 510), BG)
    draw = ImageDraw.Draw(overview)
    for index, svg_path in enumerate(svg_paths, 1):
        png_path = ROOT / "png" / f"{svg_path.stem}.png"
        subprocess.run(["inkscape", str(svg_path), "--export-area-page", "--export-dpi=96",
                        f"--export-filename={png_path}"], check=True, capture_output=True)
        with Image.open(png_path) as picture:
            thumb = picture.convert("RGB")
            thumb.thumbnail((480, 480), Image.Resampling.LANCZOS)
        x, y = (index - 1) % 3 * 480, (index - 1) // 3 * 510
        overview.paste(thumb, (x + (480 - thumb.width) // 2, y + (480 - thumb.height) // 2))
        draw.text((x + 12, y + 487), svg_path.stem, fill="white")
    overview.save(ROOT / "overview.jpg", quality=92)
    print(f"Exported {len(svg_paths)} SVGs to PNGs and overview.jpg; SVG sources unchanged.")


if __name__ == "__main__":
    main()
