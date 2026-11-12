#!/usr/bin/env python3
"""Compose App Store images around genuine iRana Cams simulator captures."""

import base64
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCENES = (
    ("cameras", "01-cameras.jpg", ("Your cameras,", "at a glance."), "See status and details side by side."),
    ("dashboard", "02-dashboard.jpg", ("Bring your views", "together."), "Arrange supported streams in a dashboard."),
    ("live-view", "03-live-view.jpg", ("Open a camera.", "Take control."), "PTZ is available on compatible cameras."),
)
DEVICES = {
    "iphone": {
        "width": 1206,
        "height": 2622,
        "screen_width": 960,
        "screen_y": 480,
        "eyebrow_y": 95,
        "title_y": (220, 310),
        "subtitle_y": 390,
        "title_size": 78,
        "subtitle_size": 29,
    },
    "ipad": {
        "width": 2064,
        "height": 2752,
        "screen_width": 1660,
        "screen_y": 450,
        "eyebrow_y": 105,
        "title_y": (235, 335),
        "subtitle_y": 405,
        "title_size": 86,
        "subtitle_size": 34,
    },
}


def screenshot_svg(image_path: Path, device: dict, title_lines: tuple[str, str], subtitle: str) -> str:
    width = device["width"]
    height = device["height"]
    screen_width = device["screen_width"]
    screen_height = round(screen_width * height / width)
    bezel = 14
    frame_width = screen_width + bezel * 2
    frame_height = screen_height + bezel * 2
    frame_x = (width - frame_width) // 2
    frame_y = device["screen_y"]
    screen_x = frame_x + bezel
    screen_y = frame_y + bezel
    image = base64.b64encode(image_path.read_bytes()).decode("ascii")
    title_one, title_two = title_lines

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <filter id="shadow" x="-20%" y="-10%" width="140%" height="130%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="24"/>
      <feOffset dy="18"/>
      <feComponentTransfer><feFuncA type="linear" slope=".2"/></feComponentTransfer>
      <feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="screen">
      <rect x="{screen_x}" y="{screen_y}" width="{screen_width}" height="{screen_height}" rx="46"/>
    </clipPath>
  </defs>
  <rect width="{width}" height="{height}" fill="#f5f8fc"/>
  <circle cx="{round(width * .86)}" cy="{round(height * .15)}" r="{round(width * .31)}" fill="#c6eee2" opacity=".65"/>
  <circle cx="{round(width * .08)}" cy="{round(height * .31)}" r="{round(width * .17)}" fill="#d9e5fc" opacity=".75"/>
  <text x="{width // 2}" y="{device['eyebrow_y']}" text-anchor="middle" fill="#4a6f9c" font-family="Arial, Helvetica, sans-serif" font-size="29" font-weight="700" letter-spacing="3">iRana Cams  /  Demo Mode</text>
  <text x="{width // 2}" y="{device['title_y'][0]}" text-anchor="middle" fill="#172033" font-family="Arial, Helvetica, sans-serif" font-size="{device['title_size']}" font-weight="700" letter-spacing="-2">{title_one}</text>
  <text x="{width // 2}" y="{device['title_y'][1]}" text-anchor="middle" fill="#172033" font-family="Arial, Helvetica, sans-serif" font-size="{device['title_size']}" font-weight="700" letter-spacing="-2">{title_two}</text>
  <text x="{width // 2}" y="{device['subtitle_y']}" text-anchor="middle" fill="#5c687b" font-family="Arial, Helvetica, sans-serif" font-size="{device['subtitle_size']}">{subtitle}</text>
  <rect x="{frame_x}" y="{frame_y}" width="{frame_width}" height="{frame_height}" rx="62" fill="#121a2a" filter="url(#shadow)"/>
  <image x="{screen_x}" y="{screen_y}" width="{screen_width}" height="{screen_height}" preserveAspectRatio="none" clip-path="url(#screen)" href="data:image/png;base64,{image}"/>
</svg>"""


def main() -> None:
    for device_name, device in DEVICES.items():
        for scene, filename, title_lines, subtitle in SCENES:
            source = ROOT / "app-store" / "source" / device_name / f"{scene}.png"
            output = ROOT / "site" / "assets" / "screenshots" / device_name / filename
            if not source.is_file():
                raise FileNotFoundError(f"Missing genuine app capture: {source}")
            output.parent.mkdir(parents=True, exist_ok=True)
            markup = screenshot_svg(source, device, title_lines, subtitle)
            with tempfile.TemporaryDirectory() as temp_dir:
                svg_path = Path(temp_dir) / "screenshot.svg"
                png_path = Path(temp_dir) / "screenshot.png"
                svg_path.write_text(markup, encoding="utf-8")
                subprocess.run(
                    [
                        "rsvg-convert",
                        "--format=png",
                        "--output",
                        str(png_path),
                        str(svg_path),
                    ],
                    check=True,
                )
                subprocess.run(
                    [
                        "magick",
                        str(png_path),
                        "-strip",
                        "-quality",
                        "92",
                        str(output),
                    ],
                    check=True,
                )
            print(f"Wrote {output.relative_to(ROOT)} ({device['width']} x {device['height']})")


if __name__ == "__main__":
    main()
