#!/usr/bin/env python3
"""Builds the Caribbean Queen site. OUTDIR / INDEX_STANDALONE control the target."""
import os, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from menu_data import MENU, CAT_COLOR

HERE = os.path.dirname(os.path.abspath(__file__))
OUT  = os.path.normpath(os.path.join(HERE, '..', os.environ.get('OUTDIR', 'site')))
INDEX_STANDALONE = os.environ.get('INDEX_STANDALONE', '1') == '1'
CSS  = open(os.path.join(HERE, '_css.css'), encoding='utf-8').read()

# ---------------------------------------------------------------- facts
NAME    = "Caribbean Queen"
PHONE_T = "(352) 374-8111"
PHONE_H = "tel:+13523748111"
ADDR1   = "507 NW 5th Ave"
ADDR2   = "Gainesville, FL 32601"
MAPS    = ("https://www.google.com/maps/dir/?api=1&destination="
           "Caribbean+Queen%2C+507+NW+5th+Ave%2C+Gainesville%2C+FL+32601")
MAPS_PL = ("https://www.google.com/maps/place/Caribbean+Queen/"
           "@29.6554959,-82.3299333,17z/data=!4m6!3m5!1s0x88e8a389697fea59:"
           "0x6c01334397afe9b9!8m2!3d29.6554959!4d-82.3299333!16s%2Fg%2F1pp2vhn24")
YELP    = "https://www.yelp.com/biz/caribbean-queen-gainesville"
BOARD   = "menu-card.jpg"           # photograph of the printed menu card
TODAY   = "October 14, 2026"        # stamped on the privacy and accessibility pages
OPENED  = "2000"
G_RATING, G_PCT, G_COUNT = "4.1", "82%", "232"   # read from the Google listing

# Hours as published on their Google listing. Saturday is the closed day.
HOURS = [("Monday","10:30am","6:30pm"),("Tuesday","10:30am","6:30pm"),
         ("Wednesday","10:30am","6:30pm"),("Thursday","10:30am","6:30pm"),
         ("Friday","10:30am","5:00pm"),("Saturday","Closed",None),
         ("Sunday","10:30am","5:00pm")]


I = {
 'phone':'<path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1-9.4 0-17-7.6-17-17 0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .7-.2 1l-2.3 2.2z"/>',
 'pin':'<path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/>',
 'clock':'<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20zm.9 10.6-3.6 2.3-.8-1.3 3-1.9V6.5h1.4v6.1z"/>',
 'dir':'<path d="M21.7 11.3 12.7 2.3a1 1 0 0 0-1.4 0l-9 9a1 1 0 0 0 0 1.4l9 9a1 1 0 0 0 1.4 0l9-9a1 1 0 0 0 0-1.4zM13 15v-2.5h-3V15l-3-3.5L10 8v2.5h4V15h-1z"/>',
 'bag':'<path d="M18 6h-2a4 4 0 0 0-8 0H6a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2zm-6-2a2 2 0 0 1 2 2h-4a2 2 0 0 1 2-2z"/>',
 'mail':'<path d="M20 4H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2zm0 4.2-8 5-8-5V6l8 5 8-5v2.2z"/>',
 'fb':'<path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.7-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/>',
 'ig':'<path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.3 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c0 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2 0-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c0-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.8A6 6 0 1 0 12 18a6 6 0 0 0 0-12zm0 9.9A3.9 3.9 0 1 1 12 8.2a3.9 3.9 0 0 1 0 7.7zm7.6-10.3a1.4 1.4 0 1 1-2.8 0 1.4 1.4 0 0 1 2.8 0z"/>',
 'star':'<path d="m12 17.3-6.2 3.7 1.7-7-5.4-4.7 7.1-.6L12 2l2.8 6.7 7.1.6-5.4 4.7 1.7 7z"/>',
 'menu':'<path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/>',
 'pdf':'<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8l-6-6zm-1 7V3.5L18.5 9H13z"/>',
 'prev':'<path d="M15.4 4.6 8 12l7.4 7.4 1.4-1.4L10.8 12l6-6z"/>',
 'next':'<path d="M8.6 4.6 7.2 6l6 6-6 6 1.4 1.4L16 12z"/>',
 'a11y':'<path d="M20.5 6c-2.6.7-5.7 1-8.5 1s-5.9-.3-8.5-1L3 8c1.9.5 4 .8 6 1v13h2v-6h2v6h2V9c2-.2 4.1-.5 6-1l-.5-2zM12 6a2 2 0 1 0 0-4 2 2 0 0 0 0 4z"/>',
 'cookie':'<path fill-rule="evenodd" d="M12 2a10 10 0 1 0 10 10 2.9 2.9 0 0 1-3.9-3.2A2.9 2.9 0 0 1 14.6 4 2.9 2.9 0 0 1 12 2zM8.2 8.6a1.3 1.3 0 1 1 0 2.6 1.3 1.3 0 0 1 0-2.6zm.9 5.1a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4zm4.5 1.5a1.3 1.3 0 1 1 0 2.6 1.3 1.3 0 0 1 0-2.6zm.4-5.6a1.4 1.4 0 1 1 0 2.8 1.4 1.4 0 0 1 0-2.8zm4.1 3.1a1.2 1.2 0 1 1 0 2.4 1.2 1.2 0 0 1 0-2.4z"/>',
 'x':'<path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19 12 13.4 17.6 19 19 17.6 13.4 12z"/>',
 'shield':'<path d="M12 2 4 5v6.1c0 5 3.4 9.7 8 10.9 4.6-1.2 8-5.9 8-10.9V5l-8-3zm-1 14.5-3.5-3.5 1.4-1.4L11 13.7l4.7-4.7 1.4 1.4-6.1 6.1z"/>',
}
def ico(k): return '<svg viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % I[k]

PAGES = [('index','Home','index.html'), ('menu','Menu','menu.html'),
         ('about','Our Story','about.html'), ('catering','Catering','catering.html'),
         ('visit','Visit','visit.html')]

def wordmark(sub=True):
    """The lockup from Caribbean Queen's printed menu card: a gold crown over
    'Caribbean' in green script and 'Queen' in gold, with JAMAICA RESTAURANT beneath.
    Set in type rather than cut from the card, which is only a phone photograph."""
    crown = ('<svg class="crown" viewBox="0 0 24 24" aria-hidden="true">'
             '<path d="M2.6 7.4 7.3 11 12 3.4 16.7 11l4.7-3.6L19.6 19H4.4L2.6 7.4z"/>'
             '<path d="M4.4 20.3h15.2v2.3H4.4z"/></svg>')
    return ('<span class="brandmark">%s<span class="brandmark__t">'
            '<span class="brandmark__k">Caribbean <b>Queen</b></span>'
            '<span class="brandmark__n">Jamaica <i>Restaurant</i></span>%s</span></span>'
            % (crown, '<span class="brandmark__s">507 NW 5th Ave &middot; Gainesville</span>'
               if sub else ''))

def flag(cls="flag"):
    """The flag of Jamaica: gold saltire, green above and below, black hoist and fly."""
    return ('<svg class="%s" viewBox="0 0 24 12" role="img" '
            'aria-label="Flag of Jamaica">'
            '<path d="M0 0h24v12H0z" fill="#FFC400"/>'
            '<path d="M0 0h24l-12 6z" fill="#0C8A3E"/>'
            '<path d="M0 12h24l-12-6z" fill="#0C8A3E"/>'
            '<path d="M0 0v12l12-6z" fill="#0B0B0B"/>'
            '<path d="M24 0v12l-12-6z" fill="#0B0B0B"/>'
            '<path d="M0 0 24 12M0 12 24 0" stroke="#FFC400" stroke-width="2.1" fill="none"/>'
            '</svg>') % cls

def head(key):
    nav = ''.join('<a href="%s"%s>%s</a>' % (h, ' aria-current="page"' if k == key else '', l)
                  for k, l, h in PAGES)
    return """<a class="skip" href="#main">Skip to content</a>
<div class="util" role="region" aria-label="Address, hours and phone"><div class="wrap util__in">
  <span class="util__i">{pin} {a1}, {a2}</span>
  <span class="util__i"><span class="open-dot" id="open-dot"></span><span id="open-now">Open 10:30am&ndash;6:30pm today</span></span>
  <span class="util__sp"></span>
  <span class="util__i">Dine in &middot; Takeout</span>
  <a class="util__ph" href="{ph}">{phi} {pht}</a>
  <span class="util__flag"><b>One Jamaica</b>{flag}</span>
</div></div>
<header class="mast"><div class="wrap mast__in">
  <a class="brand" href="index.html" aria-label="Caribbean Queen &mdash; home">{wm}</a>
  <span class="mast__sp"></span>
  <button class="navtoggle" id="navtoggle" aria-expanded="false" aria-controls="nav">{mn} Menu</button>
  <nav class="nav" id="nav" aria-label="Main">{nav}</nav>
  <div class="mast__cta">
    <a class="btn btn--ghost btn--sm btn--hide-sm" href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
    <a class="btn btn--red btn--sm" href="{ph}">{phi} Call to Order</a>
  </div>
</div></header>""".format(nav=nav, a1=ADDR1, a2=ADDR2, ph=PHONE_H, pht=PHONE_T, maps=MAPS,
                          pin=ico('pin'), phi=ico('phone'), dir=ico('dir'),
                          mn=ico('menu'), wm=wordmark(False), flag=flag())


