#!/usr/bin/env python3
"""Build the AMERICAN PSYCHO (APX) page — Mary Harron's 2000 film of Bret Easton
Ellis's 1991 novel, catalogued into UD0 as the second film-world. A full PRODUCTION
page: the source, the troubled development, the makers, the cast, the soundtrack.

Two layers, per ROOT0's standing brief:
  • the CARBONS — the cast as ACI .agents, each with a .shadow: the real-life analog
    (the actor — the TRON "User" behind the program).
  • the SYNTHS — the parabolic threads distilled into ACIs (synth-style): the business
    card, the morning routine, the return-videotapes alibi, the music monologues, the
    Reaganite surface, the performed self, the confession that means nothing, and the
    keystone — THE AMBIGUITY (killer or fantasist; the film refuses to resolve it).

Full ACI badge work via the shared noesis kernel:
.agent · .shadow (carbons) · .attribute · .carbon.tiff · .silicon.png · .spun · .moniker · .1099 · manifest."""
import os, re, html, base64, json, io, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "AMERICAN PSYCHO", "axiom": "APX",
 "position": "American Psycho · Lionsgate · 2000 — dir. Mary Harron, from Bret Easton Ellis's 1991 novel",
 "origin": "the chrome-and-bone surface of 1987 Wall Street — Pierce & Pierce, the Upper West Side condo, the reservations no one can get, the morning of masques and toners",
 "mechanism": "Crystallized from the 2000 film and Ellis's 1991 novel — a satire in which the most expensive surface in Manhattan is wrapped around nothing at all.",
 "crystallization": "A flawless 27-year-old investment banker narrates his descent into murder — or the fantasy of it — and confesses to everything, to no consequence whatsoever.",
 "nature": "American Psycho — the satire of consumerism and performed masculinity where a man is only his business card, his reservations, and his routine, and the void underneath may or may not be killing people.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the film (2000, dir. Mary Harron); Ellis's novel (1991); the '80s brand-and-status surface; the Huey Lewis / Genesis / Whitney monologues; John Cale's score",
 "witness": "No hero — a perfect surface, a confession that means nothing, and a door marked THIS IS NOT AN EXIT.",
 "role": "the second film-world of UD0",
 "seal": "There is an idea of a Patrick Bateman — but there is no real me, only an entity, and the confession changes nothing: this is not an exit.",
 "source": "American Psycho, catalogued by ROOT0",
}

# the shared four-nature taxonomy — APX-flavored glosses (darker)
NATURES = {
 "natural":   ("#9a9486", "flesh-and-blood Manhattan — the interchangeable colleagues, the fiancée, the detective, the people who are real and the people he barely sees as such; carbon, with a real-life User behind each"),
 "ethereal":  ("#b8a98c", "of surface and glamour — the consumerist aura, the sedated dream, the alibi, the unreal normalcy that may be all there is"),
 "spiritual": ("#8b1a1a", "of the soul and its absence — the void behind the mask, the mask itself, and the confession that buys no catharsis and no exit"),
 "electrical":("#5a6b78", "the synth nature — the brand-machine, the status-engine, taste rendered as identity; constructed, not born — the surface running with no one home"),
}

IDEAS = [
 ("The Business Card", "status anxiety, distilled to an object", [
   "The colleagues compare cards — the bone stock, the Silian Rail typeface, the tasteful thickness, the subtle off-white coloring, the watermark — and Bateman nearly faints with envy.",
   "Murder is almost beside the point: the deepest violence in the film is a man undone by a slightly better card than his own." ]),
 ("The Void Behind the Surface", "there is no real me", [
   "‘There is an idea of a Patrick Bateman — some kind of abstraction — but there is no real me. Only an entity, something illusory.’",
   "The perfect skincare routine, the perfect body, the perfect reservations: a flawless surface wrapped around an absence." ]),
 ("The Ambiguity", "killer or fantasist?", [
   "Apartments hold no bodies; an ATM tells him to feed it a stray cat; his lawyer says he had dinner with the man Bateman swears he axed — in London, last week.",
   "The film refuses to resolve whether any of it happened. The horror is that it does not matter — to anyone, including the law." ]),
 ("The Satire", "the '80s, indicted", [
   "Mary Harron — a feminist director — made it as a critique of Reagan-era consumerism and performed masculinity, not a celebration of either.",
   "The brands, the cards, the Trump-worship, the music criticism mid-atrocity: the surface is the subject, and the surface is rotten." ]),
]

