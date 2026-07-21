import os
import glob
import re

files = glob.glob('*.html')
files = [f for f in files if f not in ['404.html']]

# Standard LOGO block for NAV
nav_logo_standard = """      <!-- LOGO -->
      <a href="index.html" class="flex items-center gap-3 group">
        <div
          class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-teal-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-teal-500/25 group-hover:scale-105 transition-transform">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253">
            </path>
          </svg>
        </div>
        <div>
          <span class="font-heading font-semibold text-2xl tracking-tight text-slate-900 dark:text-white">Paw<span
              class="text-teal-600 dark:text-teal-400">Luxe</span></span>
          <span class="block text-[10px] uppercase tracking-widest text-slate-400 font-medium">Pet Spa & Salon</span>
        </div>
      </a>"""

# Standard LOGO block for FOOTER
footer_logo_standard = """          <!-- Footer Logo -->
          <a href="index.html" class="flex items-center gap-3 group">
            <div
              class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-teal-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-teal-500/25 group-hover:scale-105 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                  d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253">
                </path>
              </svg>
            </div>
            <span class="font-heading font-semibold text-2xl tracking-tight text-white">Paw<span
                class="text-teal-600 dark:text-teal-400">Luxe</span></span>
          </a>"""

# Standard CTAs
ctas_standard = """      <!-- UTILITY & CTAS -->
      <div class="hidden md:flex items-center gap-3">
        <!-- Dark Mode Toggle -->
        <button type="button" aria-label="Toggle Theme"
          class="theme-toggle-btn w-10 h-10 flex items-center justify-center rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 transition-colors">
          <svg class="theme-icon-sun w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z">
            </path>
          </svg>
          <svg class="theme-icon-moon w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
              d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path>
          </svg>
        </button>

        <!-- LTR/RTL Toggle -->
        <button type="button" aria-label="Toggle Direction"
          class="dir-toggle-btn px-3 h-10 flex items-center justify-center rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
          <span class="dir-toggle-label">LTR</span>
        </button>

        <!-- Login Link -->
        <a href="login.html"
          class="w-[100px] lg:w-[90px] xl:w-[100px] h-10 flex items-center justify-center rounded-xl bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-400 hover:bg-indigo-100 dark:hover:bg-indigo-500/20 transition-colors font-medium text-sm lg:text-xs xl:text-sm">Login</a>

        <!-- Book Now CTA -->
        <a href="booknow.html"
          class="w-[100px] lg:w-[90px] xl:w-[100px] h-10 flex items-center justify-center rounded-xl bg-gradient-to-r from-teal-600 to-indigo-600 hover:from-teal-500 hover:to-indigo-500 text-white font-medium text-sm lg:text-xs xl:text-sm shadow-md shadow-teal-500/20 hover:shadow-lg hover:shadow-teal-500/30 transition-all hover:-translate-y-0.5">
          Book Now
        </a>
      </div>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    modified = False

    # 1. Replace nav logo
    new_content = re.sub(
        r'(<a href="index\.html" class="flex items-center gap-3 group">).*?(</a>)',
        nav_logo_standard,
        content,
        count=1,
        flags=re.DOTALL
    )
    if new_content != content:
        content = new_content
        modified = True

    # 2. Make Desktop Nav Responsive
    new_content = re.sub(
        r'<nav class="hidden lg:flex items-center (?:gap-\d+|lg:gap-\d+ xl:gap-\d+)">',
        r'<nav class="hidden lg:flex items-center lg:gap-3 xl:gap-7">',
        content
    )
    if new_content != content:
        content = new_content
        modified = True
        
    # Replace all nav link text sizes to be responsive
    # e.g., class="nav-link text-sm font-medium... -> class="nav-link text-sm lg:text-xs xl:text-sm font-medium...
    # But only inside the <nav ...> ... </nav> block!
    nav_match = re.search(r'(<nav class="hidden lg:flex.*?>)(.*?)(</nav>)', content, flags=re.DOTALL)
    if nav_match:
        nav_inner = nav_match.group(2)
        # First, ensure we don't have lg:text-xs already to avoid double adding
        nav_inner_clean = re.sub(r' lg:text-xs xl:text-sm', '', nav_inner)
        # Then add it after text-sm
        nav_inner_updated = re.sub(r'text-sm', 'text-sm lg:text-xs xl:text-sm', nav_inner_clean)
        if nav_inner != nav_inner_updated:
            content = content[:nav_match.start(2)] + nav_inner_updated + content[nav_match.end(2):]
            modified = True

    # 3. Standardize UTILITY & CTAS
    # Find block between </nav> and <!-- MOBILE MENU BUTTON -->
    utils_match = re.search(r'(?:<!-- UTILITY & CTAS -->|<div class="hidden md:flex items-center gap-4">).*?(?=<!-- MOBILE MENU BUTTON -->|<button id="mobile-menu-btn")', content, flags=re.DOTALL)
    if utils_match:
        content = content[:utils_match.start()] + ctas_standard + '\n\n      ' + content[utils_match.end():]
        modified = True

    # 4. Standardize Footer Logo
    # Footer logo is the a href="index.html" block in the footer
    footer_logo_match = re.search(r'(<!-- Footer Logo -->\s*)?<a href="index\.html" class="flex items-center gap-3 group">.*?(</a>)', content[len(content)//2:], flags=re.DOTALL)
    if footer_logo_match:
        # We search in the second half of the document to target the footer
        idx_offset = len(content)//2
        start_idx = idx_offset + footer_logo_match.start()
        end_idx = idx_offset + footer_logo_match.end()
        content = content[:start_idx] + footer_logo_standard + content[end_idx:]
        modified = True

    # 5. Fix Mobile Drawer positioning
    # From: class="hidden lg:hidden border-t ... bg-white...
    # To: class="hidden lg:hidden fixed inset-0 top-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md z-50 px-6 py-6 space-y-4"
    mobile_drawer_regex = r'<div id="mobile-menu"[^>]*class="[^"]*"[^>]*>'
    drawer_match = re.search(mobile_drawer_regex, content)
    if drawer_match:
        replacement = '<div id="mobile-menu"\n      class="hidden lg:hidden fixed inset-0 top-20 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md z-50 px-6 py-6 space-y-4">'
        if drawer_match.group(0) != replacement:
            content = content[:drawer_match.start()] + replacement + content[drawer_match.end():]
            modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
