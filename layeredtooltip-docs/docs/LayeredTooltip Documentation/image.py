import os
from PIL import Image

# 시작 경로 (예: 문서 폴더)
root_folder = os.getcwd()
quality = 90  # 0~100, 일반적으로 80~90이 적당

# 재귀적으로 모든 하위 폴더 탐색
for dirpath, _, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.lower().endswith(".webp"):
            png_path = os.path.join(dirpath, filename)
            webp_filename = os.path.splitext(filename)[0] + ".webp"
            webp_path = os.path.join(dirpath, webp_filename)

            # 이미 webp가 있으면 건너뜀 (선택 사항)
            if os.path.exists(webp_path):
                print(f"⚠️ 이미 존재: {webp_path}")
                continue

            try:
                with Image.open(png_path) as img:
                    img.save(webp_path, "webp", quality=quality)
                print(f"✅ 변환됨: {png_path} → {webp_path}")
            except Exception as e:
                print(f"❌ 실패: {png_path} ({e})")