FOOT_HTML = """<section class="sec sec--char" aria-labelledby="hungry" style="border-top:5px solid var(--gold-bright)">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:1.4rem;align-items:center;justify-content:space-between">
    <div style="display:flex;flex-direction:column;gap:.75rem;min-width:0">
      <p class="signboard">Good Food Brings People Together</p>
      <h2 id="hungry">Hungry yet?</h2>
      <p class="lede">Call the kitchen and it will be boxed and waiting. Fish needs a little
        more notice &mdash; say so when you ring.</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.6rem">
      <a class="btn btn--gold btn--lg" href="{ph}">{phi} {pht}</a>
      <a class="btn btn--onchar btn--lg" href="menu.html">See the Menu</a>
    </div>
  </div>
</section>
<footer class="foot"><div class="wrap">
  <div class="foot__grid">
    <div class="foot__brand">
      {wm}
      <p class="script" style="margin-top:.2rem">Authentic Jamaican flavors, made with love</p>
      <p>Ms. Queen&rsquo;s Jamaican kitchen on Northwest Fifth Avenue, cooking oxtail,
         curry goat and jerk chicken in Gainesville since {opened}.</p>
      <div class="social">
        <a href="{yelp}" target="_blank" rel="noopener" aria-label="Caribbean Queen on Yelp">{sti}</a>
        <a href="{maps_pl}" target="_blank" rel="noopener" aria-label="Caribbean Queen on Google">{pini}</a>
      </div>
    </div>
    <div><h3>Eat</h3><ul>
      <li><a href="menu.html">Full Menu</a></li>
      <li><a href="menu.html#specialties">Jamaican Specialties</a></li>
      <li><a href="menu.html#vegetarian">Vegetarian Dishes</a></li>
      <li><a href="menu.html#fish">Catch of the Day</a></li>
      <li><a href="{board}">The printed menu (photo)</a></li>
    </ul></div>
    <div><h3>Visit</h3><ul>
      <li>{a1}<br>{a2}</li>
      <li><a href="{maps}" target="_blank" rel="noopener">Get directions &rarr;</a></li>
      <li style="padding-top:.45rem">Mon&ndash;Thu: 10:30am &ndash; 6:30pm<br>
        Fri &amp; Sun: 10:30am &ndash; 5pm<br>Saturday: closed</li>
    </ul></div>
    <div><h3>Order &amp; Catering</h3>
      <a class="foot__ph" href="{ph}">{pht}</a>
      <ul style="padding-top:.6rem">
        <li>Call to order for pickup</li>
        <li><a href="catering.html">Catering &amp; big orders</a></li>
        <li><a href="visit.html">Hours &amp; directions</a></li>
      </ul>
    </div>
  </div>
  <div class="foot__base">
    <span class="oneja">{flag} Food <i>&middot;</i> Culture <i>&middot;</i> Community
      <i>&middot;</i> One Jamaica <i>&hearts;</i></span>
    <span>&copy; 2026 Caribbean Queen.</span>
    <span>507 NW 5th Ave &middot; Gainesville, Florida</span>
    <span class="foot__legal">
      <a href="accessibility.html">Accessibility</a>
      <a href="privacy.html">Privacy &amp; cookies</a>
      <button class="foot__lbtn" type="button" data-a11y-open>Accessibility tools</button>
      <button class="foot__lbtn" type="button" data-cc-open>Cookie settings</button>
    </span>
  </div>
</div></footer>
<nav class="dock" aria-label="Quick actions">
  <a href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
  <a href="menu.html">{mn} Menu</a>
  <a class="dock--primary" href="{ph}">{phi} Call to Order</a>
</nav>"""


CONTROLS_HTML = """<!-- ------------------------------------------------ cookie / storage consent -->
<div class="cc" id="cc" role="dialog" aria-labelledby="cc-h" aria-describedby="cc-p" hidden>
  <div class="cc__card" id="cc-card" tabindex="-1">
    <div class="cc__head">{cki}<h2 id="cc-h">Your choices about cookies</h2></div>
    <p class="cc__p" id="cc-p">This site keeps a little information on your device so it works and
      remembers your accessibility settings. Anything beyond that &mdash; measuring how the site
      gets used, or letting a social network see that a post brought you here &mdash;
      happens only if you say yes.</p>
    <button class="cc__toggle" type="button" data-cc-toggle aria-expanded="false"
            aria-controls="cc-opts">Choose categories one by one</button>
    <ul class="cc__opts" id="cc-opts">
      <li><label class="cc__opt">
        <input type="checkbox" checked disabled>
        <span><b>Strictly necessary <i>&mdash; always on</i></b>
          Remembers the choice you make here and your accessibility settings. Held on your own
          device and sent to nobody.</span>
      </label></li>
      <li><label class="cc__opt">
        <input type="checkbox" id="cc-analytics">
        <span><b>Analytics</b>
          Anonymous counts of which pages and dishes people look at, so the kitchen knows what to
          put up front. Nothing of the sort loads unless you allow it.</span>
      </label></li>
      <li><label class="cc__opt">
        <input type="checkbox" id="cc-marketing">
        <span><b>Social &amp; marketing</b>
          Would let a social network work out whether one of its posts brought you here.
          Nothing of the sort loads unless you allow it.</span>
      </label></li>
    </ul>
    <div class="cc__act">
      <button class="btn btn--gold" type="button" data-cc-set="all">Accept all</button>
      <button class="btn btn--ghost" type="button" data-cc-set="none">Necessary only</button>
      <button class="btn btn--ghost" type="button" data-cc-set="save">Save my choices</button>
    </div>
    <p class="cc__fine" id="cc-gpc" hidden>{shi} Your browser is sending a
      <b>Global Privacy Control</b> or <b>Do Not Track</b> signal, so both optional categories
      stay switched off and cannot be turned on. We respect that.</p>
    <p class="cc__fine">{shi} Change your mind any time with <b>Cookie settings</b> at the bottom
      of any page. The detail is in our
      <a href="privacy.html">privacy &amp; cookie policy</a>.</p>
  </div>
</div>

"""

FOOT_JS = r"""(function(){
  // "Stop animation" in the accessibility panel counts the same as the OS setting.
  function reduced(){
    return (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)
        || document.documentElement.getAttribute('data-a11y-motion') === 'off';
  }

  var t=document.getElementById('navtoggle'), n=document.getElementById('nav');
  if(t&&n){t.addEventListener('click',function(){
    var o=n.classList.toggle('is-open'); t.setAttribute('aria-expanded',o?'true':'false');
  });}

  // Open / closed, computed in the restaurant timezone rather than the viewer timezone.
  // Minutes from midnight, Sun..Sat; null is a closed day (Saturday).
  var HOURS=[[630,1020],[630,1110],[630,1110],[630,1110],[630,1110],[630,1020],null];
  function hhmm(m){
    var h=Math.floor(m/60), mm=m%60, ap=h>=12?'pm':'am', h12=h%12||12;
    return h12+(mm?':'+(mm<10?'0':'')+mm:'')+ap;
  }
  function etNow(){
    try{
      var p=new Intl.DateTimeFormat('en-US',{timeZone:'America/New_York',weekday:'short',
        hour:'numeric',minute:'numeric',hour12:false}).formatToParts(new Date());
      var g={}; p.forEach(function(x){g[x.type]=x.value;});
      var d=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'].indexOf(g.weekday);
      var h=parseInt(g.hour,10)%24, m=parseInt(g.minute,10);
      return d<0?null:{d:d,mins:h*60+m};
    }catch(e){ return null; }
  }
  var now=etNow(), dot=document.getElementById('open-dot'), lbl=document.getElementById('open-now');
  if(now&&dot&&lbl){
    var t=HOURS[now.d], open=!!t&&now.mins>=t[0]&&now.mins<t[1];
    // the next day that is not closed
    var nd=now.d, hop=0;
    do{ nd=(nd+1)%7; hop++; }while(!HOURS[nd]&&hop<8);
    var DAY=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    dot.setAttribute('data-shut', open?'0':'1');
    if(open){ lbl.textContent='Open now until '+hhmm(t[1]); }
    else if(t&&now.mins<t[0]){ lbl.textContent='Opens at '+hhmm(t[0])+' today'; }
    else if(t){ lbl.textContent='Closed now · opens '+hhmm(HOURS[nd][0])+' '+DAY[nd]; }
    else { lbl.textContent='Closed Saturdays · open '+DAY[nd]+' '+hhmm(HOURS[nd][0]); }
    // mark the current day on any hours list
    document.querySelectorAll('[data-day]').forEach(function(r){
      if(+r.getAttribute('data-day')===now.d) r.classList.add('is-today');
    });
  }

  // ---- dish photo carousel ----
  document.querySelectorAll('[data-pcar]').forEach(function(root){
    var vp=root.querySelector('[data-vp]'), track=root.querySelector('[data-track]'),
        prev=root.querySelector('[data-prev]'), next=root.querySelector('[data-next]'),
        dotbox=root.querySelector('[data-dots]'), count=root.querySelector('[data-count]'),
        timer=null, held=false;
    function slides(){ return Array.prototype.slice.call(track.children); }
    function step(){
      var sl=slides(); if(!sl.length) return 1;
      return sl[0].getBoundingClientRect().width + 18.4;
    }
    function perView(){
      var sl=slides(); if(sl.length<2) return 1;
      return Math.max(1, Math.round(vp.clientWidth/sl[0].getBoundingClientRect().width));
    }
    function index(){
      var sl=slides(); if(!sl.length) return 0;
      return Math.max(0, Math.min(sl.length-1, Math.round(vp.scrollLeft/step())));
    }
    function go(i, smooth){
      var sl=slides(); if(!sl.length) return;
      i=Math.max(0, Math.min(sl.length-1, i));
      var left=sl[i].offsetLeft-track.offsetLeft;
      if(smooth&&!reduced()&&vp.scrollTo) vp.scrollTo({left:left, behavior:'smooth'});
      else vp.scrollLeft=left;
    }
    function sync(){
      var i=index(), sl=slides(), last=Math.max(0, sl.length-perView());
      Array.prototype.forEach.call(dotbox.children, function(d,n){
        d.setAttribute('aria-selected', n===i?'true':'false');
      });
      if(count) count.textContent=(i+1)+' / '+sl.length;
      prev.disabled = i<=0;
      next.disabled = i>=last;
    }
    prev.addEventListener('click', function(){ go(index()-1, true); });
    next.addEventListener('click', function(){ go(index()+1, true); });
    dotbox.addEventListener('click', function(e){
      var d=e.target.closest('[data-dot]'); if(d) go(+d.getAttribute('data-dot'), true);
    });
    vp.addEventListener('keydown', function(e){
      if(e.key==='ArrowRight'){ e.preventDefault(); go(index()+1, true); }
      if(e.key==='ArrowLeft'){ e.preventDefault(); go(index()-1, true); }
    });
    var raf=null;
    vp.addEventListener('scroll', function(){
      if(raf) return;
      raf=requestAnimationFrame(function(){ raf=null; sync(); });
    });
    window.addEventListener('resize', sync);
    function stop(){ if(timer){ clearInterval(timer); timer=null; } }
    function start(){
      stop();
      if(reduced()||held||document.hidden||slides().length<2) return;
      timer=setInterval(function(){
        var sl=slides(), last=Math.max(0, sl.length-perView());
        go(index()>=last?0:index()+1, true);
      }, 4500);
    }
    ['mouseenter','focusin','touchstart','pointerdown'].forEach(function(ev){
      root.addEventListener(ev, function(){ held=true; stop(); }, {passive:true});
    });
    ['mouseleave','focusout'].forEach(function(ev){
      root.addEventListener(ev, function(){ held=false; start(); });
    });
    document.addEventListener('visibilitychange', function(){ document.hidden?stop():start(); });
    window.addEventListener('cq:motion', function(){ reduced()?stop():start(); });
    sync(); start();
  });

  document.querySelectorAll('[data-copy]').forEach(function(b){
    var label=b.textContent;
    function flash(m){ b.textContent=m; setTimeout(function(){b.textContent=label;},1700); }
    b.addEventListener('click',function(){
      var txt=b.getAttribute('data-copy');
      try{ navigator.clipboard.writeText(txt).then(function(){flash('Copied');},
            function(){flash('Copy failed');}); }
      catch(e){ flash('Copy failed'); }
    });
  });
})();
"""

