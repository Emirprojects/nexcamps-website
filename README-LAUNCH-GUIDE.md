# Nexcamp Website – Launch Guide

This folder contains the complete Nexcamp website (English). It is a static site: plain HTML, CSS, JavaScript and images. It needs no database and no special server, so it can be hosted almost anywhere and will load quickly.

## What is in the folder

| File / folder | Purpose |
|---|---|
| `index.html` | Home page |
| `about.html` | About: who we are, vision, mission, values, management approach, 45-day mobilisation plan, reporting & KPIs, team |
| `services.html` | All eight service lines, operating scope, safety & compliance |
| `industries.html` | Six industries served and the partnership model |
| `careers.html` | Roles we hire and an application form with CV upload |
| `contact.html` | Proposal request form, contact details, map and FAQ |
| `404.html` | Friendly "page not found" page |
| `css/style.css` | All styling (brand colours: green #1f4a3a, gold #b38c2f, cream #f6f1e7) |
| `js/main.js` | Menu, animations, form handling |
| `img/` | Optimised photos (≈11 MB total) and brand assets in `img/brand/` |
| `sitemap.xml`, `robots.txt` | For Google indexing |

## Step 1 – Choose a host (you only have the domain at GoDaddy)

Because the site is static, the simplest options are static hosts. Two good choices:

**Option A – Netlify (recommended)**
1. Go to netlify.com and create a free account.
2. Choose "Add new site" → "Deploy manually" and drag-and-drop this whole folder (or the zip contents).
3. Netlify gives you a temporary address like `something.netlify.app`. Check the site works.
4. Both forms (Contact and Careers) are already set up for **Netlify Forms**. In the Netlify dashboard go to *Forms* and add `info@nexcamps.com` as an email notification. Submissions, including uploaded CVs, will then arrive by email. (Free plan includes a monthly quota of submissions; check the current limits.)

**Option B – GoDaddy Web Hosting**
If you prefer to keep everything at GoDaddy, buy a basic hosting plan, open cPanel → File Manager, and upload the contents of this folder into `public_html`. Note: the forms will not work by themselves on GoDaddy hosting; they will fall back to opening the visitor's email app addressed to info@nexcamps.com. To have real form submissions there, connect the forms to a service such as Formspree or Basin (each gives you a form URL to paste into the `action="..."` attribute of the two `<form>` tags).

## Step 2 – Connect the domain nexcamps.com

For Netlify:
1. In Netlify: *Domain management* → *Add a domain* → enter `nexcamps.com`. Netlify will show you the DNS records it needs.
2. In GoDaddy: *My Products* → *DNS* next to nexcamps.com. Add/replace:
   - an **A record** for `@` pointing to the IP Netlify shows (currently `75.2.60.5`, but use the value Netlify displays), and
   - a **CNAME record** for `www` pointing to your `something.netlify.app` address.
3. Wait up to a few hours for DNS to update. Netlify then issues a free HTTPS certificate automatically.

For GoDaddy hosting the domain is linked automatically when you buy the plan.

## Step 3 – After launch

- **Google Search Console**: add nexcamps.com and submit `https://www.nexcamps.com/sitemap.xml`.
- **Google Business Profile**: create a listing for the Abu Dhabi office so the company appears on Maps.
- **Map on the Contact page**: it currently searches for "Habshan 2, Abu Dhabi". To pin the exact office, open Google Maps, find the office, click *Share* → *Embed a map*, copy the `src` URL and replace the `MAP_EMBED` value in `build.py` (or the iframe `src` in `contact.html`).

## Editing the site

- **Text changes**: open the relevant `.html` file in any text editor (VS Code is free), edit the text, save and re-upload that file.
- **Photos**: replace files in `img/` keeping the same filename, or add new ones and change the `src` in the HTML.
- **Rebuilding all pages at once**: the pages are generated from `build.py` (Python). Editing that file and running `python3 build.py` regenerates every page with consistent headers and footers.

## Things to review before launch

- Office hours on the Contact page are set to Monday–Friday 08:00–18:00. Change if needed.
- The FAQ answers and industry descriptions were written from the company profile; please review the wording.
- Arabic version: the structure is ready for a `/ar/` folder when you want to add it.