ARC = [
 ("I · The Surface", "the perfect life, the perfect routine",
  "Patrick Bateman, 27, VP at Pierce & Pierce, narrates his flawless existence — the herb-mint masque, the thousand-crunch mornings, the reservations, the fiancée he doesn't love. Every surface immaculate, every person interchangeable, including himself."),
 ("II · The Unraveling", "envy, escalation, and a detective",
  "A better business card and the Fisher account drive him to murder his colleague Paul Allen to ‘Hip to Be Square.’ The killings — or the fantasies of them — escalate; a detective named Kimball circles the disappearance; the surface begins to slip."),
 ("III · This Is Not an Exit", "the confession that changes nothing",
  "Bateman confesses everything into a lawyer's voicemail and in person — and is told it's a good joke, that Paul Allen is alive in London. No arrest, no catharsis, no punishment. He stares at a sign: THIS IS NOT AN EXIT."),
]

SECTIONS = [
 ("The Source", "the novel before the film", [
   ("American Psycho — Bret Easton Ellis", "1991 · novel", "the notorious, near-unpublishable satire; Simon & Schuster dropped it, Vintage picked it up; protested and dissected in equal measure"),
   ("The controversy", "1991–2000", "boycotts, a wrapped-in-plastic sale in some markets, and a decade of argument over whether the satire reads as critique or catalogue"),
 ]),
 ("The Production", "a troubled development, a feminist's film", [
   ("Mary Harron", "director & co-writer", "took the material as a critique of '80s masculinity; fought to keep the satire and her casting"),
   ("Guinevere Turner", "co-writer", "co-wrote the screenplay with Harron; also appears as Elizabeth"),
   ("The near-misses", "1990s development", "Leonardo DiCaprio was attached; Oliver Stone nearly directed; Harron and Bale were briefly replaced, then restored"),
   ("Edward R. Pressman · Lionsgate", "producer · distributor", "the long road from novel rights to a 2000 release"),
   ("John Cale", "score", "the cold, classical score under the brand-bright surface"),
 ]),
 ("The Cast", "the surface, performed", [
   ("Christian Bale", "Patrick Bateman", "modeled the blankness partly on a too-friendly talk-show affect; a performance of a performance of a man"),
   ("Willem Dafoe · Reese Witherspoon · Jared Leto", "Kimball · Evelyn · Paul Allen", "the detective, the fiancée, and the envied colleague"),
   ("Chloë Sevigny · Samantha Mathis", "Jean · Courtney", "the secretary who is the film's one warm soul, and the sedated mistress"),
   ("Justin Theroux · Josh Lucas · Bill Sage · Matt Ross", "the colleagues", "Bryce, McDermott, Van Patten, Carruthers — interchangeable by design"),
 ]),
 ("The Soundtrack of Atrocity", "taste as identity — the music monologues", [
   ("Huey Lewis & the News — ‘Hip to Be Square’", "the Paul Allen scene", "a sincere yuppie appreciation, raincoat on, axe in hand"),
   ("Genesis — ‘Sussudio’ / Phil Collins", "the Christie scene", "‘I think Invisible Touch is the group's undisputed masterpiece’"),
   ("Whitney Houston — ‘The Greatest Love of All’", "the monologue", "learning to love yourself is the greatest love of all — narrated by a void"),
 ]),
]

# ---- ACI complement via noesis (identical idiom to the other spheres) ----
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","APX")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","APX")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","APX")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],
            "carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
            "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
            "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ---- page fragments ----
def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def arc_html():
    out=[]
    for t,s,d in ARC:
        out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    return "".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)