A11Y_JS = r"""
/* ---------------------------------------------------------------------------
   Accessibility panel and cookie consent. Both store their state on the
   visitor's own device and send nothing anywhere. Any future analytics or
   pixel must sit behind window.CQ_CONSENT / the 'cq:consent' event.
   --------------------------------------------------------------------------- */
(function(){
  var R = document.documentElement;
  function flag(attr, on, val){ if(on) R.setAttribute(attr, val); else R.removeAttribute(attr); }


  /* ---------------- cookie / storage consent ---------------- */
  var CK = 'cq.consent.v1', YEAR = 365 * 24 * 60 * 60 * 1000;
  var cc  = document.getElementById('cc'),
      ana = document.getElementById('cc-analytics'),
      mkt = document.getElementById('cc-marketing');

  window.CQ_CONSENT = {analytics:false, marketing:false, answered:false};

  var GPC = (navigator.globalPrivacyControl === true) ||
            (navigator.doNotTrack === '1' || window.doNotTrack === '1');
  if(GPC){
    R.setAttribute('data-gpc', '1');
    [ana, mkt].forEach(function(b){ if(b){ b.checked = false; b.disabled = true; } });
  }

  function readCC(){
    try{
      var o = JSON.parse(localStorage.getItem(CK) || 'null');
      if(!o || o.v !== 1 || !o.t || (Date.now() - o.t) > YEAR) return null;
      return o;
    }catch(e){ return null; }
  }
  function publishCC(o){
    window.CQ_CONSENT = {analytics:!!o.analytics, marketing:!!o.marketing, answered:true};
    R.setAttribute('data-consent', ((o.analytics ? 'a' : '') + (o.marketing ? 'm' : '')) || 'n');
    try{
      window.dispatchEvent(new CustomEvent('cq:consent', {detail:window.CQ_CONSENT}));
    }catch(e){}
  }
  function showCC(on){
    if(!cc) return;
    cc.hidden = !on;
    flag('data-cc-open', on, '1');
    if(on){
      var card = document.getElementById('cc-card');
      if(card){ card.scrollTop = 0; card.focus(); }
    }
  }
  function saveCC(a, m){
    if(GPC){ a = false; m = false; }
    try{
      localStorage.setItem(CK, JSON.stringify({v:1, t:Date.now(), analytics:!!a, marketing:!!m}));
    }catch(e){}
    publishCC({analytics:a, marketing:m});
    showCC(false);
  }

  /* ---------------- wiring ---------------- */
  document.addEventListener('click', function(e){
    if(!e.target || !e.target.closest) return;
    var t = e.target.closest('[data-cc-set],[data-cc-open],[data-cc-toggle],[data-a11y-open]');
    if(!t) return;
    if(t.hasAttribute('data-a11y-open')){
      var nf = document.getElementById('a11yFab');
      if(nf) nf.click();
      return;
    }
    if(t.hasAttribute('data-cc-toggle')){
      var open = R.getAttribute('data-cc-opts') !== '1';
      flag('data-cc-opts', open, '1');
      t.setAttribute('aria-expanded', open ? 'true' : 'false');
      return;
    }
    if(t.hasAttribute('data-cc-open')){
      var cur = readCC() || {};
      if(ana) ana.checked = !!cur.analytics;
      if(mkt) mkt.checked = !!cur.marketing;
      showCC(true);
      return;
    }
    var how = t.getAttribute('data-cc-set');
    if(how === 'all' && GPC){ saveCC(false, false); return; }
    if(how === 'all'){
      if(ana) ana.checked = true;
      if(mkt) mkt.checked = true;
      saveCC(true, true);
    }else if(how === 'none'){
      if(ana) ana.checked = false;
      if(mkt) mkt.checked = false;
      saveCC(false, false);
    }else{
      saveCC(ana && ana.checked, mkt && mkt.checked);
    }
  });


  document.addEventListener('keydown', function(e){
    if(e.key !== 'Escape') return;
    /* The banner has no dismiss: a visitor who has not answered yet must choose.
       Once answered, re-opening it from the footer can be escaped. */
    if(cc && !cc.hidden && readCC()) showCC(false);
  });

  var gpcnote = document.getElementById('cc-gpc');
  if(gpcnote) gpcnote.hidden = !GPC;
  var had = readCC();
  if(had) publishCC(had); else showCC(true);
})();
"""

# ======================================================== ACCESSIBILITY TOOLBAR
# A visitor-facing panel of display preferences. It is deliberately a plain
# <aside> landmark holding a launcher and a non-modal dialog: no framework, no
# network call, and nothing it does is required for the page to work. Choices
# persist in localStorage; every read and write is guarded because private
# windows and blocked site data make both throw.
#
# All of the page-wide CSS it triggers is scoped to body>*:not(.a11y-ui) in
# _css.css, so the panel can never restyle its own controls out from under the
# visitor who is using them.

A11Y_ICONS = {
 'person':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.6a2.1 2.1 0 1 1 0 4.2 2.1 2.1 0 0 1 0-4.2zM3.4 7.9c2.7.9 5.6 1.4 8.6 1.4s5.9-.5 8.6-1.4a1.2 1.2 0 1 1 .7 2.3c-2 .6-4 1.1-6.1 1.3l.6 3.1 2.3 5.7a1.2 1.2 0 1 1-2.2.9L13.4 16h-2.8l-2.5 6.2a1.2 1.2 0 1 1-2.2-.9l2.3-5.7.6-3.1c-2.1-.2-4.1-.7-6.1-1.3a1.2 1.2 0 1 1 .7-2.3z"/></svg>',
 'aa':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M9 16l3-8 3 8M10 13.6h4"/></svg>',
 'cursor':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3.5l12 8.4-5.6 1 2.6 5.6-2.6 1.1-2.5-5.6-3.9 3.7z"/></svg>',
 'ls':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5v7M11 5v7M15 5v7M3 18h18M3 18l2.5-2.5M3 18l2.5 2.5M21 18l-2.5-2.5M21 18l-2.5 2.5"/></svg>',
 'align':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M7 10.7h10M4 15.3h16M7 20h10"/></svg>',
 'bold':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="4"/><path d="M9.5 8h3.1a2.1 2.1 0 0 1 0 4.2H9.5zm0 4.2h3.6a2.1 2.1 0 0 1 0 4.2H9.5z"/></svg>',
 'sun':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.4v2.1M12 19.5v2.1M4.2 4.2l1.5 1.5M18.3 18.3l1.5 1.5M2.4 12h2.1M19.5 12h2.1M4.2 19.8l1.5-1.5M18.3 5.7l1.5-1.5"/></svg>',
 'half':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 3.1a8.9 8.9 0 0 1 0 17.8z" fill="currentColor" stroke="none"/></svg>',
 'moon':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.3 14.6A8.6 8.6 0 0 1 9.4 3.7a8.9 8.9 0 1 0 10.9 10.9z"/></svg>',
 'mono':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M4.3 8.6h15.4M3.2 12.4h17.6M4.3 16.2h15.4"/></svg>',
 'rline':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="2.5" y="6.5" width="19" height="11" rx="3"/><path d="M7.4 12h.01M12 12h.01M16.6 12h.01"/></svg>',
 'rmask':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8.2c3-2.6 6-2.6 9 0s6 2.6 9 0M3 15.8c3 2.6 6 2.6 9 0s6-2.6 9 0"/></svg>',
 'noimg':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M3.8 17.2L9 12l3.4 3.4M14.4 13.6L16.8 11l3.4 3.4"/><path d="M14.4 6.2l3.6 3.6M18 6.2l-3.6 3.6"/></svg>',
 'spot':'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4.5" y="4.5" width="15" height="15" rx="2"/><circle cx="4.5" cy="4.5" r="1.9" fill="currentColor" stroke="none"/><circle cx="19.5" cy="4.5" r="1.9" fill="currentColor" stroke="none"/><circle cx="4.5" cy="19.5" r="1.9" fill="currentColor" stroke="none"/><circle cx="19.5" cy="19.5" r="1.9" fill="currentColor" stroke="none"/></svg>',
 'stop':'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M5.6 18.4L18.4 5.6"/></svg>',
 'link':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M10 13.8a4 4 0 0 0 5.7 0l2.8-2.9a4 4 0 0 0-5.7-5.6l-1.3 1.3"/><path d="M14 10.2a4 4 0 0 0-5.7 0l-2.8 2.9a4 4 0 0 0 5.7 5.6l1.3-1.3"/></svg>',
 'plus':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5.5v13M5.5 12h13"/></svg>',
 'minus':'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5.5 12h13"/></svg>',
}

def a11y_tile(key, label, icon):
    return ('<button class="a11y__tile" type="button" data-a11y-t="%s" aria-pressed="false">'
            '<span class="a11y__ic">%s</span>'
            '<span class="a11y__lab" data-lab="%s">%s</span></button>'
            % (key, A11Y_ICONS[icon], label, label))

def a11y_step(key, label):
    return ('<div class="a11y__step"><span id="a11y-%s-l">%s</span><div class="a11y__row">'
            '<button class="a11y__sbtn" type="button" data-a11y-s="%s" data-dir="1" '
            'aria-describedby="a11y-%s-l" aria-label="Increase %s">%s</button>'
            '<output class="a11y__out" id="a11y-%s-v" for="a11y-%s-l">Default</output>'
            '<button class="a11y__sbtn" type="button" data-a11y-s="%s" data-dir="-1" '
            'aria-describedby="a11y-%s-l" aria-label="Decrease %s">%s</button>'
            '</div></div>'
            % (key, label, key, key, label.lower(), A11Y_ICONS['plus'],
               key, key, key, key, label.lower(), A11Y_ICONS['minus']))

