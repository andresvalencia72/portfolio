// Theme toggle
(function() {
  const root = document.documentElement;
  const toggle = document.getElementById('themeToggle');
  let saved = null;
  try { saved = localStorage.getItem('pf-theme'); } catch (e) {}
  const theme = saved || 'light';
  root.setAttribute('data-theme', theme);

  toggle.addEventListener('click', function() {
    const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('pf-theme', next); } catch (e) {}
  });
})();

// Nav scroll
(function() {
  const header = document.getElementById('header');
  const onScroll = function() {
    if (window.scrollY > 16) {
      header.classList.add('header--scrolled');
    } else {
      header.classList.remove('header--scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();

// Mobile menu
(function() {
  const menu = document.getElementById('mobileMenu');
  const burger = document.getElementById('burgerBtn');
  const close = document.getElementById('menuClose');

  burger.addEventListener('click', function() {
    menu.classList.add('mobile-menu--open');
  });
  close.addEventListener('click', function() {
    menu.classList.remove('mobile-menu--open');
  });
  menu.querySelectorAll('[data-mobile-nav]').forEach(function(a) {
    a.addEventListener('click', function() {
      menu.classList.remove('mobile-menu--open');
    });
  });
})();

// Active nav link
(function() {
  const links = document.querySelectorAll('[data-nav]');
  const sections = document.querySelectorAll('[data-section]');
  const obs = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        var id = entry.target.id;
        links.forEach(function(a) {
          var on = a.getAttribute('href') === '#' + id;
          a.classList.toggle('header__nav-link--active', on);
        });
      }
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(function(s) { obs.observe(s); });
})();
// Form submit feedback
(function() {
  var btn = document.getElementById('submitBtn');
  var label = document.getElementById('submitLabel');
  btn.addEventListener('click', function() {
    var orig = label.textContent;
    label.textContent = '¡Gracias! Te respondo pronto';
    btn.style.opacity = '.85';
    setTimeout(function() {
      label.textContent = orig;
      btn.style.opacity = '1';
    }, 2600);
  });
})();
