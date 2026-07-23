import os

files = ['d:/Srinivas/petwebsitenew/index.html', 'd:/Srinivas/petwebsitenew/home2.html']
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace('<span class="text-xs text-slate-500">Max\'s Mom', '<span class="text-xs text-slate-500 dark:text-slate-400">Max\'s Mom')
    content = content.replace('<span class="text-xs text-slate-500">Cleo\'s Dad', '<span class="text-xs text-slate-500 dark:text-slate-400">Cleo\'s Dad')
    content = content.replace('<span class="text-xs text-slate-500">Bella\'s Mom', '<span class="text-xs text-slate-500 dark:text-slate-400">Bella\'s Mom')
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done')