A11Y = ("""
<aside class="a11y-ui a11y-root" aria-label="Accessibility adjustments">
<button class="a11y-fab" id="a11yFab" type="button" aria-expanded="false" aria-controls="a11yPanel">
  """ + A11Y_ICONS['person'] + """<span class="vh">Accessibility adjustments</span>
</button>
<div class="a11y" id="a11yPanel" role="dialog" aria-labelledby="a11yTitle" hidden>
  <div class="a11y__head">
    <button class="a11y__x" type="button" data-a11y-close
            aria-label="Close accessibility adjustments">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/></svg>
    </button>
    <span class="a11y__mark">""" + A11Y_ICONS['person'] + """</span>
    <h2 id="a11yTitle">Accessibility Adjustments</h2>
    <p class="a11y__sub">Caribbean Queen &middot;
      <button class="a11y__hide" type="button" data-a11y-close>Hide Toolbar</button></p>
  </div>
  <div class="a11y__body">
    <section class="a11y__grp" aria-labelledby="a11yG1">
      <h3 id="a11yG1">Content Modules</h3>
      <div class="a11y__grid">
        """ + a11y_step('fs', 'Font Size') + a11y_tile('readable', 'Readable Font', 'aa') + """
        """ + a11y_step('lh', 'Line Height') + a11y_tile('cursor', 'Big Cursor', 'cursor') + """
        """ + a11y_tile('ls', 'Letter Spacing', 'ls')
            + a11y_tile('align', 'Align Text', 'align')
            + a11y_tile('weight', 'Font Weight', 'bold') + """
      </div>
    </section>
    <section class="a11y__grp" aria-labelledby="a11yG2">
      <h3 id="a11yG2">Color Modules</h3>
      <div class="a11y__grid">
        """ + a11y_tile('c-light', 'Light Contrast', 'sun')
            + a11y_tile('c-dark', 'Dark Contrast', 'moon')
            + a11y_tile('c-high', 'High Contrast', 'half')
            + a11y_tile('c-mono', 'Monochrome', 'mono') + """
      </div>
    </section>
    <section class="a11y__grp" aria-labelledby="a11yG3">
      <h3 id="a11yG3">Orientation Modules</h3>
      <div class="a11y__grid">
        """ + a11y_tile('line', 'Reading Line', 'rline')
            + a11y_tile('mask', 'Reading Mask', 'rmask')
            + a11y_tile('noimg', 'Hide Images', 'noimg')
            + a11y_tile('spot', 'Highlight Content', 'spot')
            + a11y_tile('motion', 'Stop Animations', 'stop')
            + a11y_tile('links', 'Highlight Links', 'link') + """
      </div>
    </section>
    <p class="a11y__note">Your choices are stored on this device only. Need the menu read to you,
      in large print, or in any other form? Call <a href="{ph}">{pht}</a>. Our
      <a href="accessibility.html">accessibility statement</a> says how to tell us about
      anything here that got in your way.</p>
    <button class="a11y__reset" type="button" data-a11y-reset>Reset Settings</button>
  </div>
</div>
</aside>
<script>
(function(){
  var H = document.documentElement, KEY = 'cq_a11y_v1';
  var fab = document.getElementById('a11yFab'), panel = document.getElementById('a11yPanel');
  if (!fab || !panel) return;
  var root = fab.parentNode;

  // Stepper scales. Index 1 is the untouched page in both, so "Default" is always
  // one press away and a visitor can never strand themselves at an unreadable size.
  var FS = [{s:'0.88',n:'Smaller'},{s:'1',n:'Default'},{s:'1.15',n:'Large'},
            {s:'1.3',n:'Larger'},{s:'1.5',n:'X-Large'},{s:'1.75',n:'XX-Large'}];
  var LH = [{v:'1.25',n:'Tight'},{v:'',n:'Default'},{v:'1.9',n:'Relaxed'},
            {v:'2.3',n:'Loose'},{v:'2.8',n:'Very Loose'}];
  var LS = [{n:'Default'},{v:'.06em',w:'.16em',n:'Wide'},
            {v:'.12em',w:'.26em',n:'Wider'},{v:'.2em',w:'.4em',n:'Widest'}];
  var AL = [{n:'Default'},{v:'left',n:'Left'},{v:'center',n:'Center'},{v:'right',n:'Right'}];
  var DEF = {fs:1, lh:1, ls:0, align:0, weight:0, readable:0, cursor:0,
             color:'', line:0, mask:0, noimg:0, spot:0, motion:0, links:0};
  var S = {};

  function load(){
    for (var k in DEF) S[k] = DEF[k];
    try {
      var raw = localStorage.getItem(KEY);
      if (!raw) return;
      var o = JSON.parse(raw);
      for (var k2 in DEF) if (o && o[k2] !== undefined) S[k2] = o[k2];
    } catch (e) {}
  }
  function save(){ try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }

  function flag(attr, on){ if (on) H.setAttribute(attr,''); else H.removeAttribute(attr); }

  // ---- reading aids are drawn inside this landmark, never loose on <body> ----
  function overlay(cls){
    var d = document.createElement('div');
    d.className = cls + ' a11y-ui';
    d.setAttribute('aria-hidden','true');
    root.appendChild(d);
    return d;
  }
  var rule = overlay('a11y-rule'), mTop = overlay('a11y-mask'), mBot = overlay('a11y-mask');
  var spotted = null;

  function clearSpot(){
    if (spotted) { spotted.classList.remove('a11y-spot'); spotted = null; }
  }
  function onMove(e){
    var y = e.clientY;
    if (S.line) rule.style.top = (y - 2) + 'px';
    if (S.mask) {
      mTop.style.top = '0px';
      mTop.style.height = Math.max(0, y - 62) + 'px';
      mBot.style.top = (y + 62) + 'px';
      mBot.style.bottom = '0px';
    }
    if (S.spot) {
      var el = document.elementFromPoint(e.clientX, y);
      el = el && el.closest ? el.closest('p,h1,h2,h3,h4,h5,h6,li,figcaption,blockquote') : null;
      if (el && el.closest('.a11y-ui')) el = null;
      if (el !== spotted) { clearSpot(); spotted = el; if (el) el.classList.add('a11y-spot'); }
    }
  }
  document.addEventListener('mousemove', onMove, {passive:true});

  function apply(){
    H.style.setProperty('--a11y-fs', FS[S.fs].s);

    var lh = LH[S.lh];
    flag('data-a11y-lh', !!lh.v);
    if (lh.v) H.style.setProperty('--a11y-lh', lh.v);

    var ls = LS[S.ls];
    flag('data-a11y-ls', !!ls.v);
    if (ls.v) { H.style.setProperty('--a11y-ls', ls.v); H.style.setProperty('--a11y-ws', ls.w); }

    var al = AL[S.align];
    flag('data-a11y-align', !!al.v);
    if (al.v) H.style.setProperty('--a11y-align', al.v);

    flag('data-a11y-weight',   S.weight);
    flag('data-a11y-readable', S.readable);
    flag('data-a11y-cursor',   S.cursor);
    flag('data-a11y-noimg',    S.noimg);
    flag('data-a11y-links',    S.links);
    flag('data-a11y-stopmotion', S.motion);

    if (S.color) H.setAttribute('data-a11y-color', S.color);
    else H.removeAttribute('data-a11y-color');

    rule.style.display = S.line ? 'block' : 'none';
    mTop.style.display = mBot.style.display = S.mask ? 'block' : 'none';
    if (!S.spot) clearSpot();

    sync();
  }

  function setLab(btn, base, extra){
    var lab = btn.querySelector('.a11y__lab');
    lab.textContent = extra ? base + ': ' + extra : base;
  }
  function tile(key){ return panel.querySelector('[data-a11y-t="' + key + '"]'); }
  function press(key, on){ var b = tile(key); if (b) b.setAttribute('aria-pressed', on ? 'true' : 'false'); }

  function sync(){
    document.getElementById('a11y-fs-v').value = FS[S.fs].n;
    document.getElementById('a11y-lh-v').value = LH[S.lh].n;

    press('readable', S.readable); press('cursor', S.cursor);
    press('weight', S.weight);     press('noimg', S.noimg);
    press('line', S.line);         press('mask', S.mask);
    press('spot', S.spot);         press('motion', S.motion);
    press('links', S.links);
    press('c-light', S.color === 'light');
    press('c-dark',  S.color === 'dark');
    press('c-high',  S.color === 'high');
    press('c-mono',  S.color === 'mono');

    press('ls', S.ls > 0);
    setLab(tile('ls'), 'Letter Spacing', S.ls > 0 ? LS[S.ls].n : '');
    press('align', S.align > 0);
    setLab(tile('align'), 'Align Text', S.align > 0 ? AL[S.align].n : '');
  }

  // ---- controls ----
  panel.addEventListener('click', function(e){
    var b = e.target.closest ? e.target.closest('button') : null;
    if (!b || !panel.contains(b)) return;

    if (b.hasAttribute('data-a11y-close')) { closePanel(); return; }

    if (b.hasAttribute('data-a11y-reset')) {
      for (var k in DEF) S[k] = DEF[k];
      clearSpot(); apply(); save();
      return;
    }

    var st = b.getAttribute('data-a11y-s');
    if (st) {
      var dir = parseInt(b.getAttribute('data-dir'), 10);
      var max = (st === 'fs' ? FS : LH).length - 1;
      S[st] = Math.min(max, Math.max(0, S[st] + dir));
      apply(); save();
      return;
    }

    var t = b.getAttribute('data-a11y-t');
    if (!t) return;
    if (t === 'ls')         S.ls    = (S.ls + 1) % LS.length;
    else if (t === 'align') S.align = (S.align + 1) % AL.length;
    else if (t.indexOf('c-') === 0) {
      var mode = t.slice(2);
      S.color = (S.color === mode) ? '' : mode;   // the three colour modes are exclusive
    } else {
      S[t] = S[t] ? 0 : 1;
    }
    apply(); save();
  });

  // ---- open / close ----
  function openPanel(){
    panel.hidden = false;
    fab.setAttribute('aria-expanded','true');
    fab.style.display = 'none';          // the panel sits over the launcher
    // preventScroll matters: without it the browser scrolls .a11y__body to "reveal"
    // a button that is in the header, and the panel opens halfway down the list.
    panel.querySelector('.a11y__x').focus({preventScroll:true});
    panel.querySelector('.a11y__body').scrollTop = 0;
  }
  function closePanel(){
    panel.hidden = true;
    fab.setAttribute('aria-expanded','false');
    fab.style.display = '';
    fab.focus();
  }
  fab.addEventListener('click', openPanel);
  document.addEventListener('keydown', function(e){
    if ((e.key === 'Escape' || e.key === 'Esc') && !panel.hidden) closePanel();
  });

  load();
  apply();
})();
</script>""")

A11Y = A11Y.replace('{ph}', PHONE_H).replace('{pht}', PHONE_T)


FOOT = (FOOT_HTML.format(ph=PHONE_H, pht=PHONE_T, a1=ADDR1, a2=ADDR2, maps=MAPS,
                         maps_pl=MAPS_PL, yelp=YELP, board=BOARD, opened=OPENED,
                         phi=ico('phone'), dir=ico('dir'), mn=ico('menu'),
                         sti=ico('star'), pini=ico('pin'), wm=wordmark(), flag=flag())
        + CONTROLS_HTML.format(ph=PHONE_H, pht=PHONE_T,
                               cki=ico('cookie'), a11yi=ico('a11y'),
                               xi=ico('x'), shi=ico('shield'))
        + '<script>\n' + FOOT_JS + A11Y_JS + '</script>')


FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Alfa+Slab+One&family=Yellowtail&family=Barlow+Condensed:wght@500;600;700'
         '&family=Karla:wght@400;500;700&display=swap">')

