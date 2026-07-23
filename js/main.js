/**
 * PawLuxe - Premium Pet Grooming & Care Salon
 * Main JavaScript Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initTheme();
  initDirection();
  initNavbar();
  initMobileMenu();
  initAccordions();
  initTabs();
  initAnimatedCounters();
  initBookingWizard();
  initDashboardMobileMenu();
});

/* ==========================================================
   1. Theme Toggle (Dark / Light Mode)
   ========================================================== */
function initTheme() {
  const savedTheme = localStorage.getItem('pawluxe_theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }

  updateThemeIcons();

  const themeToggles = document.querySelectorAll('.theme-toggle-btn');
  themeToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');
      const isDark = document.documentElement.classList.contains('dark');
      localStorage.setItem('pawluxe_theme', isDark ? 'dark' : 'light');
      updateThemeIcons();
    });
  });
}

function updateThemeIcons() {
  const isDark = document.documentElement.classList.contains('dark');
  const sunIcons = document.querySelectorAll('.theme-icon-sun');
  const moonIcons = document.querySelectorAll('.theme-icon-moon');

  sunIcons.forEach(icon => icon.classList.toggle('hidden', !isDark));
  moonIcons.forEach(icon => icon.classList.toggle('hidden', isDark));
}

/* ==========================================================
   2. LTR / RTL Toggle
   ========================================================== */
function initDirection() {
  const savedDir = localStorage.getItem('pawluxe_dir') || 'ltr';
  document.documentElement.setAttribute('dir', savedDir);
  updateDirButtons(savedDir);

  const dirToggles = document.querySelectorAll('.dir-toggle-btn');
  dirToggles.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentDir = document.documentElement.getAttribute('dir') || 'ltr';
      const newDir = currentDir === 'ltr' ? 'rtl' : 'ltr';
      document.documentElement.setAttribute('dir', newDir);
      localStorage.setItem('pawluxe_dir', newDir);
      updateDirButtons(newDir);
    });
  });
}

function updateDirButtons(dir) {
  const dirLabels = document.querySelectorAll('.dir-toggle-label');
  dirLabels.forEach(label => {
    label.textContent = dir.toUpperCase();
  });
}

/* ==========================================================
   3. Sticky Navbar & Active Navigation State
   ========================================================== */
function initNavbar() {
  const navbar = document.getElementById('main-header');
  if (navbar) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 20) {
        navbar.classList.add('shadow-md', 'backdrop-blur-md', 'bg-white/90', 'dark:bg-slate-900/90');
        navbar.classList.remove('bg-transparent');
      } else {
        navbar.classList.remove('shadow-md');
      }
    });
  }

  // Active Link Highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('text-teal-600', 'dark:text-teal-400', 'font-semibold');
      link.classList.remove('text-slate-600', 'dark:text-slate-300');
    }
  });
}

/* ==========================================================
   4. Mobile Menu Drawer Toggle
   ========================================================== */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }
}

/* ==========================================================
   4.b Dashboard Mobile Menu Toggle
   ========================================================== */
function initDashboardMobileMenu() {
  const dashMenuBtn = document.getElementById('dashboard-menu-btn');
  const dashSidebar = document.getElementById('dashboard-sidebar');

  if (dashMenuBtn && dashSidebar) {
    dashMenuBtn.addEventListener('click', () => {
      dashSidebar.classList.toggle('hidden');
    });

    // Close the sidebar when any navigation link is clicked (on mobile)
    const dashLinks = dashSidebar.querySelectorAll('a');
    dashLinks.forEach(link => {
      link.addEventListener('click', () => {
        dashSidebar.classList.add('hidden');
      });
    });
  }
}

/* ==========================================================
   5. Accordion (FAQ) Logic
   ========================================================== */
