import os
import glob

directory = 'd:/Srinivas/petwebsitenew'
old_str = '<span class="font-heading font-semibold text-2xl tracking-tight text-teal-400">Paw<span class="text-indigo-400">Luxe</span></span>'
new_str = '''<div>
            <span class="font-heading font-semibold text-2xl tracking-tight text-teal-400 block">Paw<span class="text-indigo-400">Luxe</span></span>
            <span class="block text-[10px] uppercase tracking-widest text-slate-400 font-medium">Pet Spa & Salon</span>
          </div>'''

for filepath in glob.glob(os.path.join(directory, '*.html')):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Updated {filepath}')