BOOT = ("<script>(function(){try{"
        # Applies the saved toolbar settings before first paint, so a visitor who chose
        # large text or high contrast never sees a flash of the default page. The scales
        # here must stay in step with FS/LH/LS/AL in the panel's own script below.
        "var R=document.documentElement,s=JSON.parse(localStorage.getItem('cq_a11y_v1')||'{}');"
        "var FS=['0.88','1','1.15','1.3','1.5','1.75'],LH=['1.25','','1.9','2.3','2.8'],"
        "LS=['','.06em','.12em','.2em'],WS=['','.16em','.26em','.4em'],"
        "AL=['','left','center','right'];"
        "if(s.fs&&FS[s.fs])R.style.setProperty('--a11y-fs',FS[s.fs]);"
        "if(s.lh&&LH[s.lh]){R.setAttribute('data-a11y-lh','');"
        "R.style.setProperty('--a11y-lh',LH[s.lh]);}"
        "if(s.ls&&LS[s.ls]){R.setAttribute('data-a11y-ls','');"
        "R.style.setProperty('--a11y-ls',LS[s.ls]);R.style.setProperty('--a11y-ws',WS[s.ls]);}"
        "if(s.align&&AL[s.align]){R.setAttribute('data-a11y-align','');"
        "R.style.setProperty('--a11y-align',AL[s.align]);}"
        "if(s.weight)R.setAttribute('data-a11y-weight','');"
        "if(s.readable)R.setAttribute('data-a11y-readable','');"
        "if(s.cursor)R.setAttribute('data-a11y-cursor','');"
        "if(s.noimg)R.setAttribute('data-a11y-noimg','');"
        "if(s.links)R.setAttribute('data-a11y-links','');"
        "if(s.motion)R.setAttribute('data-a11y-stopmotion','');"
        "if(s.color)R.setAttribute('data-a11y-color',s.color);"
        "}catch(e){}})();</script>")

def build(key, title, desc, body, standalone):
    inner = ('<title>%s</title>\n%s\n<style>\n%s</style>\n%s\n%s\n<main id="main">\n%s\n</main>\n%s\n%s\n'
             % (title, FONTS, CSS, BOOT, head(key), body, FOOT, A11Y))
    if not standalone:
        return inner
    hp, bp = inner.split('</style>\n', 1)
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            '<meta name="description" content="%s">\n'
            '<style>:root{padding-top:env(safe-area-inset-top,0px);'
            'padding-bottom:env(safe-area-inset-bottom,0px);color-scheme:light}'
            'html{-webkit-text-size-adjust:100%%}[hidden]{display:none!important}</style>\n'
            % html.escape(desc, quote=True)) + hp + '</style>\n</head>\n<body>\n' + bp + '</body>\n</html>\n'

def phead(eyebrow, h1, lede):
    return ('<section class="phead"><div class="wrap phead__in"><p class="eyebrow">%s</p>'
            '<h1>%s</h1><p class="lede">%s</p></div></section>' % (eyebrow, h1, lede))

def hours_dl(mark_today=True):
    rows = ''
    for i, (day, o, c) in enumerate(HOURS):
        js_day = (i + 1) % 7            # Mon..Sun -> JS day indices, Sun=0
        val = '%s &ndash; %s' % (o, c) if c else '<i>%s</i>' % o
        rows += ('<div class="hours__row"%s><dt>%s</dt><dd>%s</dd></div>'
                 % (' data-day="%d"' % js_day if mark_today else '', day, val))
    return '<dl class="hours">%s</dl>' % rows


def grate(dark=False):
    stars = '&#9733;' * 5
    return ('<a class="grate%s" href="%s" target="_blank" rel="noopener"'
            ' aria-label="Rated %s out of 5 on Google from %s reviews. Opens the Google listing.">'
            '<span class="grate__num">%s</span>'
            '<span class="stars" aria-hidden="true"><span class="stars__bg">%s</span>'
            '<span class="stars__fg" style="--pct:%s">%s</span></span>'
            '<span class="grate__n"><b>%s Google reviews</b>Read them &nearr;</span></a>'
            % (' grate--dark' if dark else '', MAPS_PL, G_RATING, G_COUNT, G_RATING,
               stars, G_PCT, stars, G_COUNT))

# (image, dish, blurb, sizes, menu anchor, section name)
# Ordered so no two neighbours come from the same menu section — a visitor paging
# through sees the breadth of the menu rather than three stew plates in a row.
DISHES = [
 ("img/Jerk-Chicken.jpg", "Jerk Chicken",
  "Pimento, scallion and scotch bonnet, grilled dark. Rice and a side.",
  "Medium or Large", "menu.html#specialties", "Jamaican Specialties"),
 ("img/Catch-of-the-Day.jpg", "Catch of the Day",
  "Brown stew, steamed or escovitch &mdash; whole fish, cooked to order.",
  "Call ahead to order", "menu.html#fish", "Catch of the Day"),
 ("img/Oxtails.jpg", "Oxtails",
  "Slow-cooked until it gives way, in the gravy it made.",
  "Express, Medium or Large", "menu.html#specialties", "Jamaican Specialties"),
 ("img/Cool-Tropics.jpg", "Cool Tropics",
  "Soursop, mango, pineapple ginger, passion fruit &mdash; cold out of the cooler.",
  "Five flavours", "menu.html#tropics", "Cool Tropics"),
 ("img/Curry-Chicken.jpg", "Curry Chicken",
  "Jamaican curry over chicken. The weekday regular.",
  "Express, Medium or Large", "menu.html#specialties", "Jamaican Specialties"),
]

def dish_card(src, name, desc, sizes, href, section):
    """A dish photo that links to its own line on the menu."""
    return ("""<a class="dish" href="%s">
  <img src="%s" alt="%s at Caribbean Queen" loading="lazy">
  <div class="dish__b"><h3>%s</h3><p>%s</p><p class="dish__price">%s</p>
    <p class="dish__go">See it on the menu &rarr; %s</p></div>
</a>""" % (href, src, name, name, desc, sizes, section))


def photo_carousel(items):
    slides = ''.join(
        '<div class="pcar__slide" role="group" aria-roledescription="slide" aria-label="%d of %d">%s</div>'
        % (i + 1, len(items), dish_card(*it)) for i, it in enumerate(items))
    dots = ''.join(
        '<button class="pcar__dot" type="button" role="tab" data-dot="%d" aria-selected="%s" '
        'aria-label="Dish %d of %d"></button>' % (i, 'true' if i == 0 else 'false', i + 1, len(items))
        for i in range(len(items)))
    return """<div class="pcar" data-pcar>
  <div class="pcar__vp" data-vp tabindex="0" role="group" aria-roledescription="carousel"
       aria-label="Dishes from the menu" aria-live="polite">
    <div class="pcar__track" data-track>%s</div>
  </div>
  <div class="pcar__ctl">
    <button class="pcar__btn" type="button" data-prev aria-label="Previous dish">%s</button>
    <div class="pcar__dots" role="tablist" aria-label="Choose a dish" data-dots>%s</div>
    <span class="pcar__count" data-count></span>
    <button class="pcar__btn" type="button" data-next aria-label="Next dish">%s</button>
  </div>
</div>""" % (slides, ico('prev'), dots, ico('next'))


# ---------------------------------------------------------------- menu render
def size_block(sizes):
    """Which sizes a dish comes in. Prices are the owner\'s to supply."""
    if not sizes:
        return ''
    return ('<p class="item__p">%s</p>'
            % ''.join('<i>%s</i>' % part.strip() for part in sizes.split('&middot;')))

def menu_html():
    jump = ''.join('<a href="#%s">%s</a>' % (slug, name)
                   for slug, name, _c, _b, _t, _i in MENU)
    out = ['<nav class="menujump" aria-label="Jump to a menu section">%s</nav>' % jump,
           '<p class="legend">'
           '<span><b>Plates come three ways</b> &mdash; Express, Medium or Large. '
           'Express is the quick plate; Large is the one you take home leftovers from.</span>'
           '<span>&#9733; <b>Most ordered</b>, according to their Google listing.</span>'
           '<span><b>Catch of the Day needs a call ahead</b> &mdash; the fish is cooked '
           'to order.</span>'
           '<span><b>Prices are not listed here yet.</b> Call the kitchen on '
           '<a href="%s">%s</a> and they will tell you.</span></p>' % (PHONE_H, PHONE_T)]
    for slug, name, color, blurb, tag, items in MENU:
        rows = ''
        for iname, idesc, sizes, star, note in items:
            rows += '<div class="item"><p class="item__n">%s%s</p>%s%s%s</div>' % (
                iname,
                ' <span class="item__star" title="One of the most ordered dishes">'
                '&#9733;</span>' if star else '',
                size_block(sizes),
                '<p class="item__d">%s</p>' % idesc if idesc else '',
                '<p class="item__note">%s</p>' % note if note else '')
        out.append("""<section class="mcat" id="%s" style="--cat:%s">
  <div class="mcat__h"><h2>%s</h2>%s%s</div>
  <div class="mcat__body">%s</div>
</section>""" % (slug, CAT_COLOR[color], name,
                 '<span class="mcat__tag">%s</span>' % tag if tag else '',
                 '<span>%s</span>' % blurb if blurb else '', rows))
    return '\n'.join(out)

