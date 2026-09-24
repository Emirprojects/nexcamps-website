#!/usr/bin/env python3
"""Builds the static NEXCAMP website into ./site from shared header/footer + page content."""
import os, datetime

OUT = os.path.join(os.path.dirname(__file__), "site")
SITE_URL = "https://www.nexcamps.com"
PHONE_DISPLAY = "+971 52 820 0088"
PHONE_TEL = "+971528200088"
WA = "https://wa.me/971528200088?text=Hello%20Nexcamp%2C%20I%20would%20like%20to%20discuss%20employee%20housing%20management."
EMAIL = "info@nexcamps.com"
ADDRESS = "Office No. 8, Habshan 2, PO Box 232505, Abu Dhabi, UAE"
MAP_EMBED = "https://www.google.com/maps?q=Habshan+2,+Abu+Dhabi,+United+Arab+Emirates&z=14&output=embed"

NAV = [("index.html", "Home"), ("about.html", "About"), ("services.html", "Services"),
       ("industries.html", "Industries"), ("careers.html", "Careers"), ("contact.html", "Contact")]

ICONS = {
  "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  "wa": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.2-.7.2-1.3.2-1.4-.1-.1-.3-.2-.6-.4zM12 2C6.5 2 2 6.5 2 12c0 1.8.5 3.5 1.3 5L2 22l5.2-1.4c1.5.8 3.1 1.2 4.8 1.2 5.5 0 10-4.5 10-10S17.5 2 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3.1.8.8-3-.2-.3C4 15 3.7 13.5 3.7 12c0-4.6 3.7-8.3 8.3-8.3s8.3 3.7 8.3 8.3-3.7 8.2-8.3 8.2z"/></svg>',
  "up": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19V5M5 12l7-7 7 7"/></svg>',
  "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.5c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.8 2z"/></svg>',
  "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
  "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="m9 12 2 2 4-4"/></svg>',
  "home": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11 12 3l9 8"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/></svg>',
  "gear": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
  "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.8 4.6a5.5 5.5 0 0 0-7.8 0L12 5.7l-1-1.1a5.5 5.5 0 0 0-7.8 7.8l1 1L12 21l7.8-7.6 1-1a5.5 5.5 0 0 0 0-7.8z"/></svg>',
  "chart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="m7 15 4-4 3 3 6-7"/></svg>',
  "users": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/></svg>',
  "layers": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="m12 2 10 5-10 5L2 7l10-5z"/><path d="m2 17 10 5 10-5M2 12l10 5 10-5"/></svg>',
  "leaf": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M11 20A7 7 0 0 1 4 13c0-6 5-10 16-10-1 11-5 16-9 17z"/><path d="M4 20c4-4 7-7 12-9"/></svg>',
  "upload": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>',
}

