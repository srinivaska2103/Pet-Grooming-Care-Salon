import glob
import re

files = glob.glob('*.html')

cta_html = """
      <div class="mt-auto pt-8 border-t border-slate-200/50 dark:border-slate-800/50 flex flex-col space-y-4">
        <div class="flex items-center gap-4">
          <button type="button" aria-label="Toggle Theme" class="theme-toggle-btn w-10 h-10 flex items-center justify-center rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300">
            <svg class="theme-icon-sun w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
            <svg class="theme-icon-moon w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
          </button>
          <button type="button" aria-label="Toggle Direction" class="dir-toggle-btn px-4 h-10 flex items-center justify-center rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300">
            <span class="dir-toggle-label">LTR</span>
          </button>
        </div>
        <a href="login.html" class="w-full h-12 flex items-center justify-center rounded-xl bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-400 font-semibold text-sm">Login</a>
        <a href="booknow.html" class="w-full h-12 flex items-center justify-center rounded-xl bg-gradient-to-r from-teal-600 to-indigo-600 text-white font-semibold text-sm shadow-md">Book Now</a>
      </div>
    </div>
  </header>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. Change md:flex to lg:flex for the header CTAs so they are hidden on tablet
    content = content.replace('hidden md:flex items-center gap-3', 'hidden lg:flex items-center gap-3')
    
    # 2. Fix the drawer's wrapper class to avoid overlap issues
    # From: class="hidden lg:hidden fixed inset-0 top-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md z-50 px-6 py-6 space-y-4"
    # To: class="hidden lg:hidden absolute left-0 right-0 top-full h-[calc(100vh-5rem)] overflow-y-auto bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl z-50 px-6 py-8 flex flex-col"
    drawer_regex = r'class="hidden lg:hidden fixed inset-0 top-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md z-50 px-6 py-6 space-y-4"'
    new_drawer_class = 'class="hidden lg:hidden absolute left-0 right-0 top-full h-[calc(100vh-5rem)] overflow-y-auto bg-white/95 dark:bg-slate-900/95 backdrop-blur-xl z-50 px-6 py-8 flex flex-col border-t border-slate-200/50 dark:border-slate-800/50"'
    content = re.sub(drawer_regex, new_drawer_class, content)
    
    # 3. Inject CTAs at the bottom of the drawer
    # We find the end of the mobile drawer (</div> </div> </header> structure)
    # The current drawer ends with:
    #       </div>
    #     </div>
    #   </header>
    if cta_html not in content:
        content = re.sub(r'</div>\s*</div>\s*</header>', '</div>' + cta_html, content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
