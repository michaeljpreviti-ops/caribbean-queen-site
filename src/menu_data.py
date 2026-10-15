# Menu transcribed from Caribbean Queen's printed menu card (kept here as menu-card.jpg).
# That card replaced the old laminated counter board — menu-board.jpg is kept for
# reference only. Differences from the board: "Soups on the Avenue" is a new section,
# Sides are listed by name, the two unreadable roots tonics turn out to be Lion Roots
# and Zion Roots, and Jerk Wings are gone.
#
# PRICES ARE DELIBERATELY NOT HERE. The card carries them; the owner is supplying the
# current ones separately. Sizes are not prices and are kept, because which sizes a dish
# comes in is how you order it.
#
# item    = (name, description, sizes, starred, note)
# section = (slug, name, colour, blurb, tagline, items)

SIZES3 = "Express &middot; Medium &middot; Large"
SIZES2 = "Small &middot; Large"

MENU = [
 ("specialties", "Jamaican Specialties", "green",
  "Every plate comes three ways &mdash; Express, Medium or Large &mdash; with rice and a side.",
  "Bold Jamaican flavors!",
  [
   ("Oxtails",
    "Slow-cooked until the meat gives way, in the gravy it made. The dish Caribbean Queen "
    "is best known for.",
    SIZES3, True, ""),
   ("Curry Goat",
    "Bone-in goat stewed down in Jamaican curry until it falls apart. Ms. Queen&rsquo;s "
    "curry powder comes from home.",
    SIZES3, True, ""),
   ("Beef Stew",
    "Brown stew beef, cooked down slow with onion, pepper and thyme.",
    SIZES3, False, ""),
   ("Curry Chicken",
    "The same curry, over chicken. The weekday regular.",
    SIZES3, True, ""),
   ("Jerk Chicken",
    "Marinated in pimento, scallion and scotch bonnet, then grilled dark. Served with "
    "rice and a side.",
    "Medium &middot; Large", True, "Half serving available"),
  ]),

 ("vegetarian", "Vegetarian Dishes", "green2",
  "Not one token dish &mdash; a section of its own, cooked in the same pots and the same "
  "seasoning as everything else.",
  "Plant power. Good food. Good vibes!",
  [
   ("Jerk Tofu",
    "Tofu carrying the full jerk marinade, grilled the way the chicken is.",
    SIZES3, False, ""),
   ("Curry Tofu",
    "Jamaican curry, tofu in place of the goat. Served over rice.",
    SIZES3, False, ""),
   ("Brown Stew Tofu",
    "Brown stew gravy &mdash; onion, pepper, thyme &mdash; over tofu.",
    SIZES3, False, ""),
   ("Ital Pasta",
    "Pasta with assorted vegetables, cooked ital &mdash; the Rastafarian way, clean and "
    "unsalted at the pot.",
    SIZES3, False, "With assorted veggies"),
  ]),

 ("fish", "Catch of the Day", "blue",
  "Whole fish, cooked to order. <b>Please call ahead</b> &mdash; (352) 374-8111.",
  "Fresh from the sea!",
  [
   ("Brown Stew Fish",
    "Fried, then finished in brown stew gravy with onion and sweet pepper.",
    "", False, "Call ahead"),
   ("Steamed Fish",
    "Steamed with okra, carrot and pepper, in its own broth.",
    "", False, "Call ahead"),
   ("Escovitch Fish",
    "Fried golden, then dressed in spiced vinegar with onion, carrot and scotch bonnet.",
    "", False, "Call ahead"),
  ]),

 ("soups", "Soups on the Avenue", "red",
  "Cooked down in the pot all morning and sold by the cup or the bowl.",
  "Hearty soups. Real Jamaican comfort!",
  [
   ("Chicken", "Chicken soup with ground provisions, carrot and dumplings.",
    SIZES2, False, ""),
   ("Chicken Foot", "Stewed long and slow, the way it is made at home.",
    SIZES2, False, ""),
   ("Goat Head", "Mannish water &mdash; the Jamaican goat head soup.",
    SIZES2, False, ""),
   ("Red Peas", "Red peas soup, thick with spinners.", SIZES2, False, ""),
   ("Gungo Peas", "Gungo &mdash; pigeon &mdash; peas, cooked down into soup.",
    SIZES2, False, ""),
  ]),

 ("patties", "Patties", "gold",
  "The quickest thing on the counter, baked and ready to carry out.",
  "Taste Jamaica in every bite!",
  [
   ("Mild Beef", "", "", False, ""),
   ("Spicy Beef", "", "", False, ""),
   ("Curry Chicken", "", "", False, ""),
   ("Jerk Chicken", "", "", False, ""),
   ("Veggie", "", "", False, ""),
   ("Soy", "", "", False, ""),
   ("Callaloo", "Jamaican greens, stewed.", "", False, ""),
  ]),

 ("sides", "Sides", "gold2",
  "Your plate comes with a side &mdash; say which one when you order.",
  "Simple sides. Big flavor!",
  [
   ("Pigeon Peas and Rice", "", "", False, ""),
   ("Red Beans and Rice", "", "", False, ""),
   ("Seasoned White Rice", "", "", False, ""),
   ("Herb Saut&eacute;ed Vegetables", "", "", False, ""),
   ("Fried Plantain", "", "", False, ""),
  ]),

 ("tropics", "Cool Tropics", "green",
  "Tropical juice, cold out of the cooler.",
  "Cool. Refreshing. Irresistible!",
  [
   ("Soursop", "", "", False, ""),
   ("Mango", "", "", False, ""),
   ("Pineapple / Ginger", "", "", False, ""),
   ("Passion Fruit", "", "", False, ""),
   ("Mango / Orange", "", "", False, ""),
  ]),

 ("drinks", "Drinks", "blue",
  "Jamaican sodas and roots tonics, straight off the island shelf.",
  "Taste the island in every sip!",
  [
   ("Cola Champagne", "", "", False, ""),
   ("Grape", "", "", False, ""),
   ("Pineapple", "", "", False, ""),
   ("Orange", "", "", False, ""),
   ("Cream", "", "", False, ""),
   ("Ginger Beer", "", "", False, ""),
   ("Jamaican Ting", "Grapefruit, properly bitter.", "", False, ""),
   ("Tiger &amp; Bone", "Jamaican roots tonic.", "", False, ""),
   ("Lion Roots", "Roots tonic.", "", False, ""),
   ("Zion Roots", "Roots tonic.", "", False, ""),
  ]),
]

# Section accent colours, drawn from the printed card: flag green, leaf green,
# sea blue, hibiscus red and the gold of the brush strokes behind every heading.
CAT_COLOR = {
 'green': 'var(--green)', 'green2': 'var(--leaf)', 'blue': 'var(--blue)',
 'red': 'var(--red)', 'gold': 'var(--gold-deep)', 'gold2': 'var(--gold-deep)',
 'char': 'var(--char)',
}