def _card(p):
    em=p.get("emergence","natural"); col=NATURES.get(em,("#9a9486",""))[0]
    rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"APX · American Psycho","axiom":"APX"}
    actor=p.get("actor",""); kind=p.get("kind","carbon")
    extra=(f'<span class="pa">· .shadow · {html.escape(actor)} →</span>' if kind=="carbon"
           else '<span class="pa">· synth · .agent →</span>')
    sub=(f'<div class="pact">User · <b>{html.escape(actor)}</b></div>' if actor else "")
    return f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>{sub}
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span>{extra}</div></div></a>'''

def personas_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8"))
    carb=[p for p in ps if p.get("kind","carbon")=="carbon"]
    syn=[p for p in ps if p.get("kind")=="synth"]
    out=f'''<section class="sec" id="carbons"><h2>The Carbons — the cast &amp; their Users</h2>
      <p class="ss">the cast as ACI <b>.agent</b>s — and each carries a <b>.shadow</b>: its real-life analog, the actor who is the <b>User</b> behind the program. Think TRON — every program has a User. ({len(carb)} carbons)</p>
      <div class="pgrid">{"".join(_card(p) for p in carb)}</div></section>'''
    out+=f'''<section class="sec" id="synths"><h2>The Synths — the parabolic threads</h2>
      <p class="ss">not characters but the film's <b>distilled threads</b>, each given its own ACI — the business card, the morning routine, the videotapes, the music monologues, the surface, the performed self, the non-exit, and the keystone: <b>the ambiguity</b>. Synth-style — constructed, not carbon; no single User. ({len(syn)} synths)</p>
      <div class="pgrid">{"".join(_card(p) for p in syn)}</div></section>'''
    return out

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="American Psycho (APX) — Mary Harron's 2000 film of Bret Easton Ellis's novel as a UD0 film-world: a full production page, the cast as ACI carbons with .shadow real-life Users (TRON), plus synth ACIs for the parabolic threads — the business card, the morning routine, the music monologues, and the ambiguity that never resolves.">
<title>AMERICAN PSYCHO · APX · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--paper:#e7e3d8;--paper2:#ddd8ca;--card:#f1eee6;--ink:#161410;--ink2:#3a352c;--blood:#8b1a1a;--blood2:#a8201f;--steel:#5a6b78;--gold:#9a8a5c;
--dim:#8c8675;--faint:#cbc5b4;--line:#cdc7b6;--disp:"Cormorant Garamond",Georgia,serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--body);line-height:1.62;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -10%,rgba(139,26,26,.05),transparent 55%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:56px 0 30px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:120px;height:2px;background:var(--blood)}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.34em;text-transform:uppercase;color:var(--dim);margin-bottom:18px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--blood)}
h1{font-family:var(--disp);font-size:clamp(40px,9vw,86px);font-weight:300;letter-spacing:.12em;color:var(--ink);line-height:.98;text-transform:uppercase}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.22em;color:var(--ink2);margin-top:18px;text-transform:uppercase}
.h-sub b{color:var(--blood)}
.flag{display:inline-block;margin-top:16px;font-family:var(--mono);font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--steel);border:1px solid var(--faint);background:var(--card);padding:6px 12px}
.lede{font-size:16px;color:var(--ink2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.7}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:22px;border:1px solid var(--faint);background:var(--card);max-width:700px;box-shadow:0 1px 0 #fff inset}
.badge img{width:84px;height:84px;border:1px solid var(--faint);background:var(--paper)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--ink2);line-height:1.75}
.badge .bt b{color:var(--ink)}.badge .bt .mo{color:var(--blood)}.badge .bt a{color:var(--steel);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:48px}
.sec h2{font-family:var(--disp);font-size:30px;font-weight:400;letter-spacing:.04em;color:var(--ink);padding-bottom:8px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:8px 0 18px}.ss b{color:var(--ink2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--card);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--mono);font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:.08em}
.nat-g{font-size:12px;color:var(--ink2);font-style:italic;line-height:1.45;margin-top:3px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--card);border:1px solid var(--line);padding:17px 19px}
.pillar h3{font-family:var(--disp);font-size:23px;color:var(--blood);font-weight:500;text-transform:uppercase;letter-spacing:.03em}
.pillar .ps{font-size:12px;color:var(--dim);font-style:italic;margin:4px 0 11px}
.pillar ul{list-style:none}.pillar li{font-size:13px;color:var(--ink2);line-height:1.55;padding:7px 0;border-top:1px solid var(--faint)}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:8px}
.arc-card{background:var(--card);border:1px solid var(--line);border-top:2px solid var(--blood);padding:17px 19px}
.arc-h{font-family:var(--disp);font-size:22px;color:var(--ink);font-weight:500;text-transform:uppercase}
.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:5px 0 9px}
.arc-card p{font-size:13px;color:var(--ink2);line-height:1.58}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--ink);font-weight:600}
.books .y{font-family:var(--mono);font-size:10.5px;color:var(--steel);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}
.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--ink2);font-style:italic}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--card);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--blood);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0;background:var(--paper)}
.pn{font-family:var(--disp);font-size:20px;color:var(--ink);font-weight:500;line-height:1.1;letter-spacing:.02em}
.persona:hover .pn{color:var(--blood)}
.pe{font-size:11.5px;color:var(--ink2);font-style:italic;margin-top:2px;line-height:1.3}
.pact{font-family:var(--mono);font-size:10px;color:var(--dim);margin-top:3px}.pact b{color:var(--steel)}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;flex-wrap:wrap}
.pnat .dot{width:8px;height:8px;margin-top:0}
.pa{color:var(--dim)}
.note{margin-top:40px;padding:17px 19px;border-left:2px solid var(--blood);background:var(--card);font-size:13.5px;color:var(--ink2);font-style:italic}
.note b{color:var(--ink)}
footer{margin-top:48px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}
footer a{color:var(--blood);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the second film-world</div>
    <h1>American<br>Psycho</h1>
    <div class="h-sub">a satire of the surface · <b>this is not an exit</b> · APX</div>
    <div class="flag">★ MARY HARRON · 2000 · FROM BRET EASTON ELLIS ★</div>
    <p class="lede">A flawless 27-year-old investment banker narrates his descent into murder — or the fantasy of it — across a Manhattan of business cards, reservations, and morning masques, and confesses to everything, to no consequence whatsoever. Catalogued into UD0 as the second film-world: a full production page, the cast as carbons with real-life Users (.shadow), the film's parabolic threads as synths.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of APX" title="carbon badge (archival: apx.dlw/apx.carbon.tiff)">
      <img src="__SILICON__" alt="DLW silicon badge of APX" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>APX</b> — American Psycho</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="apx.dlw/apx.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="apx.dlw/apx.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2>
    <p class="ss">each emergent comes by one of four natures — the cast lives in the first; Bateman's is the absence in the third</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">why a satire about a business card became a permanent diagnosis</p><div class="pillars">__IDEAS__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">three beats — the surface, the unraveling, and the door that is not an exit</p><div class="arc">__ARC__</div></section>

  __PERSONAS__

  <div class="note"><b>On the .shadow — the User behind the program.</b> Think TRON: every program is cast from a real-world User. Each carbon here is a program; its <b>.shadow</b> names the User — the actor who lent the face — and the real-life archetype it shadows. The <b>synths</b> have no single User: they are the film's parabolic threads distilled. The keystone synth, <b>the ambiguity</b>, is the film's refusal made a character — the question of whether any of the violence is real, which the film will not answer, because the indictment lands either way.</div>

  <section class="sec"><h2 style="margin-top:16px">The Production</h2><p class="ss">the source, the troubled road to the screen, the cast, and the soundtrack of atrocity</p></section>
  __SECTIONS__

  <div class="note">American Psycho, its characters, and its world are © Lionsgate / Bret Easton Ellis / the respective rights-holders. The personas here are catalogued personifications under the DLW standard — commentary and cataloguing of a satirical work, not original creations, and not endorsed by the rights-holders. The film is a critique of 1980s consumerism and performed masculinity; this catalogue reads it as such, and renders its victims as victims. The credit for the catalogue returns to the human governor.</div>

  <footer>
    AMERICAN PSYCHO · APX · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="apx.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "apx.dlw"), "apx")
    json.dump({"node":"APX","name":"AMERICAN PSYCHO","moniker":tok["moniker"],
               "carbon":"apx.carbon.tiff","silicon":"apx.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,
               "seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"apx.dlw","manifest.dlw.json"),"w",encoding="utf-8"),
              indent=2, ensure_ascii=False)
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ARC__", arc_html()).replace("__PERSONAS__", personas_html())
            .replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote AMERICAN PSYCHO (APX) — badge {tok['moniker']}")
