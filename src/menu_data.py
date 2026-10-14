# Menu transcribed from the laminated menu board on Caribbean Queen's counter
# (photographed on their Google listing — the same photo is kept here as menu-board.jpg).
# Prices and wording are theirs, including the hand-written patty prices written over
# the printed ones. A star marks the four dishes Google's listing reports as most
# ordered; the board itself carries no stars.
#
# item = (name, description, price, starred, note)

MENU = [
 ("specialties", "Jamaican Specialties", "red",
  "Every plate comes three ways &mdash; Express, Medium or Large &mdash; with rice and a choice of side.",
  [
   ("Oxtails",
    "Slow-cooked until the meat gives way, in the gravy it made. The dish Caribbean Queen "
    "is best known for.",
    [("Express", "$7.75"), ("Medium", "$13.99"), ("Large", "$15.99")], True, ""),
   ("Curry Goat",
    "Bone-in goat stewed down in Jamaican curry until it falls apart. Ms. Queen&rsquo;s "
    "curry powder comes from home.",
    [("Express", "$7.75"), ("Medium", "$13.99"), ("Large", "$14.99")], True, ""),
   ("Curry Chicken",
    "The same curry, over chicken. The weekday regular &mdash; and the cheapest full plate "
    "on the board.",
    [("Express", "$6.75"), ("Medium", "$8.99"), ("Large", "$10.20")], True, ""),
   ("Jerk Chicken",
    "Marinated in pimento, scallion and scotch bonnet, then grilled dark. Served with "
    "rice and a side.",
    [("Medium", "$8.99"), ("Large", "$10.99")], True, "Half serving $12.20"),
   ("Beef Stew",
    "Brown stew beef, cooked down slow with onion, pepper and thyme.",
    [("Express", "$6.75"), ("Medium", "$9.99"), ("Large", "$10.99")], False, ""),
   ("Jerk Wings (6)",
    "Six wings, same jerk marinade, off the same grill.",
    [("Medium", "$8.99"), ("Large", "$10.20")], False, ""),
  ]),

 ("vegetarian", "Vegetarian Dishes", "green",
  "Not one token dish &mdash; a section of its own, cooked in the same pots and the same seasoning.",
  [
   ("Jerk Tofu",
    "Tofu carrying the full jerk marinade, grilled the way the chicken is.",
    [("Express", "$5.75"), ("Medium", "$7.75"), ("Large", "$8.50")], False, ""),
   ("Curry Tofu",
    "Jamaican curry, tofu in place of the goat. Served over rice.",
    [("Express", "$5.75"), ("Medium", "$7.75"), ("Large", "$8.50")], False, ""),
   ("Brown Stew Tofu",
    "Brown stew gravy &mdash; onion, pepper, thyme &mdash; over tofu.",
    [("Express", "$5.75"), ("Medium", "$7.75"), ("Large", "$8.50")], False, ""),
   ("Ital Pasta",
    "Pasta with assorted vegetables, cooked ital &mdash; the Rastafarian way, clean and "
    "unsalted at the pot.",
    [("Express", "$6.00"), ("Medium", "$7.75"), ("Large", "$8.75")], False,
    "With assorted veggies"),
  ]),

 ("fish", "Catch of the Day", "blue",
  "Whole fish, cooked to order. <b>Please call ahead</b> &mdash; (352) 374-8111.",
  [
   ("Brown Stew Fish",
    "Fried, then finished in brown stew gravy with onion and sweet pepper.",
    [("", "$14.75 and up")], False, "Call ahead"),
   ("Steamed Fish",
    "Steamed with okra, carrot and pepper, in its own broth.",
    [("", "$14.75 and up")], False, "Call ahead"),
   ("Escoviche Fish",
    "Fried golden, then dressed in spiced vinegar with onion, carrot and scotch bonnet.",
    [("", "$14.75 and up")], False, "Call ahead"),
  ]),

 ("patties", "Patties", "gold",
  "The quickest thing on the counter, and none of them over three dollars.",
  [
   ("Mild Beef", "", [("", "$2.40")], False, ""),
   ("Spicy Beef", "", [("", "$2.40")], False, ""),
   ("Curry Chicken", "", [("", "$2.50")], False, ""),
   ("Jerk Chicken", "", [("", "$2.50")], False, ""),
   ("Veggie", "", [("", "$2.30")], False, ""),
   ("Soy", "", [("", "$2.89")], False, ""),
   ("Callaloo", "Jamaican greens, stewed.", [("", "$2.89")], False, ""),
  ]),

 ("sides", "Sides", "gold2",
  "Your plate comes with these &mdash; say which when you order.",
  [
   ("Pidgeon Peas and Rice", "", [], False, ""),
   ("Red Beans and Rice", "", [], False, ""),
   ("Seasoned White Rice", "", [], False, ""),
   ("Herb Saut&eacute;ed Vegetables", "", [], False, ""),
   ("Fried Plantain", "", [], False, ""),
  ]),

 ("tropics", "Cool Tropics", "green",
  "Tropical juice, cold out of the cooler. Every one the same price.",
  [
   ("Soursap", "", [("", "$1.85")], False, ""),
   ("Mango", "", [("", "$1.85")], False, ""),
   ("Pineapple / Ginger", "", [("", "$1.85")], False, ""),
   ("Passion Fruit", "", [("", "$1.85")], False, ""),
   ("Mango / Orange", "", [("", "$1.85")], False, ""),
  ]),

 ("drinks", "Drinks", "blue",
  "Jamaican sodas and tonics, straight from the island shelf.",
  [
   ("Cola Champagne", "", [("", "$1.79")], False, ""),
   ("Grape", "", [("", "$1.79")], False, ""),
   ("Pineapple", "", [("", "$1.79")], False, ""),
   ("Orange", "", [("", "$1.79")], False, ""),
   ("Cream Soda", "", [("", "$1.79")], False, ""),
   ("Ginger Beer", "", [("", "$1.79")], False, ""),
   ("Jamaican Ting", "Grapefruit, properly bitter.", [("", "$2.69")], False, ""),
   ("Tiger &amp; Bone", "Jamaican roots tonic.", [("", "$3.50")], False, ""),
   ("Roots Tonic", "Two more roots tonics on the board.",
    [("", "$3.50 &ndash; $4.50")], False, "Ask at the counter"),
  ]),
]

CAT_COLOR = {
 'red': 'var(--red)', 'gold': 'var(--gold)', 'gold2': 'var(--gold)',
 'green': 'var(--green)', 'blue': 'var(--blue)', 'char': 'var(--char)',
}