function initAccordions() {
  const accordionTriggers = document.querySelectorAll('.accordion-header');
  
  accordionTriggers.forEach(trigger => {
    trigger.addEventListener('click', () => {
      const content = trigger.nextElementSibling;
      const icon = trigger.querySelector('.accordion-icon');
      
      const isOpen = !content.classList.contains('hidden');
      
      // Close other accordion items in the same container
      const parent = trigger.closest('.accordion-group');
      if (parent) {
        parent.querySelectorAll('.accordion-content').forEach(el => el.classList.add('hidden'));
        parent.querySelectorAll('.accordion-icon').forEach(el => el.classList.remove('rotate-180'));
      }

      if (!isOpen) {
        content.classList.remove('hidden');
        if (icon) icon.classList.add('rotate-180');
      }
    });
  });
}

/* ==========================================================
   6. Interactive Filtering Tabs (Gallery, Pricing, Dashboard)
   ========================================================== */
function initTabs() {
  const tabContainers = document.querySelectorAll('[data-tabs]');
  
  tabContainers.forEach(container => {
    const tabButtons = container.querySelectorAll('[data-tab-target]');
    const tabItems = container.querySelectorAll('[data-tab-category]');
    
    tabButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        if(btn.tagName === 'A' && btn.getAttribute('href') === '#') {
          e.preventDefault();
        }
        
        const target = btn.getAttribute('data-tab-target');
        
        tabButtons.forEach(b => {
          b.classList.remove('bg-teal-600', 'text-white', 'shadow-md', 'shadow-lg');
          b.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300');
          b.classList.remove('font-semibold');
        });
        
        btn.classList.add('bg-teal-600', 'text-white', 'shadow-md', 'font-semibold');
        btn.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-600', 'dark:text-slate-300', 'hover:bg-slate-100', 'dark:hover:bg-slate-800');

        tabItems.forEach(item => {
          const category = item.getAttribute('data-tab-category');
          if (target === 'all' || category === target) {
            item.classList.remove('hidden');
          } else {
            item.classList.add('hidden');
          }
        });
      });
    });
  });
}

/* ==========================================================
   7. Animated Counter Logic
   ========================================================== */
function initAnimatedCounters() {
  const counters = document.querySelectorAll('.counter-val');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const counter = entry.target;
        const target = +counter.getAttribute('data-target');
        const duration = 2000;
        const stepTime = 20;
        const steps = duration / stepTime;
        const increment = target / steps;
        let current = 0;

        const timer = setInterval(() => {
          current += increment;
          if (current >= target) {
            counter.textContent = target.toLocaleString();
            clearInterval(timer);
          } else {
            counter.textContent = Math.ceil(current).toLocaleString();
          }
        }, stepTime);

        obs.unobserve(counter);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

/* ==========================================================
   8. Multi-Step Booking Flow Logic (Book Now Page)
   ========================================================== */
function initBookingWizard() {
  const wizard = document.getElementById('booking-wizard');
  if (!wizard) return;

  const steps = wizard.querySelectorAll('.wizard-step');
  const stepIndicators = wizard.querySelectorAll('.step-indicator');
  let currentStep = 1;

  window.goToWizardStep = function(stepNum) {
    if (stepNum < 1 || stepNum > steps.length) return;
    
    steps.forEach((step, idx) => {
      step.classList.toggle('hidden', idx + 1 !== stepNum);
    });

    stepIndicators.forEach((ind, idx) => {
      const stepIndex = idx + 1;
      const circle = ind.querySelector('.step-circle');
      if (stepIndex <= stepNum) {
        circle.classList.add('bg-teal-600', 'text-white', 'border-teal-600');
        circle.classList.remove('bg-slate-100', 'dark:bg-slate-800', 'text-slate-400', 'border-slate-300');
      } else {
        circle.classList.remove('bg-teal-600', 'text-white', 'border-teal-600');
        circle.classList.add('bg-slate-100', 'dark:bg-slate-800', 'text-slate-400', 'border-slate-300');
      }
    });

    currentStep = stepNum;
  };
}
