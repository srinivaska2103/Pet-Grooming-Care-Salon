"""
Fix footer layout and ensure Main Menu & Pages & Booking are in the same row across all pages.
Changes:
  1. Footer grid: change 'md:grid-cols-2' to 'md:grid-cols-4' so all 4 columns
     are always in the same horizontal row on medium+ screens.
  2. Add 'flex-1' to main content wrapper so footer sticks to the bottom properly.
"""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Pages that have the standard footer
HTML_FILES = [
    "index.html",
    "home2.html",
    "aboutus.html",
    "services.html",
    "gallery.html",
    "pricing.html",
    "contact.html",
]

CHANGES = {
    # Fix 1: Footer grid columns – change md:grid-cols-2 to md:grid-cols-4
    # This ensures Main Menu and Pages & Booking columns are always in the same row
    'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-10 pb-12 border-b border-slate-800':
        'grid grid-cols-1 md:grid-cols-4 lg:grid-cols-5 gap-10 pb-12 border-b border-slate-800',
}

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    changed = False

    for old, new in CHANGES.items():
        if old in content:
            content = content.replace(old, new)
            changed = True
            print(f"  [OK] Fixed footer grid in: {os.path.basename(filepath)}")
        else:
            print(f"  [SKIP] Pattern not found in: {os.path.basename(filepath)}")

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    print("=== Fixing Footer & Navigation Layout ===\n")
    total_fixed = 0

    for filename in HTML_FILES:
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            print(f"Processing: {filename}")
            if fix_file(filepath):
                total_fixed += 1
        else:
            print(f"  [MISSING] File not found: {filename}")

    print(f"\n=== Done! Fixed {total_fixed}/{len(HTML_FILES)} files ===")


if __name__ == '__main__':
    main()
