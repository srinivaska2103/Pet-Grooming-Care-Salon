import re
import os

html_files = [
    "index.html",
    "home2.html",
    "aboutus.html",
    "services.html",
    "gallery.html",
    "pricing.html",
    "contact.html",
    "booknow.html",
    "dashboard.html",
    "login.html",
    "signup.html",
    "comingsoon.html",
    "404.html"
]

# SVG Paw Print
paw_svg = """<svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">
              <path d="M11 20a2 2 0 1 0-4 0a2 2 0 0 0 4 0zm5 0a2 2 0 1 0-4 0a2 2 0 0 0 4 0zM4 14a2 2 0 1 0 0-4a2 2 0 0 0 0 4zm16 0a2 2 0 1 0 0-4a2 2 0 0 0 0 4zM12 5a2 2 0 1 0 0-4a2 2 0 0 0 0 4zm0 9a3 3 0 1 1-6 0c0-2.5 3-4.5 3-4.5s3 2 3 4.5z"/>
            </svg>"""

brand_name_span = '<span class="font-heading font-semibold text-2xl tracking-tight text-teal-600 dark:text-teal-400">PawLuxe</span>'

def update_file(filename):
    print(f"Processing {filename}...")
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    orig_content = content

    # 1. Replace the book SVG
    # Matches <svg ... viewBox="0 0 24 24"> ... d="M12 6.253v13... ... </svg>
    svg_pattern = re.compile(
        r'<svg\s+class="w-6\s+h-6"\s+fill="none"\s+stroke="currentColor"\s+viewBox="0\s+0\s+24\s+24">.*?'
        r'd="M12\s+6\.253v13m0-13C10\.832.*?d="M12\s+6\.253v13m0-13C10\.832[^"]+".*?'
        r'</svg>',
        re.DOTALL
    )
    
    # We can also do a simpler match since the d attribute path is very unique:
    # Match <svg ...> containing the path
    content_new, count = re.subn(
        r'<svg[^>]*viewBox="0\s+0\s+24\s+24"[^>]*>\s*<path[^>]*d="M12\s+6\.253v13m0-13C10\.832.*?/path>\s*</svg>',
        paw_svg,
        content,
        flags=re.DOTALL
    )
    print(f"  Replaced {count} open book SVGs")
    content = content_new

    # In case there are other book SVGs with self-closing or slight formatting variations:
    content_new, count = re.subn(
        r'<svg[^>]*>\s*<path[^>]*d="M12\s+6\.253v13m0-13C10\.832[^"]+"[^>]*>\s*</path>\s*</svg>',
        paw_svg,
        content,
        flags=re.DOTALL
    )
    if count:
        print(f"  Replaced {count} other SVGs")
        content = content_new

    # Special replacement for 404 emoji logo to paw SVG
    if filename == "404.html":
        content_new, count = re.subn(
            r'<div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-teal-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-teal-500/25">\s*🐾\s*</div>',
            f'<div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-teal-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-teal-500/25">{paw_svg}</div>',
            content,
            flags=re.DOTALL
        )
        print(f"  Replaced emoji logo in 404.html: {count}")
        content = content_new

    # 2. Replace brand name Paw<span...>Luxe</span> spans
    # Match any <span class="...tracking-tight...">Paw<span class="...">Luxe</span></span>
    # First: text-slate-900 dark:text-white / text-white containing PawLuxe
    content_new, count = re.subn(
        r'<span class="font-heading font-semibold text-2xl tracking-tight (?:text-slate-900 dark:text-white|text-white)">\s*Paw\s*<span\s+class="text-teal-600 dark:text-teal-400">Luxe</span>\s*</span>',
        brand_name_span,
        content,
        flags=re.DOTALL
    )
    print(f"  Replaced {count} brand name spans (type 1)")
    content = content_new

    content_new, count = re.subn(
        r'<span class="font-heading font-semibold text-2xl tracking-tight text-white">\s*Paw\s*<span\s+class="text-teal-600 dark:text-teal-400">Luxe</span>\s*</span>',
        brand_name_span,
        content,
        flags=re.DOTALL
    )
    print(f"  Replaced {count} brand name spans (type 2)")
    content = content_new

    # Let's also do a generic replacement for any Paw<span class="text-teal-600 dark:text-teal-400">Luxe</span> spans with standard brand classes:
    content_new, count = re.subn(
        r'<span class="font-heading font-semibold text-2xl tracking-tight[^"]*">\s*Paw\s*<span\s+class="text-teal-600 dark:text-teal-400">Luxe</span>\s*</span>',
        brand_name_span,
        content,
        flags=re.DOTALL
    )
    print(f"  Replaced {count} brand name spans (type 3)")
    content = content_new

    # 3. Add dark class to footers so that the brand name stays light-mode/dark-mode compatible
    # Replace <footer class="bg-slate-900 text-slate-400 pt-16 pb-6 border-t border-slate-800">
    # with <footer class="bg-slate-900 text-slate-400 pt-16 pb-6 border-t border-slate-800 dark">
    content_new, count = re.subn(
        r'<footer class="bg-slate-900 text-slate-400 pt-16 pb-6 border-t border-slate-800">',
        '<footer class="bg-slate-900 text-slate-400 pt-16 pb-6 border-t border-slate-800 dark">',
        content
    )
    print(f"  Added 'dark' class to {count} footers")
    content = content_new

    # Check for the alternative footer definition in case it differs:
    content_new, count = re.subn(
        r'<footer class="bg-slate-900 text-slate-400 pt-16 pb-12 border-t border-slate-800 mt-auto">',
        '<footer class="bg-slate-900 text-slate-400 pt-16 pb-12 border-t border-slate-800 mt-auto dark">',
        content
    )
    if count:
        print(f"  Added 'dark' class to {count} alternative footers")
        content = content_new

    if content != orig_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Updated {filename} successfully.")
    else:
        print(f"  No changes made to {filename}.")

for file in html_files:
    if os.path.exists(file):
        update_file(file)
    else:
        print(f"File {file} not found")