# ================================================================ HOME
home = """<section class="hero"><div class="wrap hero__in">
  <div class="hero__body">
    <p class="hero__badge">Gainesville, Florida &nbsp;&middot;&nbsp; Northwest Fifth Avenue</p>
    <h1>Jamaica, cooked by <em>the Queen.</em></h1>
    <p class="script">Authentic Jamaican flavors, made with love</p>
    <p class="lede">Oxtail, curry goat and jerk chicken out of a small kitchen on Fifth Avenue,
      seasoned with herbs and spices carried back from home. Open since {opened} &mdash; and
      every plate comes in three sizes, so you order what you can finish.</p>
    <div class="hero__act">
      <a class="btn btn--gold btn--lg" href="{ph}">{phi} {pht}</a>
      <a class="btn btn--onchar btn--lg" href="menu.html">See the Menu</a>
      <a class="btn btn--onchar btn--lg" href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
    </div>
    {grate_dark}
  </div>
  <figure class="hero__fig">
    <img src="img/Jerk-Chicken.jpg" alt="A jerk chicken plate with rice, cabbage and fried plantain at Caribbean Queen"
         width="480" height="640" fetchpriority="high">
    <figcaption class="hero__tag">Jerk chicken, rice, plantain</figcaption>
  </figure>
</div></section>

<section class="strip"><div class="wrap strip__in">
  <span>Open <b>Mon&ndash;Thu 10:30am&ndash;6:30pm</b></span>
  <span>Fri &amp; Sun <b>10:30am&ndash;5pm</b></span>
  <span><b>Closed Saturdays</b></span>
  <span>Plates in <b>three sizes</b></span>
  <span>Dine in &amp; <b>takeout</b></span>
</div></section>

<section class="sec"><div class="wrap">
  <div class="sechead sechead--row">
    <div class="sechead" style="margin:0">
      <p class="eyebrow">What to order</p>
      <h2>Off the menu card</h2>
      <hr class="rule">
      <p class="lede" style="font-size:1.08rem">Tap any dish to jump straight to it on the menu.</p>
    </div>
    <a class="btn btn--ghost" href="menu.html">Full menu &rarr;</a>
  </div>
  {carousel}
</div></section>

<section class="sec" id="sizes"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <p class="eyebrow">Express, Medium, Large</p>
      <h2>Order the size you actually want</h2>
      <hr class="rule">
      <div class="prose">
        <p>Nearly every plate on the menu comes three ways. It is the reason nobody has to
          buy a dinner portion to taste the curry goat, and the reason a quick lunch and a
          proper sit-down come out of the same kitchen.</p>
      </div>
      <div class="hero__act" style="padding:0">
        <a class="btn btn--red" href="menu.html#specialties">See the plates</a>
      </div>
    </div>
    <div class="info">
      <div class="field"><span class="field__k">Express</span>
        <span class="field__v field__v--big">The quick plate</span>
        <span class="field__v" style="color:var(--muted)">Lunch, in and out.</span></div>
      <div class="field"><span class="field__k">Medium</span>
        <span class="field__v field__v--big">The usual order</span>
        <span class="field__v" style="color:var(--muted)">What most people take.</span></div>
      <div class="field"><span class="field__k">Large</span>
        <span class="field__v field__v--big">Enough to share</span>
        <span class="field__v" style="color:var(--muted)">Or to put in the fridge.</span></div>
    </div>
  </div>
</div></section>

<section class="sec sec--surface" id="kitchen"><div class="wrap">
  <div class="sechead">
    <p class="eyebrow">In this kitchen</p>
    <h2>Two people, one stove, no shortcuts</h2>
    <hr class="rule">
    <p class="lede">Caribbean Queen is cooked by the couple who own it. Nothing arrives
      ready to reheat, which is also why the fish needs a phone call.</p>
  </div>
  <div class="grid grid--2">
    <article class="dish"><div class="dish__b">
      <h3>Spices brought from Jamaica</h3>
      <p>The herbs and spices are not ordered from a supplier. They come back from Jamaica with
        Ms. Queen &mdash; and as she puts it, <strong>&ldquo;the spices is what makes it what
        it is.&rdquo;</strong></p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>Stews that take all morning</h3>
      <p>Oxtail, curry goat, beef stew and brown stew are cooked down until the meat gives way.
        That is a <strong>morning&rsquo;s work before the door opens</strong>, and it is why the
        oxtail goes first.</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>A real vegetarian section</h3>
      <p>Jerk tofu, curry tofu, brown stew tofu and <strong>ital pasta</strong> &mdash; the same
        seasoning and the same pots, not one substitution tacked onto the end of the menu.</p>
      </div></article>
    <article class="dish"><div class="dish__b">
      <h3>Fish cooked to order</h3>
      <p>Brown stew, steamed or escovitch, done when you ask for it rather than held under a
        lamp. <strong>Call ahead</strong> and it will be ready when you arrive.</p></div></article>
  </div>
</div></section>

<section class="sec sec--char"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <p class="eyebrow">Ms. Queen</p>
      <h2>Gainesville&rsquo;s first Jamaican kitchen</h2>
      <hr class="rule">
      <div class="prose">
        <p>Valerie Phillips grew up in Clarendon, left Jamaica at eighteen, and had been cooking
          since elementary school. When she looked at the restaurants doing well around her, the
          question she asked was simply <strong>&ldquo;Why not Jamaican?&rdquo;</strong></p>
        <p>She opened Caribbean Queen in {opened}, the first Jamaican restaurant in town. Regulars
          called her Ms. Queen, and the name stuck to the building. She and her husband Errol
          still cook everything that leaves the kitchen.</p>
      </div>
      <a class="btn btn--gold" href="about.html">Our story</a>
    </div>
    <div class="grid" style="gap:1rem">
      <div class="info" style="background:var(--char-2);border-color:var(--char-line)">
        <div class="field"><span class="field__k" style="color:var(--char-muted)">Since</span>
          <span class="field__v" style="color:var(--char-ink)">{opened} &mdash; more than twenty-five
            years on the same street.</span></div>
        <div class="field"><span class="field__k" style="color:var(--char-muted)">Best known for</span>
          <span class="field__v" style="color:var(--char-ink)">Oxtails, curry goat, curry chicken
            and jerk chicken.</span></div>
        <div class="field"><span class="field__k" style="color:var(--char-muted)">Where</span>
          <span class="field__v" style="color:var(--char-ink)">507 NW 5th Ave, a block off
            Main Street in northwest Gainesville.</span></div>
      </div>
    </div>
  </div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <p class="eyebrow">Find us</p>
      <h2>507 NW 5th Avenue</h2>
      <hr class="rule">
      <div class="info" style="width:100%">
        <div class="field"><span class="field__k">Address</span>
          <span class="field__v">{a1}<br>{a2}</span></div>
        <div class="field"><span class="field__k">Call the kitchen</span>
          <span class="field__v field__v--big"><a href="{ph}">{pht}</a></span></div>
        <div class="field"><span class="field__k">Hours</span>{hours}</div>
        <div class="copyrow">
          <a class="btn btn--red" href="{maps}" target="_blank" rel="noopener">{dir} Get Directions</a>
          <a class="btn btn--ghost" href="visit.html">Visit page</a>
        </div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1rem">
      <a class="maplink" href="{maps}" target="_blank" rel="noopener">
        <b>507 NW 5th Ave</b>
        <span>Open in Google Maps &nearr;</span>
      </a>
      {grate}
      <div class="copyrow">
        <a class="btn btn--ghost btn--sm" href="{board}">{pdfi} The printed menu</a>
        <a class="btn btn--ghost btn--sm" href="{yelp}" target="_blank" rel="noopener">{sti} Yelp</a>
      </div>
    </div>
  </div>
</div></section>""".format(ph=PHONE_H, pht=PHONE_T, a1=ADDR1, a2=ADDR2, maps=MAPS, yelp=YELP,
                           board=BOARD, opened=OPENED, phi=ico('phone'), dir=ico('dir'),
                           pdfi=ico('pdf'), sti=ico('star'), hours=hours_dl(),
                           carousel=photo_carousel(DISHES),
                           grate=grate(), grate_dark=grate(dark=True))

# ================================================================ MENU
menu = phead("The full menu",
    "Everything on the card",
    "Oxtail, curry goat, jerk chicken, fish cooked to order, a vegetarian section and "
    "Jamaican sodas. Call and we&rsquo;ll have it boxed.") + """
<section class="sec"><div class="wrap">
  <div class="copyrow" style="padding-bottom:1.3rem">
    <a class="btn btn--red btn--lg" href="{ph}">{phi} {pht}</a>
    <a class="btn btn--ghost" href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
    <a class="btn btn--ghost" href="{board}">{pdfi} The printed menu (photo)</a>
  </div>
  {menu}
</div></section>

<section class="sec sec--surface"><div class="wrap">
  <div class="sechead"><p class="eyebrow">Seen on the menu</p><h2>A few of them, plated</h2><hr class="rule"></div>
  <div class="grid grid--3">{dishes}</div>
</div></section>""".format(ph=PHONE_H, pht=PHONE_T, maps=MAPS, board=BOARD, phi=ico('phone'),
                           dir=ico('dir'), pdfi=ico('pdf'), menu=menu_html(),
                           dishes=''.join(dish_card(*d) for d in DISHES[1:4]))

# ================================================================ ABOUT
about = phead("Our story", "Ms. Queen&rsquo;s kitchen",
    "How the first Jamaican restaurant in Gainesville ended up on Northwest Fifth Avenue, "
    "and stayed there.") + """
<section class="sec"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <h2>&ldquo;Why not Jamaican?&rdquo;</h2>
      <hr class="rule">
      <div class="prose">
        <p>Valerie Phillips was born in Kingston and raised in Clarendon. She left Jamaica at
          eighteen and spent years working in the medical field, but she had been cooking since
          elementary school and never really stopped.</p>
        <p>Watching other restaurants in Gainesville do well, she asked herself the obvious
          question &mdash; <strong>&ldquo;Why not Jamaican?&rdquo;</strong> &mdash; and in {opened}
          she opened Caribbean Queen, the first Jamaican restaurant in the city. Customers took to
          calling her <strong>Ms. Queen</strong>, and that is how most of Gainesville knows her
          now. She and her husband Errol own the place and cook every dish in it.</p>
        <p>The cooking is the cooking she grew up with. Oxtail and curry goat stewed down until
          they give way. Jerk chicken marinated and grilled dark. Brown stew, escovitch, callaloo,
          rice and peas, fried plantain. Nothing reinvented and nothing fused.</p>
        <p>The one thing she will not compromise on is seasoning. The herbs and spices are not
          bought from a local supplier &mdash; she goes home to Jamaica and brings them back.
          <strong>&ldquo;The spices is what makes it what it is.&rdquo;</strong></p>
        <p>The room is small, there is reggae on, and she is as likely to give you the recipe as
          not. More than twenty-five years in, that is still how it works.</p>
      </div>
      <div class="hero__act" style="padding:0">
        <a class="btn btn--red" href="menu.html">See the full menu</a>
        <a class="btn btn--ghost" href="visit.html">Hours &amp; directions</a>
      </div>
    </div>
    <figure class="split__fig">
      <img src="img/Rice-and-Peas-Plate.jpg" alt="A curry plate with rice and peas and fried plantain at Caribbean Queen"
           width="480" height="640">
      <figcaption>Curry, rice and peas, plantain</figcaption>
    </figure>
  </div>
</div></section>

<section class="sec sec--surface"><div class="wrap">
  <div class="sechead"><p class="eyebrow">What that looks like</p><h2>Straight off the menu</h2><hr class="rule"></div>
  <div class="grid grid--3">{dishes}</div>
</div></section>

<section class="sec"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <p class="eyebrow">Where we are</p>
      <h2>A block off Main Street</h2>
      <hr class="rule">
      <div class="prose">
        <p>507 Northwest Fifth Avenue is a few minutes from downtown Gainesville and an easy
          detour off Main Street. It is a small room with a counter, which is part of the point:
          whoever hands you the plate is the person who cooked it.</p>
        <p>Saturday is the day off. Everything else, the kitchen opens at 10:30 in the morning.</p>
      </div>
      <a class="btn btn--red" href="visit.html">Hours &amp; directions</a>
    </div>
    {grate}
  </div>
</div></section>""".format(opened=OPENED,
                           dishes=''.join(dish_card(*d) for d in [DISHES[0], DISHES[2], DISHES[4]]),
                           grate=grate())

