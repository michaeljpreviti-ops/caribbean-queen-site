# Caribbean Queen — website

A seven-page site for **Caribbean Queen**, Ms. Queen's Jamaican kitchen at
507 NW 5th Ave, Gainesville, Florida.

## Pages

| Page | File |
|---|---|
| Home | `index.html` |
| Menu (full, with prices) | `menu.html` |
| Our Story | `about.html` |
| Catering & big orders | `catering.html` |
| Visit (hours & directions) | `visit.html` |
| Privacy & cookies | `privacy.html` |
| Accessibility statement | `accessibility.html` |

The last two are deliberately **not** in the main navigation — they are linked from the footer
of every page.

## Why this exists

Caribbean Queen has **no website at all**. Their Google listing still shows "Add website".
Everything a customer can find — the menu, the prices, the hours — lives in a photograph of a
laminated board that somebody took on their phone. This site puts all 38 items into real HTML
that Google can read and a phone can display.

## How this is built

Same generator as the Di Big Jerk site, same stylesheet, same accessibility and consent
machinery. The HTML is **generated**:

| File | Holds |
|---|---|
| `src/menu_data.py` | the full menu — every item, description and price |
| `src/gen.py` | the facts, page copy and structure |
| `src/_css.css` | the single stylesheet, inlined into each page at build time |

```sh
OUTDIR=. python3 src/gen.py     # regenerate all 7 pages at the repo root
```

`OUTDIR` is required: with it unset the build writes to `site/` instead of the repo root.

> **Edit `src/`, not the `.html` files.** Anything typed into an `.html` file is overwritten
> on the next run.

## What is different from the Di Big Jerk build

- **No online ordering.** There is no Menufy, no DoorDash, no delivery app. Every "order" call
  to action is the phone number. The Visit page says so in plain words.
- **No social accounts.** No Instagram or Facebook page could be found, so the masthead social
  buttons, the hero "follow the kitchen" row and the footer social pills are gone. If they do
  have accounts, they drop straight back in — the CSS for them is still in the stylesheet.
- **No email address.** Every contact route is the phone. If they give you an address, add an
  `EMAIL` constant in `src/gen.py` and put it back in the footer and the two statement pages.
- **No logo file.** The masthead and footer typeset the card's lockup instead
  (`wordmark()` in `gen.py`, `.brandmark*` in the stylesheet). See **Theme** below.
- **Closed Saturdays.** The open/closed clock in the top bar now handles a closed day and skips
  over it when working out when the kitchen next opens — Friday evening correctly says
  "opens 10:30am Sunday". *(The Di Big Jerk build has a latent bug here: its "closed now" string
  prints a literal `·` instead of a middle dot. Fixed in this build, not touched there.)*
- **Three sizes** replace the weekly-specials block on the home page, because that is the
  genuinely unusual thing about this menu.
- **No prices anywhere.** See **Menu provenance** below.

## Menu provenance

Transcribed from **Caribbean Queen's printed menu card** (`menu-card.jpg`), which replaced
the old laminated counter board. `menu-board.jpg` is kept only for reference.

**There are no prices on this site.** The card carries them; the owner is supplying the
current ones separately. Every place a price used to sit now shows the sizes a dish comes
in instead, and the menu page says plainly to call. To put prices back, add them to the
items in `src/menu_data.py` and give `size_block()` a price slot.

What the new card changed:

- **"Soups on the Avenue" is a new section** — chicken, chicken foot, goat head, red peas
  and gungo peas, small or large.
- **The two unreadable roots tonics are solved.** They are **Lion Roots** and **Zion Roots**.
- **Sides are named on the card now**, so they are on the site by name.
- **Jerk Wings are gone.** They were on the old board and are not on the card, so they have
  been dropped. Worth confirming they really are off.
- Spellings corrected to the card: **Escovitch** (not escoviche), **Soursop** (not soursap),
  **Pigeon Peas** (not pidgeon).
- The card's own section lines are used as written — *Bold Jamaican flavors!*,
  *Plant power. Good food. Good vibes!*, *Fresh from the sea!*, *Hearty soups. Real Jamaican
  comfort!*, *Simple sides. Big flavor!*, *Taste Jamaica in every bite!*, *Cool. Refreshing.
  Irresistible!*, *Taste the island in every sip!*
