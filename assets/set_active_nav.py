import glob
import re

files = glob.glob('*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # Reset all links to inactive state first to ensure clean state
    # Desktop
    content = re.sub(
        r'<a href="([^"]+\.html)"\s+class="nav-link[^"]*text-teal-600[^"]*">',
        r'<a href="\1" class="nav-link text-sm lg:text-xs xl:text-sm font-medium text-slate-600 dark:text-slate-300 transition-colors hover:text-teal-600 dark:hover:text-teal-400">',
        content
    )
    
    # Mobile
    content = re.sub(
        r'<a href="([^"]+\.html)"\s+class="text-teal-600 font-semibold">',
        r'<a href="\1" class="text-slate-600 dark:text-slate-300">',
        content
    )
    
    # Now set the active state for THIS specific file
    # Desktop active:
    desktop_active = r'<a href="\1" class="nav-link text-sm lg:text-xs xl:text-sm font-medium text-teal-600 dark:text-teal-400">'
    content = re.sub(
        f'<a href="{file}"\\s+class="nav-link[^"]*">',
        f'<a href="{file}" class="nav-link text-sm lg:text-xs xl:text-sm font-medium text-teal-600 dark:text-teal-400">',
        content
    )
    
    # Mobile active:
    content = re.sub(
        f'<a href="{file}"\\s+class="text-slate-600 dark:text-slate-300">',
        f'<a href="{file}" class="text-teal-600 font-semibold">',
        content
    )
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Set active nav state in {file}")
