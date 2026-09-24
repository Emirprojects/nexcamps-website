/* NEXCAMP site scripts */
(function () {
  const header = document.querySelector('.header');
  const burger = document.querySelector('.burger');
  const mobileNav = document.querySelector('.mobile-nav');
  const toTop = document.querySelector('.to-top');

  // Sticky header state
  const onScroll = () => {
    if (header && !header.classList.contains('inner')) {
      header.classList.toggle('solid', window.scrollY > 40);
    }
    if (toTop) toTop.classList.toggle('show', window.scrollY > 600);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  if (burger && mobileNav) {
    burger.addEventListener('click', () => {
      const open = mobileNav.classList.toggle('open');
      document.body.classList.toggle('menu-open', open);
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileNav.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
      mobileNav.classList.remove('open');
      document.body.classList.remove('menu-open');
    }));
  }

  // Back to top
  if (toTop) toTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  // Reveal on scroll
  const reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(el => io.observe(el));
  } else {
    reveals.forEach(el => el.classList.add('in'));
  }

  // Active nav link
  const path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav a, .mobile-nav a').forEach(a => {
    const href = a.getAttribute('href');
    if (href === path) a.classList.add('active');
  });

  // Forms: Netlify-compatible AJAX submit with graceful fallback to email
  document.querySelectorAll('form[data-form]').forEach(form => {
    form.addEventListener('submit', async (ev) => {
      ev.preventDefault();
      const msg = form.querySelector('.form-msg');
      const btn = form.querySelector('button[type=submit]');
      const original = btn.innerHTML;
      btn.disabled = true; btn.textContent = 'Sending…';
      msg.classList.remove('show', 'error');
      try {
        const data = new FormData(form);
        const res = await fetch(form.getAttribute('action') || '/', { method: 'POST', body: data, headers: { 'Accept': 'application/json' } });
        if (!res.ok) throw new Error('Form endpoint returned ' + res.status);
        form.reset();
        msg.textContent = form.dataset.success || 'Thank you. Your message has been received and our team will respond shortly.';
        msg.classList.add('show');
      } catch (err) {
        // Fallback: open the visitor's email client with the message pre-filled
        const data = new FormData(form);
        let body = '';
        data.forEach((v, k) => { if (k !== 'form-name' && k !== 'bot-field' && typeof v === 'string') body += k.replace(/_/g, ' ') + ': ' + v + '\n'; });
        const subject = encodeURIComponent(form.dataset.subject || 'Website enquiry');
        window.location.href = 'mailto:info@nexcamps.com?subject=' + subject + '&body=' + encodeURIComponent(body);
        msg.textContent = 'Opening your email app to send this enquiry to info@nexcamps.com. If it does not open, please email us directly.';
        msg.classList.add('show');
      } finally {
        btn.disabled = false; btn.innerHTML = original;
      }
    });
  });

  // Current year
  document.querySelectorAll('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