# ================================================================ CATERING
catering = phead("Catering &amp; big orders", "Feeding a crowd",
    "Trays of oxtail, curry chicken, jerk chicken and rice &amp; peas for a party, "
    "an office or a family gathering. It starts with a phone call.") + """
<section class="sec"><div class="wrap">
  <div class="split">
    <div class="split__body">
      <h2>Tell us the headcount and the day</h2>
      <hr class="rule">
      <div class="prose">
        <p>This is a small kitchen cooking everything from scratch, so a large order is not
          something to spring on us at noon. Call, say how many people and what day, and we will
          tell you straight away what we can do and what it will cost.</p>
        <p>The dishes that scale best are the ones that already cook in a pot &mdash; oxtail,
          curry goat, curry chicken, beef stew, brown stew &mdash; alongside rice and peas,
          seasoned rice, sauteed vegetables and fried plantain. The vegetarian dishes scale just
          as easily, which tends to matter for a mixed room.</p>
        <p><strong>Fish needs the most notice.</strong> Brown stew, steamed and escovitch are all
          cooked to order, even for one plate, so give us as much warning as you can.</p>
      </div>
      <div class="hero__act" style="padding:0">
        <a class="btn btn--red btn--lg" href="{ph}">{phi} {pht}</a>
        <a class="btn btn--ghost btn--lg" href="menu.html">See the menu</a>
      </div>
    </div>
    <div class="info">
      <div class="field"><span class="field__k">Call the kitchen</span>
        <span class="field__v field__v--big"><a href="{ph}">{pht}</a></span>
        <span class="copyrow" style="padding-top:.3rem">
          <button class="copybtn" type="button" data-copy="{pht}">Copy number</button></span></div>
      <div class="field"><span class="field__k">Best time to ring</span>
        <span class="field__v">During opening hours &mdash; 10:30am to 6:30pm Monday to Thursday,
          10:30am to 5pm Friday and Sunday. Closed Saturdays.</span></div>
      <div class="field"><span class="field__k">Notice</span>
        <span class="field__v">As much as you can give. The stews take a morning, and the oxtail
          is the first thing to run out on a normal day.</span></div>
      <div class="field"><span class="field__k">Pickup</span>
        <span class="field__v">{a1}, {a2}
          <span class="copyrow" style="padding-top:.35rem">
            <button class="copybtn" type="button" data-copy="{a1}, {a2}">Copy address</button>
            <a class="btn btn--red btn--sm" href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
          </span></span></div>
    </div>
  </div>
</div></section>

<section class="sec sec--surface"><div class="wrap">
  <div class="sechead"><p class="eyebrow">Travels well</p><h2>What to put on the table</h2><hr class="rule"></div>
  <div class="grid grid--3">
    <article class="dish"><div class="dish__b">
      <h3>Oxtails &#9733;</h3>
      <p>The dish people ask for by name. Slow-cooked in its own gravy, and it holds heat well
        in a tray.</p>
      <p class="dish__price">Express, Medium or Large</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>Curry Goat &#9733;</h3>
      <p>Bone-in goat in Jamaican curry. The other dish regulars plan their week around.</p>
      <p class="dish__price">Express, Medium or Large</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>Curry Chicken &#9733;</h3>
      <p>The easiest crowd-pleaser on the menu, and the simplest way to feed a lot of
        people properly.</p>
      <p class="dish__price">Express, Medium or Large</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>Jerk Chicken &#9733;</h3>
      <p>Grilled dark, cut up and trayed. Good hot, and still good an hour later.</p>
      <p class="dish__price">Medium or Large</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>The vegetarian dishes</h3>
      <p>Jerk tofu, curry tofu, brown stew tofu and ital pasta &mdash; so nobody is left with a
        side plate for dinner.</p>
      <p class="dish__price">Express, Medium or Large</p></div></article>
    <article class="dish"><div class="dish__b">
      <h3>Rice, vegetables, plantain</h3>
      <p>Pigeon peas and rice, red beans and rice, seasoned white rice, herb saut&eacute;ed
        vegetables, fried plantain.</p>
      <p class="dish__price">by the tray &mdash; call</p></div></article>
  </div>
  <p class="legend" style="margin-top:1.3rem">
    <span><b>Prices are not published on this site.</b> Nothing here is a quote &mdash; call
    <a href="{ph}">{pht}</a> and the kitchen will price the trays you need.</span></p>
</div></section>""".format(ph=PHONE_H, pht=PHONE_T, a1=ADDR1, a2=ADDR2, maps=MAPS,
                           phi=ico('phone'), dir=ico('dir'))

# ================================================================ VISIT
visit = phead("Visit", "Hours &amp; directions",
    "507 NW 5th Ave, Gainesville &mdash; a block off Main Street, a few minutes "
    "from downtown.") + """
<section class="sec"><div class="wrap">
  <div class="split">
    <div class="info" style="width:100%">
      <div class="field"><span class="field__k">Address</span>
        <span class="field__v" id="addr">{a1}, {a2}</span>
        <span class="copyrow" style="padding-top:.35rem">
          <button class="copybtn" type="button" data-copy="{a1}, {a2}">Copy address</button>
          <a class="btn btn--red btn--sm" href="{maps}" target="_blank" rel="noopener">{dir} Directions</a>
        </span></div>
      <div class="field"><span class="field__k">Phone</span>
        <span class="field__v field__v--big"><a href="{ph}">{pht}</a></span>
        <span class="copyrow" style="padding-top:.3rem">
          <button class="copybtn" type="button" data-copy="{pht}">Copy number</button></span></div>
      <div class="field"><span class="field__k">Opening hours</span>{hours}</div>
      <div class="field"><span class="field__k">Closed</span>
        <span class="field__v">Saturdays, all day.</span></div>
      <div class="field"><span class="field__k">How to order</span>
        <span class="field__v">Walk in, or call ahead and we will box it for pickup. There is no
          online ordering and no delivery app &mdash; the phone is the fastest way to us.</span></div>
      <div class="field"><span class="field__k">Fish</span>
        <span class="field__v">Brown stew, steamed and escovitch are cooked to order.
          <strong>Call ahead</strong> rather than turning up hoping.</span></div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1rem">
      <a class="maplink" href="{maps}" target="_blank" rel="noopener">
        <b>507 NW 5th Ave</b><span>Open in Google Maps &nearr;</span></a>
      <div class="prose">
        <p>We are on Northwest Fifth Avenue between 5th and 6th Street, one block north of
          Northwest 4th Avenue and a short drive from downtown Gainesville. It is a small
          building with a counter &mdash; if you have not been before, look for the flag.</p>
      </div>
      <div class="copyrow">
        <a class="btn btn--red" href="{ph}">{phi} Call to Order</a>
        <a class="btn btn--ghost" href="menu.html">See the menu</a>
      </div>
      {grate}
      <div class="copyrow">
        <a class="btn btn--ghost btn--sm" href="{board}">{pdfi} The printed menu</a>
        <a class="btn btn--ghost btn--sm" href="{yelp}" target="_blank" rel="noopener">{sti} Yelp</a>
      </div>
    </div>
  </div>
</div></section>""".format(a1=ADDR1, a2=ADDR2, ph=PHONE_H, pht=PHONE_T, maps=MAPS,
                           yelp=YELP, board=BOARD, hours=hours_dl(),
                           dir=ico('dir'), phi=ico('phone'), pdfi=ico('pdf'),
                           sti=ico('star'), grate=grate())

# ================================================================ PRIVACY & COOKIES
privacy = phead("Privacy", "Privacy &amp; cookies",
    "What this website keeps, what it does not, and how to change your mind.") + """
<section class="sec"><div class="wrap">
  <div class="legal">
    <p class="legend" style="margin-bottom:1.4rem">
      <span><b>The short version.</b> This site sets no advertising and no tracking cookies.
        It keeps two small items on your own device &mdash; the cookie choice you made and your
        accessibility settings &mdash; and nothing else. We do not sell anything about you.</span>
      <span><button class="copybtn" type="button" data-cc-open>{cki} Cookie settings</button></span>
    </p>

    <h2>Who we are</h2>
    <p>Caribbean Queen, {a1}, {a2}. Phone <a href="{ph}">{pht}</a>. We run this website and we are
      responsible for anything it stores on your device. This page covers <b>this website
      only</b> &mdash; the map and review sites we link to are run by other companies and have
      their own policies, listed further down.</p>

    <h2>What this site collects</h2>
    <p>Nothing you type. There is no account, no login, no contact form, no newsletter signup,
      no online ordering and no payment on this site. Every page is a plain page of text and
      pictures. If you want to order, call <a href="{ph}">{pht}</a>.</p>
    <p>Our host, Vercel, keeps ordinary server logs for a short period so the site can be run and
      kept secure &mdash; the page requested, the time, a browser identifier and an IP address.
      We do not use those logs to build any picture of you, and we cannot tie them to a name.</p>

    <h2>Cookies and storage</h2>
    <p>Strictly speaking, this site sets <b>no cookies at all</b>. What it uses instead is your
      browser&rsquo;s own local storage, which works the same way from your point of view and is
      covered by the same rules, so we are telling you about it plainly:</p>
    <table class="tbl">
      <caption>Everything this site stores on your device</caption>
      <thead><tr><th>Name</th><th>What it is for</th><th>How long</th></tr></thead>
      <tbody>
        <tr>
          <td data-th="Name"><code>cq.consent.v1</code></td>
          <td data-th="Purpose">Remembers the choice you made in the cookie notice, so you are not
            asked on every page. Strictly necessary.</td>
          <td data-th="How long">12 months, then we ask again</td>
        </tr>
        <tr>
          <td data-th="Name"><code>cq.a11y.v1</code></td>
          <td data-th="Purpose">Remembers your accessibility settings &mdash; text size, contrast,
            plain type, stopped animation and so on. Strictly necessary.</td>
          <td data-th="How long">Until you reset them or clear your browser</td>
        </tr>
      </tbody>
    </table>
    <p>Both stay on your device. Neither is sent to us or to anyone else, and neither contains a
      name, a phone number or an identifier that could be used to follow you anywhere.</p>

    <h3>Analytics and marketing</h3>
    <p>The cookie notice offers two optional categories, <b>Analytics</b> and
      <b>Social &amp; marketing</b>. As of the date at the foot of this page,
      <b>nothing in either category is loaded</b> &mdash; there is no Google Analytics, no
      Meta Pixel and no advertising tag on this site. The switches are there so that if we ever
      do add a visitor count or a social measurement tag, it will not run at all until you have
      allowed it. Saying no leaves the site working exactly as it does now.</p>

    <h3>Global Privacy Control and Do Not Track</h3>
    <p>If your browser or an extension sends a <b>Global Privacy Control</b> signal, or the older
      <b>Do Not Track</b> header, we treat it as a refusal of both optional categories. They stay
      switched off and cannot be turned on while that signal is set, and the notice says so.</p>

    <h3>Changing your mind</h3>
    <p>Use <b>Cookie settings</b> at the bottom of any page, or the button at the top of this one.
      You can also clear this site&rsquo;s storage in your browser&rsquo;s own settings, which
      wipes both items above; the notice will then appear again on your next visit.</p>

    <h2>Other companies we link to</h2>
    <p>When you follow one of these links, or when your browser fetches something from them, you
      are dealing with that company under its own policy. We have no access to what they collect.</p>
    <ul>
      <li><b>Google Fonts</b> &mdash; the typefaces on this site are served by Google. Your
        browser fetches them from <code>fonts.googleapis.com</code> and
        <code>fonts.gstatic.com</code>, which means Google sees the request and your IP address.
        Google sets no cookies for this and states it does not use the data for profiling.</li>
      <li><b>Google Maps</b> &mdash; only when you tap a directions, map or reviews link.</li>
      <li><b>Yelp</b> &mdash; only when you click through to our listing. We embed nothing from
        Yelp, so it cannot see you here unless you choose to go there.</li>
      <li><b>Vercel</b> &mdash; our host, as described above.</li>
    </ul>

    <h2>What we never do</h2>
    <ul>
      <li>We do not sell, rent or trade information about you &mdash; and because there is nothing
        to sell, that is not a promise we have to work at.</li>
      <li>We do not build advertising profiles or follow you to other websites.</li>
      <li>We do not send marketing email. We have no mailing list.</li>
    </ul>

    <h2>Your rights</h2>
    <p>Whichever law covers you, start by calling us on <a href="{ph}">{pht}</a>. We will answer
      within 30 days. In practice the honest answer to &ldquo;what do you hold about me?&rdquo;
      is almost always &ldquo;nothing&rdquo;, and we will say so plainly rather than pretend
      otherwise.</p>
    <ul>
      <li><b>Florida and the United States.</b> You can ask what we hold, ask for a copy, ask us
        to correct it or delete it, and ask us not to sell or share it. We do not sell or share
        personal information, and we honour Global Privacy Control as an opt-out signal.</li>
      <li><b>EU and UK visitors.</b> Our lawful basis for the two necessary storage items is your
        legitimate interest in a site that works and remembers your accessibility settings; for
        anything optional it is your consent, which you can withdraw at any time from
        <b>Cookie settings</b>. You may also complain to your data protection authority.</li>
    </ul>

    <h2>Children</h2>
    <p>This site is a restaurant menu. It is not aimed at children, and we do not knowingly
      collect anything from anyone under 13. There is nowhere on the site for anyone of any age
      to enter information.</p>

    <h2>Changes to this page</h2>
    <p>If we add anything that collects or stores more than what is listed above, we will update
      this page and the cookie notice before it goes live, and the notice will ask you again.</p>

    <p class="stamp">Last updated {today} &middot; Caribbean Queen &middot;
      Questions: <a href="{ph}">{pht}</a></p>
  </div>
</div></section>""".format(a1=ADDR1, a2=ADDR2, ph=PHONE_H, pht=PHONE_T,
                           cki=ico('cookie'), today=TODAY)

