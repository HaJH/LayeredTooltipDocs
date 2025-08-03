import re
import argparse
from pathlib import Path
from urllib.parse import quote

IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif"}

def find_image_path(image_name: str, assets_root: Path) -> Path | None:
    for path in assets_root.rglob("*"):
        if path.is_file() and path.name == image_name:
            return path
    return None

def convert_obsidian_links(md_path: Path, assets_root: Path, dry_run: bool):
    original_text = md_path.read_text(encoding="utf-8")
    converted_text = original_text

    matches = re.findall(r'!\[\[(.*?)\]\]', original_text)
    for match in matches:
        image_name = Path(match).name
        if Path(image_name).suffix.lower() not in IMAGE_EXTENSIONS:
            continue

        image_path = find_image_path(image_name, assets_root)
        if image_path:
            rel_path = image_path.relative_to(assets_root.parent)
            # URL 인코딩 적용 (공백 → %20 등)
            rel_path_str = quote(str(rel_path).replace("\\", "/"))
            replacement = f"![{image_name}](/{rel_path_str})"
            converted_text = converted_text.replace(f"![[{match}]]", replacement)
        else:
            print(f"[!] {image_name} not found in {assets_root}")

    if converted_text != original_text:
        if dry_run:
            print(f"\n--- Draft change for {md_path} ---\n")
            print(converted_text)
        else:
            md_path.write_text(converted_text, encoding="utf-8")
            print(f"[✔] Updated: {md_path}")

def run_conversion(target_dir: str, assets_dir: str, dry_run: bool):
    target_path = Path(target_dir)
    assets_path = Path(assets_dir)

    for md_file in target_path.rglob("*.md"):
        convert_obsidian_links(md_file, assets_path, dry_run)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-dir", default=".", help="Markdown directory to process")
    parser.add_argument("-assets", required=True, help="Assets root directory (e.g. static/image)")
    parser.add_argument("-draft", action="store_true", help="Only print changes without writing")
    args = parser.parse_args()

    run_conversion(args.dir, args.assets, args.draft)