def head(title, desc, page, image="img/camp-1.jpg", extra_ld=""):
    canonical = f"{SITE_URL}/{'' if page=='index.html' else page}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nexcamp">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE_URL}/{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f4a3a">
<link rel="icon" type="image/png" sizes="32x32" href="img/brand/icon-32.png">
<link rel="apple-touch-icon" href="img/brand/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
{extra_ld}
</head>
<body>
"""

def header(inner):
    links = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    mlinks = "".join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f"""
<header class="header{' inner' if inner else ''}">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Nexcamp home">
      <img class="arch-light" src="img/brand/arch-white.svg" alt="" width="38" height="42">
      <img class="arch-dark" src="img/brand/arch.svg" alt="" width="38" height="42">
      <span class="wordmark">NEXCAMP</span>
    </a>
    <nav class="nav" aria-label="Main">{links}<a class="btn btn-gold" href="contact.html#enquiry">Request a Proposal</a></nav>
    <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
  </div>
</header>
<div class="mobile-nav" aria-label="Mobile menu">
  {mlinks}
  <a class="btn btn-gold" href="contact.html#enquiry">Request a Proposal</a>
  <div class="contact-mini">{PHONE_DISPLAY}<br>{EMAIL}</div>
</div>
"""

def footer():
    links = "".join(f'<li><a href="{h}">{t}</a></li>' for h, t in NAV)
    return f"""
<footer class="footer">
  <div class="container">
    <div class="top">
      <div>
        <a class="brand" href="index.html"><img src="img/brand/arch-white.svg" alt="" width="42" height="46"><span><span class="wordmark">NEXCAMP</span><span class="tagline">Management and Operation of Employee Housing LLC</span></span></a>
        <p>An owner-side operating partner for workforce accommodation communities. One team, one standard, one accountable point of coordination.</p>
      </div>
      <div>
        <h4>Company</h4>
        <ul>{links}</ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="services.html#administration">Labour Camp Administration</a></li>
          <li><a href="services.html#accommodation">Accommodation Management</a></li>
          <li><a href="services.html#catering">Catering &amp; Mess Hall</a></li>
          <li><a href="services.html#housekeeping">Housekeeping &amp; Laundry</a></li>
          <li><a href="services.html#maintenance">Maintenance &amp; MEP</a></li>
          <li><a href="services.html#hse">HSE &amp; Compliance</a></li>
        </ul>
      </div>
      <div>
        <h4>Contact</h4>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li>{ADDRESS}</li>
          <li><a href="{WA}" target="_blank" rel="noopener">Chat on WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="bottom">
      <span>© <span data-year></span> Nexcamp Management and Operation of Employee Housing LLC. All rights reserved.</span>
      <span>Abu Dhabi, United Arab Emirates</span>
    </div>
  </div>
  <div class="gold-line"></div>
</footer>
<a class="wa-float" href="{WA}" target="_blank" rel="noopener" aria-label="Chat with Nexcamp on WhatsApp">{ICONS['wa']}<span>WhatsApp</span></a>
<button class="to-top" aria-label="Back to top">{ICONS['up']}</button>
<script src="js/main.js"></script>
</body>
</html>
"""

def page_hero(crumb, title, sub, img):
    return f"""
<section class="page-hero">
  <div class="media"><img src="{img}" alt=""></div>
  <div class="container content">
    <div class="crumbs"><a href="index.html">Home</a><span>/</span>{crumb}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
"""

def cta_band(img="img/community-space.jpg", title="Let’s build better communities together.", text="We are ready to support your workforce accommodation with quality living environments, accountable operations and reliable daily service."):
    return f"""
<section class="cta-band">
  <img src="{img}" alt="">
  <div class="container">
    <span class="eyebrow">Start a conversation</span>
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="contact.html#enquiry">Request a Proposal {ICONS['arrow']}</a>
      <a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">{ICONS['wa']} WhatsApp us</a>
    </div>
  </div>
</section>
"""

SERVICES = [
  ("administration", "Labour Camp Administration", "Day-to-day operations, occupancy control, reporting and resident coordination.", "img/camp-office.jpg",
   ["Occupancy planning and room allocation", "Resident onboarding, ID records and movement logs", "Daily operations reporting to the client", "Complaint logging, follow-up and transparent closure"]),
  ("accommodation", "Accommodation Management", "Room allocation, inspections, housekeeping standards and asset care.", "img/room-1.jpg",
   ["Routine room and block inspections", "Furniture, fittings and asset condition tracking", "Housekeeping standard audits", "Handover and hand-back condition reports"]),
  ("catering", "Catering & Mess Hall Support", "Dining coordination, hygiene control and meal service oversight.", "img/kitchen-counter.jpg",
   ["Mess hall scheduling and capacity planning", "Kitchen hygiene and food-safety monitoring", "Caterer coordination and quality checks", "Nutrition-focused menu review with the client"]),
  ("housekeeping", "Housekeeping & Laundry", "Room cleaning, common-area care, laundry and consumable control.", "img/laundry.jpg",
   ["Daily room, toilet and corridor cleaning checklists", "Laundry operations and linen management", "Consumables stock control", "Pest-control coordination"]),
  ("maintenance", "Maintenance & MEP Support", "MEP support, preventive maintenance, repairs and utilities monitoring.", "img/mep.jpg",
   ["Preventive maintenance schedules", "HVAC, electrical and plumbing response", "Utilities monitoring and consumption control", "Breakdown logging with priority allocation"]),
  ("hse", "HSE & Compliance Support", "Camp rules, welfare standards, inspections and emergency readiness.", "img/img-1.jpg",
   ["Site safety protocols and inductions", "Fire, life-safety, hygiene and welfare inspections", "Emergency drills and readiness planning", "Authority coordination and compliance records"]),
  ("security", "Security & Access Coordination", "Gate control, visitor management and security coordination.", "img/security.jpg",
   ["Gate and access control procedures", "Visitor and contractor management", "Patrol scheduling and incident reporting", "CCTV and access-system coordination"]),
  ("waste", "Waste Management & Hygiene", "Waste collection, sanitation, pest-control support and environmental cleanliness.", "img/waste-management.jpg",
   ["Segregated waste collection and disposal", "Sanitation and environmental cleanliness", "Recycling and resource-control initiatives", "Environmental compliance records"]),
]

INDUSTRIES = [
  ("Construction", "Project delivery and major construction sites", "img/construction-site-camp.jpg"),
  ("Oil & Gas", "Remote and industrial workforce communities", "img/oil-gas-camp.jpg"),
  ("Infrastructure", "Large, multi-stakeholder delivery programmes", "img/infrastructure.jpg"),
  ("Industrial Projects", "Manufacturing and process facilities", "img/industrial.jpg"),
  ("Logistics", "Transport depots and operational hubs", "img/logistics.jpg"),
  ("Remote Workforce Sites", "Distributed workforce and site camps", "img/remote-site.jpg"),
]

def industries_grid():
    return '<div class="industries">' + "".join(
        f'<a class="ind reveal d{i%3+1}" href="industries.html#{n.lower().replace(" ","-").replace("&","and")}"><img src="{img}" alt="{n} workforce accommodation" loading="lazy"><div class="cap"><h3>{n}</h3><p>{d}</p></div></a>'
        for i, (n, d, img) in enumerate(INDUSTRIES)) + '</div>'

# ============================================================ HOME
def home():
    ld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Organization","name":"Nexcamp Management and Operation of Employee Housing LLC","alternateName":"Nexcamp","url":"%s","logo":"%s/img/brand/logo-full.png","email":"%s","telephone":"%s","address":{"@type":"PostalAddress","streetAddress":"Office No. 8, Habshan 2","postOfficeBoxNumber":"232505","addressLocality":"Abu Dhabi","addressCountry":"AE"},"areaServed":"United Arab Emirates","description":"Professional employee-housing management and integrated support services for workforce accommodation communities in the UAE."}
</script>""" % (SITE_URL, SITE_URL, EMAIL, PHONE_TEL)
    services = "".join(f"""
      <a class="card reveal d{i%4+1}" href="services.html#{sid}">
        <div class="thumb"><img src="{img}" alt="{name}" loading="lazy"></div>
        <div class="body"><span class="num">{i+1}</span><h3>{name}</h3><p>{desc}</p><span class="more">Learn more {ICONS['arrow']}</span></div>
      </a>""" for i, (sid, name, desc, img, _) in enumerate(SERVICES))
    html = head("Nexcamp | Employee Housing Management & Camp Operations, Abu Dhabi UAE",
                "Nexcamp delivers professional management and operation of employee housing communities across the UAE: camp administration, accommodation, catering, housekeeping, maintenance, HSE, security and waste management.",
                "index.html", extra_ld=ld)
    html += header(False)
    html += f"""
<section class="hero">
  <div class="media"><img src="img/camp-1.jpg" alt="Nexcamp-managed employee housing community at dusk" fetchpriority="high"></div>
  <div class="container content">
    <div class="kicker">Employee Housing Management · Abu Dhabi, UAE</div>
    <h1>Creating comfortable communities. <em>Enriching everyday lives.</em></h1>
    <p>Nexcamp is a single accountable operating partner for workforce accommodation. We make housing assets easier to operate, safer to occupy and more reliable for the clients who depend on their people every day.</p>
    <div class="btn-row">
      <a class="btn btn-gold" href="contact.html#enquiry">Request a Proposal {ICONS['arrow']}</a>
      <a class="btn btn-outline" href="services.html">Explore our services</a>
    </div>
    <div class="hero-pillars">
      <div>Quality Accommodation<small>Well-maintained living spaces</small></div>
      <div>Efficient Operations<small>Structured daily management</small></div>
      <div>Welfare &amp; Wellbeing<small>People-focused support</small></div>
      <div>Safety &amp; Compliance<small>Controlled operating standards</small></div>
    </div>
  </div>
  <div class="scroll-hint" aria-hidden="true"></div>
</section>

<div class="strip" aria-hidden="true"><div class="track">
  <span>Labour Camp Administration</span><span>Accommodation Management</span><span>Catering &amp; Mess Hall</span><span>Housekeeping &amp; Laundry</span><span>Maintenance &amp; MEP</span><span>HSE &amp; Compliance</span><span>Security &amp; Access</span><span>Waste Management</span>
  <span>Labour Camp Administration</span><span>Accommodation Management</span><span>Catering &amp; Mess Hall</span><span>Housekeeping &amp; Laundry</span><span>Maintenance &amp; MEP</span><span>HSE &amp; Compliance</span><span>Security &amp; Access</span><span>Waste Management</span>
</div></div>

<section class="section">
  <div class="container split">
    <div class="photo-stack reveal">
      <div class="main"><img src="img/entrance.jpg" alt="Nexcamp camp entrance and gatehouse"></div>
      <div class="small"><img src="img/staff-pic.jpg" alt="Nexcamp site team"></div>
      <div class="badge"><strong>24/7</strong><span>Site support mindset</span></div>
    </div>
    <div class="text reveal d2">
      <span class="eyebrow">About Nexcamp</span>
      <h2>One team. One standard. One accountable point of coordination.</h2>
      <p class="lead">Nexcamp Management and Operation of Employee Housing LLC supports owners, developers and contractors with end-to-end management of workforce accommodation communities. We focus on safe, clean, efficient and people-centred living environments that protect asset value and enhance resident wellbeing.</p>
      <ul class="checklist">
        <li><span><strong>Owner-side operating partner</strong> with a resident-first mindset</span></li>
        <li><span><strong>360° camp operations</strong> under a single coordination structure</span></li>
        <li><span><strong>Transparent reporting</strong> through KPIs, issue logs and monthly management packs</span></li>
      </ul>
      <div class="btn-row" style="margin-top:28px"><a class="btn btn-green" href="about.html">More about us {ICONS['arrow']}</a></div>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Service Portfolio</span>
      <h2>Operational services delivered with care, compliance and efficiency</h2>
      <p class="lead">A complete operating model designed to reduce coordination burden and improve site standards.</p>
    </div>
    <div class="grid grid-4">{services}</div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Resident Experience</span>
      <h2>Better living environments support stronger workforce performance</h2>
      <p class="lead">Happy residents. Productive workforce. Stronger organisations.</p>
    </div>
    <div class="mosaic reveal">
      <figure class="wide"><img src="img/dining-room-1.jpg" alt="Dining hall" loading="lazy"><figcaption>Dining &amp; Kitchens</figcaption></figure>
      <figure><img src="img/gym-2.jpg" alt="Fitness facility" loading="lazy"><figcaption>Fitness &amp; Recreation</figcaption></figure>
      <figure class="tall"><img src="img/gym.jpg" alt="Gym supervised by Nexcamp staff" loading="lazy"><figcaption>Wellbeing Programmes</figcaption></figure>
      <figure><img src="img/room-2.jpg" alt="Resident room" loading="lazy"><figcaption>Clean, Comfortable Rooms</figcaption></figure>
      <figure><img src="img/play-area.jpg" alt="Outdoor sports court" loading="lazy"><figcaption>Outdoor Wellbeing</figcaption></figure>
      <figure class="wide"><img src="img/community-space-1.jpg" alt="Shaded community seating" loading="lazy"><figcaption>Community Spaces</figcaption></figure>
      <figure><img src="img/recreation.jpg" alt="Recreation lounge" loading="lazy"><figcaption>Recreation Lounges</figcaption></figure>
    </div>
  </div>
</section>

<section class="section bg-green">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Management Approach</span>
      <h2>A practical operating system for reliable daily performance</h2>
      <p class="lead">A disciplined management cycle creates confidence from day one and drives measurable improvement over time.</p>
    </div>
    <div class="process">
      <div class="step reveal d1"><div class="dot">1</div><h3>Mobilise</h3><p>Site survey, handover plan, team deployment and baseline condition review.</p><div class="thumb"><img src="img/entrance.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d2"><div class="dot">2</div><h3>Stabilise</h3><p>Daily routines, resident coordination, housekeeping standards and maintenance priorities.</p><div class="thumb"><img src="img/img-1.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d3"><div class="dot">3</div><h3>Control</h3><p>Reporting cadence, KPI tracking, cost visibility and authority coordination.</p><div class="thumb"><img src="img/mep.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d4"><div class="dot">4</div><h3>Improve</h3><p>Corrective actions, service upgrades and resident-experience enhancement.</p><div class="thumb"><img src="img/waste-management.jpg" alt="" loading="lazy"></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head center reveal">
      <span class="eyebrow">Industries We Support</span>
      <h2>Employee housing solutions for workforce-intensive sectors</h2>
    </div>
    {industries_grid()}
  </div>
</section>

<section class="section bg-cream">
  <div class="container split reverse">
    <div class="photo-stack reveal">
      <div class="main"><img src="img/management.jpg" alt="Nexcamp management team reviewing site plans"></div>
      <div class="small"><img src="img/kpi-track.jpg" alt="KPI dashboard review"></div>
    </div>
    <div class="text reveal d2">
      <span class="eyebrow">Why Partner With Nexcamp</span>
      <h2>An owner-side operating partner with a resident-first mindset</h2>
      <ul class="checklist">
        <li><span><strong>Experienced management team.</strong> Practical site operating knowledge and disciplined execution.</span></li>
        <li><span><strong>Comprehensive end-to-end offering.</strong> A single coordination structure for daily accommodation operations.</span></li>
        <li><span><strong>Transparent reporting.</strong> Performance visibility through KPIs, issue logs and management reporting.</span></li>
        <li><span><strong>Scalable solutions.</strong> Operating model tailored to project size, location and client priorities.</span></li>
        <li><span><strong>Reliable partner.</strong> A long-term mindset focused on asset value and resident wellbeing.</span></li>
      </ul>
      <blockquote class="quote" style="margin:28px 0 0">“We do not just manage accommodation; we build communities where people can live with comfort, dignity and confidence.”</blockquote>
    </div>
  </div>
</section>

{cta_band()}
"""
    html += footer()
    return html

# ============================================================ ABOUT
def about():
    html = head("About Nexcamp | Vision, Mission, Values & Management Approach",
                "Learn about Nexcamp, an Abu Dhabi-based operator of employee housing communities: our vision, mission, core values, 45-day mobilisation plan and KPI-driven reporting.",
                "about.html", image="img/camp-2.jpg")
    html += header(True)
    html += page_hero("About", "People-focused operations for safe, reliable and comfortable employee housing", "Nexcamp delivers professional management and operation of employee housing communities across the United Arab Emirates.", "img/camp-2.jpg")
    html += f"""
<section class="section">
  <div class="container split">
    <div class="text reveal">
      <span class="eyebrow">Who We Are</span>
      <h2>Making accommodation assets easier to operate, safer to occupy and more reliable</h2>
      <p class="lead">Our role is to make accommodation assets easier to operate, safer to occupy and more reliable for clients who depend on their workforce every day. We act as an owner-side operating partner, bringing one team, one standard and one accountable point of coordination to every site we manage.</p>
      <div class="stats" style="grid-template-columns:repeat(2,1fr);margin-top:30px">
        <div class="stat"><strong>01</strong><span>Accountable operator</span></div>
        <div class="stat"><strong>360°</strong><span>Camp operations</span></div>
        <div class="stat"><strong>24/7</strong><span>Site support mindset</span></div>
        <div class="stat"><strong>UAE</strong><span>Abu Dhabi base</span></div>
      </div>
    </div>
    <div class="photo-stack reveal d2">
      <div class="main"><img src="img/community-pic.jpg" alt="Shaded community area in a Nexcamp-managed camp"></div>
      <div class="small"><img src="img/camp-3.jpg" alt="Modern accommodation block"></div>
    </div>
  </div>
</section>

<section class="section bg-cream tight">
  <div class="container grid grid-2">
    <div class="feature-card reveal"><div class="icon">{ICONS['layers']}</div><span class="eyebrow">Vision</span><h3>A trusted leader in workforce accommodation</h3><p>To be a trusted leader in workforce accommodation and camp management by delivering reliable, compliant and people-focused support services.</p></div>
    <div class="feature-card reveal d2"><div class="icon">{ICONS['heart']}</div><span class="eyebrow">Mission</span><h3>High standards of safety, hygiene, welfare and efficiency</h3><p>To operate employee housing to high standards of safety, hygiene, welfare and efficiency through experienced management, responsive maintenance and quality support.</p></div>
  </div>
</section>

<section class="section bg-green">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Core Values</span>
      <h2>The standards that guide our people, decisions and daily site operations</h2>
      <div class="values">
        <div class="value"><div class="letter">S</div><h3>Safety</h3><p>We protect the safety and wellbeing of residents, clients and site teams.</p></div>
        <div class="value"><div class="letter">R</div><h3>Respect</h3><p>We treat every person with dignity, fairness and consideration.</p></div>
        <div class="value"><div class="letter">R</div><h3>Reliability</h3><p>We keep our promises through consistent standards and dependable service.</p></div>
        <div class="value"><div class="letter">A</div><h3>Accountability</h3><p>We take ownership of our responsibilities, reporting and outcomes.</p></div>
        <div class="value"><div class="letter">E</div><h3>Excellence</h3><p>We work to improve the resident experience and operating performance.</p></div>
      </div>
    </div>
    <div class="reveal d2"><div class="photo-stack"><div class="main" style="aspect-ratio:3/4"><img src="img/staff-pic.jpg" alt="Nexcamp team walking through a managed community"></div></div></div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Management Approach</span>
      <h2>Mobilise → Stabilise → Control → Improve</h2>
      <p class="lead">A disciplined management cycle creates confidence from day one and drives measurable improvement over time.</p>
    </div>
    <div class="process">
      <div class="step reveal d1"><div class="dot">1</div><h3>Mobilise</h3><p>Site survey, handover plan, team deployment and baseline condition review.</p><div class="thumb"><img src="img/entrance.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d2"><div class="dot">2</div><h3>Stabilise</h3><p>Daily routines, resident coordination, housekeeping standards and maintenance priorities.</p><div class="thumb"><img src="img/img-1.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d3"><div class="dot">3</div><h3>Control</h3><p>Reporting cadence, KPI tracking, cost visibility and authority coordination.</p><div class="thumb"><img src="img/mep.jpg" alt="" loading="lazy"></div></div>
      <div class="step reveal d4"><div class="dot">4</div><h3>Improve</h3><p>Corrective actions, service upgrades and resident-experience enhancement.</p><div class="thumb"><img src="img/waste-management.jpg" alt="" loading="lazy"></div></div>
    </div>
  </div>
</section>

<section class="section bg-cream" id="mobilisation">
  <div class="container split">
    <div class="text reveal">
      <span class="eyebrow">Mobilisation Plan</span>
      <h2>A clear 45-day transition from award to steady-state operation</h2>
      <p class="lead">A disciplined start-up process creates confidence from day one.</p>
      <div class="timeline">
        <div class="tl-item"><span class="tag">Days 1–7</span><p>Kick-off, site survey, document review, handover checklist and mobilisation governance.</p></div>
        <div class="tl-item"><span class="tag">Days 8–20</span><p>Team onboarding, accommodation zoning, service mapping and client reporting templates.</p></div>
        <div class="tl-item"><span class="tag">Days 21–35</span><p>Operating routines begin: housekeeping, maintenance logs, security coordination and resident communication.</p></div>
        <div class="tl-item"><span class="tag">Days 36–45</span><p>Performance baseline, corrective-action plan, KPI dashboard and steady-state operation.</p></div>
      </div>
    </div>
    <div class="reveal d2"><div class="photo-stack"><div class="main" style="aspect-ratio:4/5"><img src="img/camp-3.jpg" alt="Newly mobilised accommodation block"></div></div></div>
  </div>
</section>

<section class="section" id="reporting">
  <div class="container split reverse">
    <div class="reveal d2"><div class="photo-stack"><div class="main"><img src="img/kpi-track.jpg" alt="Nexcamp team reviewing an operations KPI dashboard"></div></div></div>
    <div class="text reveal">
      <span class="eyebrow">Reporting &amp; KPI Tracking</span>
      <h2>Transparent operating visibility for owners and client teams</h2>
      <div class="kpis">
        <div class="kpi"><div class="n">1</div><div><h4>Cleaning Completion</h4><p>Daily room and toilet cleaning checklists with site audits.</p></div></div>
        <div class="kpi"><div class="n">2</div><div><h4>Complaints</h4><p>Acknowledgement, closure tracking and escalation visibility.</p></div></div>
        <div class="kpi"><div class="n">3</div><div><h4>Maintenance Response</h4><p>Breakdown logging, priority allocation and closure status.</p></div></div>
        <div class="kpi"><div class="n">4</div><div><h4>HSE Inspections</h4><p>Fire, life-safety, hygiene and welfare checks.</p></div></div>
        <div class="kpi"><div class="n">5</div><div><h4>Security Coverage</h4><p>Gate, patrol and incident-report coordination.</p></div></div>
        <div class="kpi"><div class="n">6</div><div><h4>Authority Reporting</h4><p>Monthly records and compliance follow-up.</p></div></div>
      </div>
    </div>
  </div>
  <div class="container" style="margin-top:40px">
    <div class="pack reveal">
      <h3>Monthly Management Pack</h3>
      <ul>
        <li>Occupancy status and movement</li><li>Maintenance register and closures</li><li>HSE observations and actions</li>
        <li>Service-level performance summary</li><li>Resident feedback and complaints</li><li>Client decisions and follow-ups</li>
      </ul>
    </div>
  </div>
</section>

<section class="section bg-cream" id="team">
  <div class="container">
    <div class="section-head reveal">
      <span class="eyebrow">Our Team</span>
      <h2>A uniformed, identifiable team on site every day</h2>
      <p class="lead">Every Nexcamp role is clearly identifiable through role-specific uniforms in our green and stone palette, so residents and clients always know who to approach.</p>
    </div>
    <div class="roles">
      <div class="role reveal d1"><div class="sw" style="background:#f3ecd9"></div><div><strong>Management</strong><span>Site &amp; account leadership</span></div></div>
      <div class="role reveal d2"><div class="sw" style="background:#1f4a3a"></div><div><strong>Administration</strong><span>Records, onboarding &amp; reporting</span></div></div>
      <div class="role reveal d3"><div class="sw" style="background:#2b6a52"></div><div><strong>Supervisors</strong><span>Daily operations &amp; coordination</span></div></div>
      <div class="role reveal d4"><div class="sw" style="background:#a8bfa0"></div><div><strong>Housekeeping</strong><span>Rooms, common areas &amp; laundry</span></div></div>
      <div class="role reveal d1"><div class="sw" style="background:#cfc3a6"></div><div><strong>Maintenance</strong><span>MEP, repairs &amp; utilities</span></div></div>
      <div class="role reveal d2"><div class="sw" style="background:#d9e021"></div><div><strong>HSE</strong><span>Safety, inspections &amp; readiness</span></div></div>
      <div class="role reveal d3"><div class="sw" style="background:#b8ad8f"></div><div><strong>Camp Patrol</strong><span>Access, patrols &amp; incident response</span></div></div>
      <div class="role reveal d4"><div class="sw" style="background:#ffffff"></div><div><strong>Catering</strong><span>Kitchen &amp; mess-hall service</span></div></div>
    </div>
    <div class="grid grid-3" style="margin-top:28px">
      <div class="card reveal d1"><div class="thumb"><img src="img/management.jpg" alt="Management team" loading="lazy"></div></div>
      <div class="card reveal d2"><div class="thumb"><img src="img/kitchen-counter.jpg" alt="Catering team" loading="lazy"></div></div>
      <div class="card reveal d3"><div class="thumb"><img src="img/hvac-work.jpg" alt="Maintenance technician" loading="lazy"></div></div>
    </div>
  </div>
</section>

{cta_band("img/camp-4.jpg")}
"""
    html += footer()
    return html

# ============================================================ SERVICES
def services():
    html = head("Services | Camp Administration, Catering, Housekeeping, Maintenance, HSE & Security | Nexcamp",
                "Nexcamp's service portfolio for employee housing: labour camp administration, accommodation management, catering and mess hall, housekeeping and laundry, maintenance and MEP, HSE compliance, security and waste management.",
                "services.html", image="img/dining-room-1.jpg")
    html += header(True)
    html += page_hero("Services", "A complete operating model for employee housing", "Eight integrated service lines under one accountable coordination structure, designed to reduce coordination burden and improve site standards.", "img/dining-room-1.jpg")
    blocks = ""
    for i, (sid, name, desc, img, points) in enumerate(SERVICES):
        rev = " reverse" if i % 2 else ""
        pts = "".join(f"<li><span>{p}</span></li>" for p in points)
        cls = "bg-cream" if i % 2 else ""
        blocks += f"""
<section class="section {cls}" id="{sid}" style="padding-block:clamp(48px,6vw,80px)">
  <div class="container split{rev}">
    <div class="reveal"><div class="photo-stack"><div class="main"><img src="{img}" alt="{name}" loading="lazy"></div></div></div>
    <div class="text reveal d2">
      <span class="eyebrow">Service {i+1:02d}</span>
      <h2>{name}</h2>
      <p class="lead">{desc}</p>
      <ul class="checklist">{pts}</ul>
    </div>
  </div>
</section>"""
    html += f"""
<section class="section tight">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Operating Scope</span><h2>End-to-end operating coverage for employee housing communities</h2></div>
    <div class="grid grid-3">
      <div class="feature-card reveal d1"><div class="icon">{ICONS['home']}</div><h3>Accommodation blocks</h3><p>Room allocation, inspections, asset care and condition reporting across every block.</p></div>
      <div class="feature-card reveal d2"><div class="icon">{ICONS['users']}</div><h3>Common areas &amp; recreation</h3><p>Dining halls, kitchens, gyms, courts, lounges and shaded community spaces.</p></div>
      <div class="feature-card reveal d3"><div class="icon">{ICONS['gear']}</div><h3>Utilities &amp; MEP support</h3><p>HVAC, electrical, plumbing, preventive maintenance and consumption control.</p></div>
      <div class="feature-card reveal d1"><div class="icon">{ICONS['shield']}</div><h3>Security &amp; access control</h3><p>Gate control, visitor management, patrols and incident coordination.</p></div>
      <div class="feature-card reveal d2"><div class="icon">{ICONS['leaf']}</div><h3>Waste management &amp; hygiene</h3><p>Sanitation, pest control, segregated waste and environmental cleanliness.</p></div>
      <div class="feature-card reveal d3"><div class="icon">{ICONS['chart']}</div><h3>Authority &amp; tenant coordination</h3><p>Compliance records, authority liaison and transparent client reporting.</p></div>
    </div>
  </div>
</section>
{blocks}
<section class="section bg-green" id="safety">
  <div class="container split">
    <div class="reveal">
      <span class="eyebrow">Safety, Compliance &amp; Sustainability</span>
      <h2>Safety in every action. Sustainability in every decision.</h2>
      <p class="lead">Responsible operations with attention to safety, hygiene and resource control.</p>
      <div class="values">
        <div class="value"><div class="letter">01</div><h3>Safety First</h3><p>Site safety protocols, induction, periodic inspections and emergency readiness.</p></div>
        <div class="value"><div class="letter">02</div><h3>Compliance Assured</h3><p>Support for local requirements, authority coordination and welfare standards.</p></div>
        <div class="value"><div class="letter">03</div><h3>Sustainable Operations</h3><p>Waste control, responsible resource use and environmental cleanliness.</p></div>
        <div class="value"><div class="letter">04</div><h3>Continuous Improvement</h3><p>Performance review, corrective action tracking and service enhancement.</p></div>
      </div>
    </div>
    <div class="reveal d2 grid grid-2" style="gap:14px">
      <div class="card"><div class="thumb" style="aspect-ratio:3/4"><img src="img/hvac-work.jpg" alt="HVAC technician" loading="lazy"></div></div>
      <div class="card"><div class="thumb" style="aspect-ratio:3/4"><img src="img/mep-works.jpg" alt="Plumbing repair" loading="lazy"></div></div>
      <div class="card"><div class="thumb" style="aspect-ratio:3/4"><img src="img/gardener.jpg" alt="Landscaping" loading="lazy"></div></div>
      <div class="card"><div class="thumb" style="aspect-ratio:3/4"><img src="img/remote-work-site-1.jpg" alt="Remote site camp" loading="lazy"></div></div>
    </div>
  </div>
</section>
{cta_band("img/public-area.jpg", "Need a single operator for your camp?", "Tell us about your site, headcount and service scope. We will respond with a tailored operating proposal.")}
"""
    html += footer()
    return html

# ============================================================ INDUSTRIES
def industries():
    html = head("Industries | Construction, Oil & Gas, Infrastructure, Industrial, Logistics & Remote Sites | Nexcamp",
                "Nexcamp supports workforce-intensive sectors across the UAE with employee housing management for construction, oil and gas, infrastructure, industrial projects, logistics and remote workforce sites.",
                "industries.html", image="img/oil-gas-camp.jpg")
    html += header(True)
    html += page_hero("Industries", "Employee housing solutions for workforce-intensive sectors", "Flexible enough for one asset. Structured enough for a portfolio.", "img/oil-gas-camp.jpg")
    details = ""
    copy = {
      "Construction": "Project-delivery camps need fast mobilisation, tight occupancy control and coordination with multiple subcontractors. Nexcamp brings order to high-turnover environments and keeps welfare standards consistent through every project phase.",
      "Oil & Gas": "Remote and industrial workforce communities demand rigorous HSE discipline, reliable catering and utilities resilience. Our teams operate to the standards expected of energy-sector clients and their auditors.",
      "Infrastructure": "Large, multi-stakeholder programmes require clear reporting lines and scalable service delivery. We provide one accountable coordination point across accommodation, catering, maintenance and security.",
      "Industrial Projects": "Manufacturing and process facilities rely on a stable, well-rested workforce. We manage housing adjacent to industrial sites with an emphasis on hygiene, shift-pattern catering and quiet, well-maintained rooms.",
      "Logistics": "Transport depots and operational hubs run around the clock. Nexcamp aligns housekeeping, mess-hall timing and access control with 24-hour operations.",
      "Remote Workforce Sites": "Distributed camps in remote locations need self-sufficient operations, preventive maintenance and dependable supply coordination. We plan for distance so residents never feel it.",
    }
    for i, (n, d, img) in enumerate(INDUSTRIES):
        anchor = n.lower().replace(" ", "-").replace("&", "and")
        rev = " reverse" if i % 2 else ""
        cls = "bg-cream" if i % 2 else ""
        details += f"""
<section class="section {cls}" id="{anchor}" style="padding-block:clamp(48px,6vw,80px)">
  <div class="container split{rev}">
    <div class="reveal"><div class="photo-stack"><div class="main"><img src="{img}" alt="{n}" loading="lazy"></div></div></div>
    <div class="text reveal d2"><span class="eyebrow">{d}</span><h2>{n}</h2><p class="lead">{copy[n]}</p><a class="btn btn-outline-green" href="contact.html#enquiry">Discuss your site {ICONS['arrow']}</a></div>
  </div>
</section>"""
    html += f"""
<section class="section tight"><div class="container">{industries_grid()}</div></section>
{details}
<section class="section bg-green" id="partnership">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Partnership Model</span><h2>A flexible management framework tailored to each asset and client requirement</h2></div>
    <div class="grid grid-3" style="gap:18px">
      <div class="feature-card reveal d1" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)"><span class="num" style="display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#fff;font-family:var(--serif);margin-bottom:12px">1</span><h3>Assess</h3><p>Site survey, occupancy review and service-gap assessment.</p></div>
      <div class="feature-card reveal d2" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)"><span class="num" style="display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#fff;font-family:var(--serif);margin-bottom:12px">2</span><h3>Design</h3><p>Operating structure, manpower plan, reporting pack and service schedule.</p></div>
      <div class="feature-card reveal d3" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)"><span class="num" style="display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#fff;font-family:var(--serif);margin-bottom:12px">3</span><h3>Mobilise</h3><p>Team deployment, handover, resident communication and vendor coordination.</p></div>
      <div class="feature-card reveal d1" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)"><span class="num" style="display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#fff;font-family:var(--serif);margin-bottom:12px">4</span><h3>Operate</h3><p>Daily operations, HSE, housekeeping, maintenance, resident support and KPI tracking.</p></div>
      <div class="feature-card reveal d2" style="background:rgba(255,255,255,.05);border-color:rgba(255,255,255,.12)"><span class="num" style="display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:var(--gold);color:#fff;font-family:var(--serif);margin-bottom:12px">5</span><h3>Improve</h3><p>Monthly review, corrective actions, budget control and service improvement.</p></div>
      <div class="feature-card reveal d3" style="background:var(--gold);border-color:var(--gold)"><h3 style="color:#fff">Flexible enough for one asset. Structured enough for a portfolio.</h3><p style="color:#fff8e6">Every engagement is scoped to project size, location and client priorities.</p></div>
    </div>
  </div>
</section>
{cta_band("img/remote-work-site-1.jpg")}
"""
    html += footer()
    return html

# ============================================================ CAREERS
def careers():
    html = head("Careers at Nexcamp | Join Our Camp Operations Team in the UAE",
                "Build your career with Nexcamp. We hire camp managers, administrators, supervisors, housekeeping, maintenance, HSE, security and catering professionals for employee housing operations across the UAE.",
                "careers.html", image="img/staff-pic.jpg")
    html += header(True)
    html += page_hero("Careers", "Build communities. Build your career.", "Nexcamp is growing its site teams across the UAE. If you take pride in safe, clean and well-run places to live, we would like to hear from you.", "img/staff-pic.jpg")
    html += f"""
<section class="section">
  <div class="container split">
    <div class="text reveal">
      <span class="eyebrow">Why Nexcamp</span>
      <h2>A workplace built on safety, respect, reliability, accountability and excellence</h2>
      <p class="lead">Our people are the service. We invest in training, clear procedures and role-specific uniforms and equipment so every team member can do their job well and be recognised for it.</p>
      <ul class="checklist">
        <li><span><strong>Structured induction and HSE training</strong> for every role</span></li>
        <li><span><strong>Clear career paths</strong> from site roles to supervisory and management positions</span></li>
        <li><span><strong>Respectful, multicultural teams</strong> operating to consistent standards</span></li>
        <li><span><strong>Professional uniforms and PPE</strong> provided</span></li>
      </ul>
    </div>
    <div class="photo-stack reveal d2">
      <div class="main"><img src="img/management.jpg" alt="Nexcamp supervisors and manager on site"></div>
      <div class="small"><img src="img/gardener.jpg" alt="Landscaping team member"></div>
    </div>
  </div>
</section>

<section class="section bg-cream">
  <div class="container">
    <div class="section-head reveal"><span class="eyebrow">Roles We Hire</span><h2>Opportunities across every part of camp operations</h2><p class="lead">We regularly recruit for the roles below. Submit a general application and we will contact you when a suitable position opens.</p></div>
    <div class="grid grid-4">
      <div class="feature-card reveal d1"><h3>Management</h3><p>Camp managers and account leads responsible for site performance and client reporting.</p></div>
      <div class="feature-card reveal d2"><h3>Administration</h3><p>Occupancy records, resident onboarding, documentation and authority coordination.</p></div>
      <div class="feature-card reveal d3"><h3>Supervisors</h3><p>Shift and service supervisors coordinating daily routines and quality checks.</p></div>
      <div class="feature-card reveal d4"><h3>Housekeeping</h3><p>Room attendants, common-area cleaners and laundry operators.</p></div>
      <div class="feature-card reveal d1"><h3>Maintenance</h3><p>HVAC, electrical and plumbing technicians and multi-skilled maintenance staff.</p></div>
      <div class="feature-card reveal d2"><h3>HSE</h3><p>Safety officers conducting inspections, inductions and emergency readiness.</p></div>
      <div class="feature-card reveal d3"><h3>Camp Patrol &amp; Security</h3><p>Gate control, patrols, visitor management and incident reporting.</p></div>
      <div class="feature-card reveal d4"><h3>Catering</h3><p>Chefs, cooks, kitchen stewards and mess-hall service staff.</p></div>
    </div>
  </div>
</section>

<section class="section" id="apply">
  <div class="container contact-grid">
    <div class="form-card reveal">
      <span class="eyebrow">Apply Now</span>
      <h2 style="font-size:1.9rem">Submit your application</h2>
      <p class="lead" style="font-size:1rem">Complete the form and attach your CV. Our HR team reviews every application.</p>
      <form class="form" name="careers" method="POST" action="/" data-form data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data" data-subject="Job application via nexcamps.com" data-success="Thank you. Your application has been received. We will contact you if a suitable position becomes available.">
        <input type="hidden" name="form-name" value="careers">
        <p class="honey"><label>Do not fill this in: <input name="bot-field"></label></p>
        <div class="row">
          <label>Full name<input type="text" name="full_name" required autocomplete="name"></label>
          <label>Nationality<input type="text" name="nationality" required></label>
        </div>
        <div class="row">
          <label>Email<input type="email" name="email" required autocomplete="email"></label>
          <label>Mobile / WhatsApp<input type="tel" name="mobile" required autocomplete="tel"></label>
        </div>
        <div class="row">
          <label>Position applied for
            <select name="position" required>
              <option value="">Select a role</option>
              <option>Management</option><option>Administration</option><option>Supervisor</option><option>Housekeeping</option>
              <option>Maintenance / MEP</option><option>HSE</option><option>Camp Patrol / Security</option><option>Catering</option><option>Other</option>
            </select></label>
          <label>Current location<input type="text" name="location" placeholder="e.g. Abu Dhabi, UAE"></label>
        </div>
        <div class="row">
          <label>Years of experience<input type="number" name="experience_years" min="0" max="50"></label>
          <label>Visa status<select name="visa_status"><option value="">Select</option><option>Inside UAE – transferable visa</option><option>Inside UAE – visit visa</option><option>Outside UAE</option></select></label>
        </div>
        <label>Attach CV (PDF or Word, max 5 MB)<input type="file" name="cv" accept=".pdf,.doc,.docx"><span class="hint">If the file upload is not available, please email your CV to {EMAIL}.</span></label>
        <label>Message (optional)<textarea name="message" placeholder="Tell us briefly about your experience."></textarea></label>
        <div class="form-msg" role="status"></div>
        <button class="btn btn-gold" type="submit">Submit application {ICONS['upload']}</button>
      </form>
    </div>
    <div class="reveal d2">
      <div class="contact-list">
        <a class="contact-item" href="mailto:{EMAIL}?subject=Job%20application"><div class="ic">{ICONS['mail']}</div><div><strong>Email your CV</strong><span>{EMAIL}</span><small>Subject: Job application – [Role]</small></div></a>
        <a class="contact-item" href="{WA}" target="_blank" rel="noopener"><div class="ic">{ICONS['wa']}</div><div><strong>WhatsApp</strong><span>{PHONE_DISPLAY}</span><small>Share your CV and the role you are interested in</small></div></a>
        <div class="contact-item"><div class="ic">{ICONS['shield']}</div><div><strong>Recruitment notice</strong><span>Nexcamp never charges candidates any fee</span><small>Please report any request for payment made in our name.</small></div></div>
      </div>
      <div class="grid grid-2" style="gap:14px;margin-top:22px">
        <div class="card"><div class="thumb"><img src="img/kitchen-counter.jpg" alt="Catering team" loading="lazy"></div></div>
        <div class="card"><div class="thumb"><img src="img/laundry-1.jpg" alt="Housekeeping" loading="lazy"></div></div>
        <div class="card"><div class="thumb"><img src="img/mep-works.jpg" alt="Maintenance" loading="lazy"></div></div>
        <div class="card"><div class="thumb"><img src="img/security.jpg" alt="Camp patrol" loading="lazy"></div></div>
      </div>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

# ============================================================ CONTACT
def contact():
    ld = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LocalBusiness","name":"Nexcamp Management and Operation of Employee Housing LLC","url":"%s/contact.html","telephone":"%s","email":"%s","address":{"@type":"PostalAddress","streetAddress":"Office No. 8, Habshan 2","postOfficeBoxNumber":"232505","addressLocality":"Abu Dhabi","addressCountry":"AE"},"openingHours":"Mo-Fr 08:00-18:00"}
</script>""" % (SITE_URL, PHONE_TEL, EMAIL)
    html = head("Contact Nexcamp | Request a Proposal for Employee Housing Management",
                "Contact Nexcamp in Abu Dhabi for employee housing and camp management. Call +971 52 820 0088, WhatsApp, email info@nexcamps.com or request a proposal online.",
                "contact.html", image="img/entrance.jpg", extra_ld=ld)
    html += header(True)
    html += page_hero("Contact", "Let’s talk about your workforce accommodation", "Tell us about your site, headcount and service scope. We respond to every enquiry.", "img/entrance.jpg")
    html += f"""
<section class="section" id="enquiry">
  <div class="container contact-grid">
    <div class="form-card reveal">
      <span class="eyebrow">Request a Proposal</span>
      <h2 style="font-size:1.9rem">Send us your requirements</h2>
      <form class="form" name="enquiry" method="POST" action="/" data-form data-netlify="true" netlify-honeypot="bot-field" data-subject="Proposal request via nexcamps.com">
        <input type="hidden" name="form-name" value="enquiry">
        <p class="honey"><label>Do not fill this in: <input name="bot-field"></label></p>
        <div class="row">
          <label>Full name<input type="text" name="full_name" required autocomplete="name"></label>
          <label>Company<input type="text" name="company" autocomplete="organization"></label>
        </div>
        <div class="row">
          <label>Email<input type="email" name="email" required autocomplete="email"></label>
          <label>Phone / WhatsApp<input type="tel" name="phone" required autocomplete="tel"></label>
        </div>
        <div class="row">
          <label>Enquiry type
            <select name="enquiry_type" required>
              <option value="">Select</option>
              <option>Full camp management proposal</option><option>Specific service (housekeeping, catering, maintenance…)</option>
              <option>Mobilisation / takeover of an existing camp</option><option>Partnership or vendor enquiry</option><option>General enquiry</option>
            </select></label>
          <label>Approximate capacity (beds)<input type="text" name="capacity" placeholder="e.g. 1,200"></label>
        </div>
        <label>Site location<input type="text" name="site_location" placeholder="Emirate / area"></label>
        <label>Message<textarea name="message" required placeholder="Describe your site, current arrangements and the scope you need."></textarea></label>
        <div class="form-msg" role="status"></div>
        <button class="btn btn-gold" type="submit">Send enquiry {ICONS['arrow']}</button>
        <span class="hint">By submitting you agree that Nexcamp may contact you regarding your enquiry.</span>
      </form>
    </div>
    <div class="reveal d2">
      <div class="contact-list">
        <a class="contact-item" href="tel:{PHONE_TEL}"><div class="ic">{ICONS['phone']}</div><div><strong>Call us</strong><span>{PHONE_DISPLAY}</span><small>Mobile · click to call</small></div></a>
        <a class="contact-item" href="{WA}" target="_blank" rel="noopener"><div class="ic">{ICONS['wa']}</div><div><strong>WhatsApp</strong><span>{PHONE_DISPLAY}</span><small>Chat with our team</small></div></a>
        <a class="contact-item" href="mailto:{EMAIL}"><div class="ic">{ICONS['mail']}</div><div><strong>Email</strong><span>{EMAIL}</span><small>We reply within one business day</small></div></a>
        <div class="contact-item"><div class="ic">{ICONS['pin']}</div><div><strong>Office</strong><span>Office No. 8, Habshan 2</span><small>PO Box 232505, Abu Dhabi, United Arab Emirates</small></div></div>
        <div class="contact-item"><div class="ic">{ICONS['clock']}</div><div><strong>Office hours</strong><span>Monday – Friday, 8:00 – 18:00</span><small>Site operations run 24/7</small></div></div>
      </div>
    </div>
  </div>
</section>
<section class="section tight bg-cream">
  <div class="container">
    <div class="map reveal"><iframe src="{MAP_EMBED}" title="Nexcamp office location map" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="section-head reveal"><span class="eyebrow">Frequently Asked</span><h2>Common questions from owners and contractors</h2></div>
    <div class="reveal">
      <details open><summary>Can Nexcamp take over an existing camp mid-contract?</summary><p>Yes. Our 45-day mobilisation plan is designed for both new and existing camps: site survey and handover checklist in week one, team onboarding and service mapping by day 20, and full operating routines with a KPI baseline by day 45.</p></details>
      <details><summary>Do you offer individual services or only full camp management?</summary><p>Both. Many clients engage us for the full operating model, but we also deliver single service lines such as housekeeping and laundry, catering oversight, maintenance and MEP, or HSE support.</p></details>
      <details><summary>How do you report performance?</summary><p>Clients receive a Monthly Management Pack covering occupancy, maintenance register, HSE observations, service-level performance, resident feedback and open decisions, supported by daily and weekly operational logs.</p></details>
      <details><summary>Which regions do you cover?</summary><p>We are based in Abu Dhabi and support sites across the United Arab Emirates, including remote and industrial locations.</p></details>
    </div>
  </div>
</section>
"""
    html += footer()
    return html

# ============================================================ BUILD
PAGES = {"index.html": home, "about.html": about, "services.html": services,
         "industries.html": industries, "careers.html": careers, "contact.html": contact}

def main():
    for name, fn in PAGES.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(fn())
        print("wrote", name)
    today = datetime.date.today().isoformat()
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for name in PAGES:
            loc = SITE_URL + "/" + ("" if name == "index.html" else name)
            f.write(f"  <url><loc>{loc}</loc><lastmod>{today}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n")
    with open(os.path.join(OUT, "404.html"), "w") as f:
        f.write(head("Page not found | Nexcamp", "Page not found", "404.html") + header(True) +
                '<section class="section" style="padding-top:160px"><div class="container center"><span class="eyebrow">404</span><h1>Page not found</h1><p class="lead">The page you are looking for has moved or does not exist.</p><a class="btn btn-green" href="index.html">Back to home</a></div></section>' + footer())
    print("done")

if __name__ == "__main__":
    main()