- The star still marks the four dishes **Google reports as most ordered** — Oxtails, Curry
  Goat, Curry Chicken, Jerk Chicken. Neither the card nor the board carries stars of its own,
  and the legend says so.
- **The dish descriptions are written for this site.** The card has none. They are standard
  Jamaican preparations and nothing is invented about the food, but **Ms. Queen should read
  them and change anything she does not recognise** before this goes anywhere. The five soup
  descriptions are the newest and the least checked.

## Theme

The site is themed off the printed card rather than the old counter board:

- **Jamaican flag colours** — flag green `#0C8A3E`, gold `#FFC400` and black `#0B0B0B`, with
  the card's hibiscus red and sea blue as accents, on near-white paper.
- **The flag itself** sits in the top right corner of every page, drawn as inline SVG
  (`flag()` in `gen.py`) so it stays crisp and needs no image file.
- **Section headings sit on a painted gold brush band**, the way the card's do, with the
  section tagline beside them in script.
- **The wordmark** is the card's lockup — gold crown, *Caribbean* in green script and *Queen*
  in gold, JAMAICA RESTAURANT beneath. It is **set in type (Yellowtail), not cut from the
  card**, because the only copy of the card we have is a phone photograph of a tablet screen.
  **Swap in the real artwork when the designer's file turns up** — it will be an improvement.
- The card's own lines are used across the site: *Authentic Jamaican flavors, made with love*
  in the hero and footer, *Good Food Brings People Together* on a wooden sign above the
  closing call to action, and *Food · Culture · Community · One Jamaica* along the footer base.

## Photographs

The six food photographs are **customer photographs from the restaurant's Google listing**,
cropped to 3:4 and resized to 480×640. They are real plates from this kitchen, which is what
makes them worth using for the pitch — but they are not the restaurant's own property.
**Replace them with the owner's photographs** (or shoot new ones) before this is anything more
than a demo.

## Open questions for the owner

- **Is it cash only?** Yelp and Menupix both list Caribbean Queen as cash only. That is a big
  thing for a customer to find out at the counter, so it belongs on the Visit page — but it is
  not on this site yet, because neither source is the restaurant. **Ask, then add it.**
- **Hours.** The site uses the Google listing: Mon–Thu 10:30am–6:30pm, Fri & Sun 10:30am–5pm,
  closed Saturday. Yellow Pages says 10am–10:30pm daily and one aggregator says 11am–9pm
  Mon–Sat. Google is the most recently maintained of the three, but confirm it.
- **The story.** The About page draws on a 2016 *Independent Florida Alligator* profile:
  Valerie Phillips, raised in Clarendon, opened Caribbean Queen in 2000 as Gainesville's first
  Jamaican restaurant; her husband Errol cooks with her; the spices come back from Jamaica.
  **That article is ten years old.** Confirm she still owns it, that Errol is still cooking, and
  that she is happy being named before this is published.
- **Prices.** They are deliberately not on the site. Send them over and they go in.
- **Jerk Wings.** On the old counter board, not on the new card. Dropped from the site —
  confirm that is right.
- **Catering.** Nothing in any listing says they cater. The catering page is written as
  "call and ask", with no claim that trays are a standing offer. If they do not cater, drop the
  page from `PAGES` in `gen.py` and the nav closes up by itself.
- **No photograph of the building.** A storefront shot would improve the Visit page a lot.
- **Both statement pages are stamped October 14, 2026** (`TODAY` in `gen.py`). Bump it when
  either one changes.
- **The logo artwork.** The wordmark here is typeset from the card. If whoever printed the
  card still has the artwork, that file is worth asking for.

## Deploying

Vercel serves the repo root as static files — no build step. Pushes to `main` deploy.
`src/deploy.py` is a direct-to-REST-API fallback for machines with no Node or Vercel CLI,
but note the Vercel token on this machine is scoped to a SAML team it cannot reach, so
**the first deploy has to be done by importing this repo in the Vercel dashboard.**
