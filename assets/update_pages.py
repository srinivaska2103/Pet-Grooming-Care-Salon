import os
import glob

# HTML files to update
files = glob.glob('*.html')
files = [f for f in files if f not in ['login.html', 'signup.html', 'dashboard.html']]

nav_target = """      <!-- UTILITY & CTAS -->
      <div class="hidden md:flex items-center lg:gap-2 xl:gap-4">
        <!-- Dark Mode Toggle -->
        <button type="button" aria-label="Toggle Theme" class="theme-toggle-btn p-2 lg:p-1.5 xl:p-2.5 rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 transition-colors">
          <svg class="theme-icon-sun w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
          <svg class="theme-icon-moon w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>

        <!-- LTR/RTL Toggle -->
        <button type="button" aria-label="Toggle Direction" class="dir-toggle-btn px-2 lg:px-1.5 xl:px-3 py-1.5 rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
          <span class="dir-toggle-label">LTR</span>
        </button>

        <!-- Login Link -->
        <a href="login.html" class="text-sm lg:text-xs xl:text-sm font-medium text-slate-600 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 transition-colors px-2 lg:px-1 xl:px-3 py-2">Login</a>

        <!-- Book Now CTA -->
        <a href="booknow.html" class="px-5 lg:px-3 xl:px-5 py-2.5 lg:py-2 xl:py-2.5 rounded-xl bg-gradient-to-r from-teal-600 to-indigo-600 hover:from-teal-500 hover:to-indigo-500 text-white font-medium text-sm lg:text-xs xl:text-sm shadow-md shadow-teal-500/20 hover:shadow-lg hover:shadow-teal-500/30 transition-all hover:-translate-y-0.5">
          Book Now
        </a>
      </div>"""

nav_replace = """      <!-- UTILITY & CTAS -->
      <div class="hidden md:flex items-center gap-3">
        <!-- Dark Mode Toggle -->
        <button type="button" aria-label="Toggle Theme" class="theme-toggle-btn w-10 h-10 flex items-center justify-center rounded-xl bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-300 hover:text-teal-600 dark:hover:text-teal-400 transition-colors">
          <svg class="theme-icon-sun w-5 h-5 hidden" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z"></path></svg>
          <svg class="theme-icon-moon w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"></path></svg>
        </button>

        <!-- LTR/RTL Toggle -->
        <button type="button" aria-label="Toggle Direction" class="dir-toggle-btn px-3 h-10 flex items-center justify-center rounded-xl border border-slate-200 dark:border-slate-800 text-xs font-semibold text-slate-600 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors">
          <span class="dir-toggle-label">LTR</span>
        </button>

        <!-- Login Link -->
        <a href="login.html" class="w-[100px] lg:w-[90px] xl:w-[100px] h-10 flex items-center justify-center rounded-xl bg-indigo-50 text-indigo-600 dark:bg-indigo-500/10 dark:text-indigo-400 hover:bg-indigo-100 dark:hover:bg-indigo-500/20 transition-colors font-medium text-sm lg:text-xs xl:text-sm">Login</a>

        <!-- Book Now CTA -->
        <a href="booknow.html" class="w-[100px] lg:w-[90px] xl:w-[100px] h-10 flex items-center justify-center rounded-xl bg-gradient-to-r from-teal-600 to-indigo-600 hover:from-teal-500 hover:to-indigo-500 text-white font-medium text-sm lg:text-xs xl:text-sm shadow-md shadow-teal-500/20 hover:shadow-lg hover:shadow-teal-500/30 transition-all hover:-translate-y-0.5">
          Book Now
        </a>
      </div>"""

footer_logo_target = """          <a href="index.html" class="flex items-center gap-3 group">
            <div class="w-10 h-10 rounded-2xl bg-gradient-to-tr from-teal-500 to-indigo-500 flex items-center justify-center text-white font-bold shadow-lg shadow-teal-500/20">
              🐾
            </div>
            <span class="font-heading font-semibold text-2xl text-white">Paw<span class="text-teal-400">Luxe</span></span>
          </a>"""

footer_logo_replace = """          <a href="index.html" class="flex items-center gap-3 group">
            <div class="w-11 h-11 rounded-2xl bg-gradient-to-tr from-teal-600 to-indigo-600 flex items-center justify-center text-white shadow-lg shadow-teal-500/25 group-hover:scale-105 transition-transform">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path>
              </svg>
            </div>
            <span class="font-heading font-semibold text-2xl tracking-tight text-white">Paw<span class="text-teal-600 dark:text-teal-400">Luxe</span></span>
          </a>"""

footer_contact_target = """        <!-- Col 4: Contact Info -->
        <div>
          <h5 class="font-heading font-semibold text-white text-base mb-4">Salon Location</h5>
          <p class="text-sm text-slate-400 mb-2 leading-relaxed">124 Luxury Paw Way, Suite 400<br/>Beverly Hills, CA 90210</p>
          <p class="text-sm text-slate-400 mb-1">📞 (800) 555-PAWS</p>
          <p class="text-sm text-slate-400">✉️ hello@pawluxe.com</p>
        </div>"""

footer_contact_replace = """        <!-- Col 4: Newsletter -->
        <div>
          <h5 class="font-heading font-semibold text-white text-base mb-4">Newsletter</h5>
          <p class="text-sm text-slate-400 mb-4 leading-relaxed">Subscribe to get special offers, free giveaways, and once-in-a-lifetime deals.</p>
          <form class="flex flex-col gap-3" onsubmit="event.preventDefault();">
            <input type="email" placeholder="Enter your email" required class="w-full px-4 py-2.5 rounded-xl bg-slate-800 border border-slate-700 text-sm text-white focus:outline-none focus:border-teal-500 focus:ring-1 focus:ring-teal-500 transition-colors" />
            <button type="submit" class="w-full py-2.5 rounded-xl bg-gradient-to-r from-teal-600 to-indigo-600 hover:from-teal-500 hover:to-indigo-500 text-white font-medium text-sm transition-colors">Subscribe</button>
          </form>
        </div>"""

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    if nav_target in content:
        content = content.replace(nav_target, nav_replace)
        modified = True
    
    if footer_logo_target in content:
        content = content.replace(footer_logo_target, footer_logo_replace)
        modified = True
        
    if footer_contact_target in content:
        content = content.replace(footer_contact_target, footer_contact_replace)
        modified = True

    if modified:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
