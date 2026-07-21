import glob
import re

files = glob.glob('*.html')

# The original CTA block starts with a specific div and ends where my newly injected one starts, or we can just capture it by looking for the flex items-center justify-between.
# Looking at index.html:
#       <div class="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">
#         ...
#       </div>
#       <div class="mt-auto pt-8 border-t border-slate-200/50 dark:border-slate-800/50 flex flex-col space-y-4">

regex = r'<div class="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">.*?</div>\s*(?=<div class="mt-auto pt-8 border-t)'

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We need to make sure we don't accidentally delete other similar divs, 
    # but since it's immediately preceding the 'mt-auto' block we added, it's safe.
    
    # Actually, a better regex is one that specifically matches the exact structure inside the drawer.
    # The drawer ends with:
    # </div>
    # <div class="mt-auto pt-8...
    # We want to remove the div block before the mt-auto.
    # Let's use a non-greedy match from pt-4 border-t up to the mt-auto div.
    
    pattern = r'<div class="pt-4 border-t border-slate-200 dark:border-slate-800 flex items-center justify-between">.*?</div>\s*?(?=<div class="mt-auto pt-8)'
    new_content, count = re.subn(pattern, '', content, flags=re.DOTALL)
    
    if count > 0:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file} - removed {count} duplicate CTA block(s)")