# ================================================================ ACCESSIBILITY
accessibility = phead("Accessibility", "Accessibility statement",
    "What we have done so this site works for everyone, what still falls short, "
    "and how to tell us when it does.") + """
<section class="sec"><div class="wrap">
  <div class="legal">
    <p class="legend" style="margin-bottom:1.4rem">
      <span><b>Need something now?</b> Call <a href="{ph}">{pht}</a> and we will read the menu to
        you, take your order by phone, or get you the information in whatever form suits.</span>
      <span><button class="copybtn" type="button" data-a11y-open>{a11yi} Accessibility tools</button></span>
    </p>

    <h2>Our commitment</h2>
    <p>Caribbean Queen is a restaurant, and everybody eats. We want this website to be usable by
      everyone, including people who use a screen reader, a magnifier, voice control, a keyboard
      instead of a mouse, or who need bigger text or stronger contrast. We treat accessibility as
      part of the job rather than an add-on, and we fix what gets reported.</p>

    <h2>The standard we aim at</h2>
    <p>We aim to meet <b>WCAG 2.1 Level AA</b>, the standard that US courts and the Department of
      Justice point to for the Americans with Disabilities Act. This site was built against that
      standard and checked by hand &mdash; with a keyboard, with the text enlarged, at phone
      width and in both light and dark mode &mdash; rather than by running a scan over it and
      calling it done. We consider it <b>substantially conformant</b>: the limitations we know
      about are listed below instead of being left for you to find.</p>

    <h2>What is built in</h2>
    <ul>
      <li><b>Accessibility tools on every page.</b> The round button in the corner opens a
        toolbar of eighteen display controls, grouped the way assistive toolbars usually are.
        <b>Content:</b> text size up to 175%, line height, readable font, big cursor, letter
        spacing, text alignment and font weight. <b>Colour:</b> light, dark, high-contrast and
        monochrome. <b>Orientation:</b> a reading line that follows the pointer, a reading mask
        that dims everything but the current line, hide images, highlight the block you are
        reading, stop animation, and highlight every link. One button resets the lot. Your
        choices are kept on your own device and are applied before the page paints, so nothing
        flashes back to the default.
        Your choices are remembered on your own device, with nothing sent anywhere.</li>
      <li><b>A real menu, not a picture of one.</b> Every dish on the card is live text, so a
        screen reader can read it, you can search it, and you can zoom it without it turning to
        mush.</li>
      <li><b>Keyboard throughout.</b> A &ldquo;Skip to content&rdquo; link comes first, every
        control can be reached and operated with Tab and Enter, and focus is always visible.</li>
      <li><b>Headings, landmarks and labels</b> are marked up properly, so you can jump around
        the page rather than wading through it. Every image has alternative text, and icons are
        hidden from screen readers so they are not read out as noise.</li>
      <li><b>Contrast.</b> Body text and controls are checked against the 4.5:1 ratio, and the
        high-contrast setting goes well beyond it.</li>
      <li><b>Motion.</b> The dish carousel stops as soon as you touch, hover or tab into it, obeys
        your system &ldquo;reduce motion&rdquo; setting, and can be stopped outright from the
        accessibility panel. Nothing flashes and nothing auto-plays with sound.</li>
      <li><b>Zoom and small screens.</b> The layout holds together at 200% browser zoom and down
        to a 320px-wide phone, without a horizontal scrollbar.</li>
      <li><b>No overlay.</b> We did not bolt on a third-party accessibility overlay. The panel
        here adjusts our own pages directly, so it cannot fight your screen reader or your
        browser&rsquo;s own settings.</li>
    </ul>

    <h2>Where we still fall short</h2>
    <p>Being straight about this is part of the standard, so here is the current list.</p>
    <ul>
      <li><b>The photograph of the menu card is a photograph.</b> The
        <a href="{board}">picture of our printed menu</a> kept on this site is an image, so
        a screen reader cannot read it. It is there only as a record of the card.
        <b>The accessible version is the <a href="menu.html">full menu page</a></b>, which
        carries every dish on it as live text.</li>
      <li><b>Prices are not on the site yet.</b> The menu page lists every dish and the
        sizes it comes in, but not what it costs, so you have to call to find out. We are
        putting the prices up.</li>
      <li><b>Ordering is by phone.</b> There is no online ordering to make accessible, which
        removes a whole class of problem &mdash; but it does mean that if using a phone is hard
        for you, there is no alternative route to an order yet. Tell us and we will work
        something out.</li>
      <li><b>Directions open Google Maps</b>, another site we do not control. Our
        <a href="visit.html">Visit page</a> also gives the address and hours as plain text, and
        we will give directions over the phone.</li>
      <li><b>Dish photographs</b> are described by name rather than in detail. No photograph
        carries information that is not also in the text beside it.</li>
      <li><b>Opening hours can change</b> without this page catching up immediately. If it
        matters, call first.</li>
    </ul>

    <h2>The restaurant itself</h2>
    <p>This statement is about the website. For questions about getting into and around
      {a1} &mdash; the entrance, seating, restrooms, service animals or help at the
      counter &mdash; call <a href="{ph}">{pht}</a> before you come and we will tell you exactly
      what to expect and what we can do.</p>

    <h2>Tell us when something blocks you</h2>
    <p>If any part of this site or our service is hard to use, we want to hear it &mdash; a
      specific complaint is the fastest way to a fix.</p>
    <ul>
      <li><b>Phone:</b> <a href="{ph}">{pht}</a></li>
      <li><b>In person or by post:</b> {a1}, {a2}</li>
    </ul>
    <p>We aim to reply within <b>three business days</b>, and to tell you either how it is fixed
      or when it will be. If we cannot fix something quickly, we will offer another way to get
      what you needed &mdash; usually over the phone.</p>

    <h2>How this statement was prepared</h2>
    <p>Self-assessment by the people who built the site: a manual keyboard pass, colour contrast
      checked against the 4.5:1 ratio, layout checked at 320px wide and with the text scaling
      above turned up to 150%, and a check in both light and dark mode. It has <b>not</b> been
      audited by an outside party, and it has not yet been tested end to end with a screen reader
      by someone who uses one daily &mdash; if you do, we would value hearing from you. We review
      this statement at least once a year and whenever the site changes substantially.</p>

    <p class="stamp">Last reviewed {today} &middot; Target: WCAG 2.1 Level AA &middot;
      Report a barrier: <a href="{ph}">{pht}</a></p>
  </div>
</div></section>""".format(a1=ADDR1, a2=ADDR2, ph=PHONE_H, pht=PHONE_T, board=BOARD,
                           a11yi=ico('a11y'), today=TODAY)


SITE = [
 ('index.html','index',"Caribbean Queen",
  "Caribbean Queen, 507 NW 5th Ave, Gainesville FL. Oxtail, curry goat, jerk chicken, fish "
  "cooked to order and a vegetarian menu, since 2000. Call (352) 374-8111.", None),
 ('menu.html','menu',"Caribbean Queen Menu",
  "The full Caribbean Queen menu: oxtails, curry goat, curry chicken, jerk chicken, brown stew, "
  "soups, vegetarian dishes, patties, Jamaican sodas and tropical juice.", True),
 ('about.html','about',"Ms. Queen's Kitchen",
  "The story behind Caribbean Queen: Valerie Phillips opened Gainesville's first Jamaican "
  "restaurant in 2000, and still cooks it with spices brought from home.", True),
 ('catering.html','catering',"Caribbean Queen Catering",
  "Catering and big orders from Caribbean Queen in Gainesville: oxtail, curry goat, curry "
  "chicken, jerk chicken and rice and peas by the tray. Call to plan it.", True),
 ('visit.html','visit',"Visit Caribbean Queen",
  "Hours, directions, phone and address for Caribbean Queen, 507 NW 5th Ave, Gainesville FL "
  "32601. Open Monday to Thursday 10:30am to 6:30pm. Closed Saturdays.", True),
 ('privacy.html','privacy',"Privacy & Cookies — Caribbean Queen",
  "What the Caribbean Queen website stores on your device, what it does not collect, the "
  "companies it links to, and how to change your cookie choices.", True),
 ('accessibility.html','accessibility',"Accessibility — Caribbean Queen",
  "Caribbean Queen's accessibility statement: WCAG 2.1 AA target, the accessibility tools built "
  "into every page, known limitations, and how to report a barrier.", True),
]

BODIES = {'index':home,'menu':menu,'about':about,'catering':catering,'visit':visit,
          'privacy':privacy,'accessibility':accessibility}

os.makedirs(OUT, exist_ok=True)
for fname, key, title, desc, standalone in SITE:
    if standalone is None:
        standalone = INDEX_STANDALONE
    doc = build(key, title, desc, BODIES[key], standalone)
    open(os.path.join(OUT, fname), 'w', encoding='utf-8').write(doc)
    print('%-15s %7d bytes  %s' % (fname, len(doc), 'standalone' if standalone else 'artifact-wrapped'))
