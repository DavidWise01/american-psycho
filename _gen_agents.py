#!/usr/bin/env python3
"""Materialize the AMERICAN PSYCHO (APX) ACI corpus from the roster below.

  • CARBONS — the cast. Each → full ACI complement PLUS a .shadow: the real-life
    analog (the actor = the TRON "User" behind the program).
  • SYNTHS  — the parabolic threads distilled into ACIs (synth-style; no single User),
    including the keystone: THE AMBIGUITY (killer or fantasist — never resolved).

Read as satire: the film (a feminist director's critique of '80s consumerism and
performed masculinity) is catalogued as such; its victims are rendered as victims."""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # american-psycho/build.py — write_aci, NATURES
AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

UNI = "APX · American Psycho"
NAT_GLOSS = {
 "natural":   "*natural*: flesh-and-blood Manhattan — a person, real whether or not Bateman can see them as such; a carbon with a real-life User behind the face.",
 "ethereal":  "*ethereal*: of surface and glamour — the consumerist aura, the sedated dream, the unreal normalcy that may be the whole of it.",
 "spiritual": "*spiritual*: of the soul and its absence — the void behind the mask, the mask itself, the confession that buys no catharsis and no exit.",
 "electrical":"*electrical*: the synth nature — the brand-machine, the status-engine, taste rendered as identity; a surface running with no one home.",
}

# ---------------------------------------------------------------- THE CARBONS
CARBONS = [
 dict(slug="patrick-bateman", name="Patrick Bateman", cls="VP, Pierce & Pierce · the surface with no one home",
   emergence="spiritual", actor="Christian Bale",
   analog="the man who is only his résumé, his reservations, and his reflection — the perfectible exterior wrapped around an absence, and the violence that absence may or may not be doing",
   resemblance="Bale built the blankness from a too-bright, affectless talk-show friendliness — a performance of a man performing a man; the smile that never reaches anything.",
   who="Patrick Bateman, 27, a vice-president at the investment firm Pierce & Pierce — flawless body, flawless apartment, flawless taste, and, by his own narration, a serial killer.",
   what="The narrator and void at the film's center, who tends his surface with religious discipline and describes murders that the film will never confirm happened, confessing in the end to nothing that sticks.",
   why="Because the most expensive surface in Manhattan can be wrapped around no self at all; because a culture that rewards only the surface will never look beneath it, even for a confession.",
   how="By the morning masque and the thousand crunches, the reservations and the cards — and, in his telling, an axe to Huey Lewis, a chainsaw on the stairs, and a city too distracted to notice.",
   where="The Pierce & Pierce office, the Upper West Side condo, the restaurants no one else can book, and the inside of an unreliable narration.",
   seal="There is an idea of a Patrick Bateman, some kind of abstraction — but there is no real me: only an entity, something illusory."),
 dict(slug="paul-allen", name="Paul Allen", cls="the envied colleague · the better card",
   emergence="natural", actor="Jared Leto",
   analog="the peer who has the thing you can't stop measuring yourself against — the account, the card, the table — and never even notices the war you're waging in your head",
   resemblance="Leto plays oblivious privilege exactly: a man so secure he mistakes Bateman for someone else and condescends to him without ever registering the threat.",
   who="Paul Allen, a fellow Pierce & Pierce banker who handles the coveted Fisher account, carries the tastefully superior business card, and can get the reservation at Dorsia.",
   what="The colleague whose effortless superiority Bateman cannot bear — and whom Bateman (in his narration) murders with an axe to ‘Hip to Be Square,’ then impersonates to cover the disappearance.",
   why="Because envy needs a face, and Paul Allen's is the one that has everything Bateman has performed his way toward and still feels he lacks.",
   how="By a better card, the Fisher account, and a serene inability to tell his colleagues apart — he calls Bateman ‘Marcus Halberstam’ to the end.",
   where="The bars and dinners of the set, the apartment with the raincoat and the newspaper on the floor, and the void his absence opens.",
   seal="I have the Fisher account and the better card — and I never even learned which one of you was going to kill me for it."),
 dict(slug="evelyn-williams", name="Evelyn Williams", cls="the fiancée · the social surface",
   emergence="ethereal", actor="Reese Witherspoon",
   analog="the partner who is a merger, not a marriage — invested in the appearance of the couple and serenely blind to the person she's engaged to",
   resemblance="Witherspoon's bright, brittle obliviousness is the glamour: a woman performing a relationship with a void and calling it love.",
   who="Evelyn Williams, Bateman's fiancée, a creature of the same world — engagements, brunches, the right parties — who wants the wedding far more than the man.",
   what="The social-surface partner who cannot see, or refuses to see, what Bateman is, and to whom his ‘I want to end this’ barely registers over the seating plan.",
   why="Because in this world a marriage is a status arrangement, and a partner who only sees the surface is the perfect mate for a man who is only surface.",
   how="By the rituals of the engaged — the dinners, the chocolate-covered everything, the studied not-noticing — and a will to keep the appearance intact at all costs.",
   where="The restaurants, the engagement, and the breakup she won't quite hear.",
   seal="We're engaged, we have reservations — and whatever you are underneath, I have decided not to see it."),
 dict(slug="jean", name="Jean", cls="the secretary · the one warm soul",
   emergence="natural", actor="Chloë Sevigny",
   analog="the one genuinely kind person in a glass tower — the soul whose ordinary decency is, in this world, the most fragile and endangered thing of all",
   resemblance="Sevigny plays unguarded tenderness against everyone else's lacquer; her openness is what makes the date scene unbearable and the survival a mercy.",
   who="Jean, Bateman's secretary, who has feelings for him that he does not deserve — the film's lone source of real warmth, and very nearly its next victim.",
   what="The innocent who sees a person where there is a void, comes to his apartment, and is spared — perhaps the only mercy in the film — later finding his notebook of horrors.",
   why="Because the satire needs one true heart to measure the void against; because her decency is the thing the whole world is built to chew up.",
   how="By kindness, by hope misplaced in a monster, and by the awful luck of being the one he didn't, or couldn't, kill.",
   where="The Pierce & Pierce desk, the dinner that curdles, the apartment she escapes, and the desk drawer of drawings she should never have opened.",
   seal="I saw someone worth caring about where there was no one — and I am the one he let walk out the door."),
 dict(slug="courtney-rawlinson", name="Courtney Rawlinson", cls="the mistress · sedated",
   emergence="ethereal", actor="Samantha Mathis",
   analog="the person so anaesthetized by the life that they drift through it half-asleep — present, medicated, and barely able to register where they are",
   resemblance="Mathis plays a permanent soft fog: a woman tranquillized out of her own life, which is its own quiet indictment of the world that did it.",
   who="Courtney Rawlinson, Luis Carruthers' girlfriend and Bateman's mistress, perpetually sedated on a haze of prescriptions, drifting through dinners and afternoons.",
   what="The medicated mistress who floats through the affair barely awake — a portrait of the same void from the inside, numbed rather than performing.",
   why="Because this world tranquillizes as readily as it consumes; because her fog is what the surface feels like when you stop pretending to enjoy it.",
   how="By a pharmacy of sedatives and a learned drift, present in body and absent everywhere else.",
   where="The dinners she can't quite track, the affair she half-remembers, the apartments she wakes in.",
   seal="I'm here, I think — somewhere under the prescriptions — drifting through a life I was given instead of chose."),
 dict(slug="donald-kimball", name="Donald Kimball", cls="the detective · the circling question",
   emergence="natural", actor="Willem Dafoe",
   analog="the investigator who senses the wrongness but operates in a world too slippery to convict it — the law, arriving and finding nothing to hold",
   resemblance="Dafoe plays the questions three ways at once (knowing, friendly, skeptical) — Harron shot takes in all three registers, so even the detective is ambiguous.",
   who="Donald Kimball, a private investigator hired to look into the disappearance of Paul Allen, who interviews Bateman with an unnerving, unplaceable calm.",
   what="The procedural thread who circles Bateman, almost catches the unease — and then dissolves it, reporting that Paul Allen was seen alive in London, leaving nothing to charge.",
   why="Because the film needs the law to arrive and find no purchase; because a world of interchangeable men and unverifiable stories cannot convict anyone of anything.",
   how="By interviews, alibis, and a flat affect that may be suspicion or may be nothing — even his certainty is unreadable.",
   where="The office interview, the lunch, the trail of a missing man that leads, impossibly, to London.",
   seal="Something is wrong with you, Mr. Bateman — but a man was seen alive in London last week, so there is nothing here for me to hold."),
 dict(slug="timothy-bryce", name="Timothy Bryce", cls="colleague · interchangeable by design",
   emergence="natural", actor="Justin Theroux",
   analog="the peer who is functionally identical to you — same suit, same slang, same contempt — the proof that none of you is anyone in particular",
   resemblance="Theroux plays the smooth, coked-up sameness that makes the card scene possible: men who literally cannot tell each other apart.",
   who="Timothy Bryce, one of Bateman's Pierce & Pierce colleagues — a near-copy in suspenders and slicked hair, trading restaurant tips and casual cruelties.",
   what="One of the interchangeable set whose sameness is the joke and the point: a roomful of men so identical that murder and mistaken identity become indistinguishable.",
   why="Because the satire's deepest cut is that the cast is interchangeable — they swap names and faces because there is nothing distinct under any of them.",
   how="By the uniform, the slang, the reservations, and the shared inability to see anyone as a person, including each other.",
   where="The boardroom, the bars, the dinners where everyone is mistaken for everyone else.",
   seal="We wear the same suit and trade the same card — and not one of us could pick the others out of a line-up, or would care to."),
 dict(slug="craig-mcdermott", name="Craig McDermott", cls="colleague · interchangeable by design",
   emergence="natural", actor="Josh Lucas",
   analog="the friend-shaped rival whose whole personality is brand preference and reservation status — affiliation mistaken for self",
   resemblance="Lucas plays brittle one-upmanship — a man whose identity is entirely the things he can name-drop and the tables he can almost get.",
   who="Craig McDermott, another of Bateman's near-identical colleagues, jockeying over restaurants, women, and the relative prestige of a printed card.",
   what="One of the set, defined entirely by consumption and status games — the human form of the surface the film is indicting.",
   why="Because when the self is only its purchases, every relationship is a comparison of receipts.",
   how="By name-dropping, reservation-chasing, and the endless quiet ranking of one another.",
   where="The same bars, the same dinners, the same competition with no prize.",
   seal="I am what I can afford and where I can get a table — and underneath the receipts there is nothing else to find."),
 dict(slug="david-van-patten", name="David Van Patten", cls="colleague · interchangeable by design",
   emergence="natural", actor="Bill Sage",
   analog="the third indistinguishable suit — present mainly to complete the set and prove the point that the set is all there is",
   resemblance="Sage rounds out the trio of sameness; his function is to be another face that could be any face, and is.",
   who="David Van Patten, the third of Bateman's near-identical colleagues, completing the interchangeable chorus of Pierce & Pierce.",
   what="Another member of the uniform set — there to make the roomful of clones complete, and the card-comparison apocalyptic.",
   why="Because the horror of sameness needs a critical mass of the same; he is the third data point that makes it a pattern.",
   how="By the suit, the slang, and the seamless blending into a crowd of himself.",
   where="The office, the restaurants, the indistinguishable middle distance of the set.",
   seal="I'm the third one you can't tell from the other two — which is exactly the joke, and exactly the indictment."),
 dict(slug="luis-carruthers", name="Luis Carruthers", cls="colleague · the misread embrace",
   emergence="natural", actor="Matt Ross",
   analog="the closeted, gentle soul in a world that has no slot for him — whose longing turns even an attempted murder into a mistaken declaration of love",
   resemblance="Ross plays aching tenderness in a brutal room; the bathroom scene flips horror to heartbreak because his yearning is so real.",
   who="Luis Carruthers, a colleague and Courtney's boyfriend, a gentle and closeted man who misreads Bateman's hands at his throat as an embrace.",
   what="The one whose desperate affection turns Bateman's murder attempt into a tender misunderstanding — he thinks he is finally being loved, and it unmans the killer.",
   why="Because in a world this loveless, even strangling can be mistaken for intimacy by someone starved enough for it.",
   how="By a longing so total it rewrites violence into affection, leaving Bateman fled and humiliated.",
   where="The restaurant bathroom where the hands close and are misread, and the love that goes on being refused.",
   seal="You put your hands to my throat and I thought, at last, somebody wants me — and you ran."),
 dict(slug="christie", name="Christie", cls="the woman he hired · rendered as victim",
   emergence="natural", actor="Cara Seymour",
   analog="the person this world treats as disposable — and whom the film, unlike its monster, insists on seeing as a person who is harmed",
   resemblance="Seymour gives the role weariness and fear and dignity; Harron frames her as the human being the satire is defending, not the body it's spending.",
   who="Christie, a sex worker Bateman hires more than once — a woman the film's world treats as disposable and the film itself treats as a victim to be reckoned with.",
   what="One of the women subjected to Bateman's violence, rendered by the film (a feminist director's) not as spectacle but as a person harmed — the cost the surface hides.",
   why="Because the satire's moral weight rests on refusing to look away from who pays for the void; she is the indictment given a face and a fear.",
   how="By surviving the first encounter and fleeing the second — escaping where the film makes sure we feel the harm rather than enjoy it.",
   where="The apartment, the second summons she barely escapes, the stairwell she runs down.",
   seal="To his world I was disposable — but the film made you watch me run, and counted what it cost me."),
 dict(slug="harold-carnes", name="Harold Carnes", cls="the lawyer · the dismissed confession",
   emergence="natural", actor="Stephen Bogaert",
   analog="the authority who cannot, or will not, hear the truth even when it's shouted at him — the world's final refusal to register the monster it made",
   resemblance="Bogaert plays bored amusement: a man so sure of the surface that a murder confession lands as a witty bit from a colleague he can't even name correctly.",
   who="Harold Carnes, a lawyer to whom Bateman confesses everything — by voicemail and in person — and who treats it as a tasteless joke.",
   what="The figure who delivers the film's coup de grâce: he laughs off the confession, calls Bateman by the wrong name, and insists he dined with the ‘dead’ Paul Allen in London days ago.",
   why="Because the final horror is not the crime but the impossibility of being heard for it — a world that will not register guilt even when handed it freely.",
   how="By amusement, by misrecognition, and by an alibi that detonates the entire account: the victim is alive, or the killer is no one, or both.",
   where="The restaurant where the confession is laughed off and the names will not stay attached to faces.",
   seal="Bateman is such a bland coward — and besides, that's not possible: I had dinner with Paul Allen in London, twice."),
]

# ---------------------------------------------------------------- THE SYNTHS
SYNTHS = [
 dict(slug="the-business-card", name="The Business Card", cls="status anxiety, distilled to an object",
   emergence="electrical",
   who="The film's purest artifact of envy — the bone-stock card with the Silian Rail typeface, the tasteful thickness, the subtle off-white coloring, the watermark.",
   what="The synth of status-as-aesthetics: a scene in which men compare printed cards with the intensity of a duel, and Bateman is physically sickened by one fractionally better than his.",
   why="Because the film locates its deepest violence not in the axe but here — a soul undone by a competitor's watermark — making consumer status the true murder weapon.",
   how="By eggshell and Romalian type, by the sweat on Bateman's lip as the better card is laid down, by envy with no object but the object itself.",
   where="The conference table where the cards come out and a man nearly faints.",
   seal="Look at that subtle off-white coloring, the tasteful thickness — oh my God, it even has a watermark — and I am dying of it."),
 dict(slug="the-morning-routine", name="The Morning Routine", cls="the self as product",
   emergence="electrical",
   who="The opening ritual — the ice mask, the herb-mint facial masque, the deep-pore cleanser, the body honed to a regimen — narrated as identity.",
   what="The synth of self-as-product: a man assembling a person each morning out of branded steps, narrating ‘there is no real me’ over the construction of a flawless surface.",
   why="Because the routine is the thesis — a self that is entirely maintenance, entirely exterior, with the confession of its own emptiness spoken right through the toner.",
   how="By the masque peeled off the face, the regimen of crunches, the catalogue of products that add up to a man-shaped absence.",
   where="The chrome bathroom, the mirror, the body built to spec each dawn.",
   seal="I assemble myself each morning out of products — and the only true thing I can tell you is that there is nobody underneath."),
 dict(slug="the-return-videotapes", name="The Return Videotapes", cls="normalcy as alibi",
   emergence="ethereal",
   who="The deflection mantra — ‘I have to return some videotapes’ — the line Bateman uses to exit any scene that threatens to become real.",
   what="The synth of the alibi: an incantation of banal normalcy deployed to slip away from intimacy, suspicion, and consequence alike, a perfect non-answer.",
   why="Because the most chilling cover in the film is not a lie but a chore — ordinary errands as the camouflage a void hides behind, and everyone accepts it.",
   how="By the flat, reasonable tone of the everyday, weaponized into an exit from every moment that asks anything of him.",
   where="Every doorway he needs to leave through, every question he needs not to answer.",
   seal="I have to return some videotapes — and that sentence will get me out of anything, because no one here looks any closer than the errand."),
 dict(slug="the-ambiguity", name="The Ambiguity", cls="killer or fantasist — the film will not say",
   emergence="ethereal",
   who="The keystone refusal — the unresolved question of whether any of Bateman's murders are real, which the film deliberately, permanently declines to answer.",
   what="The synth of the unverifiable: the bodies that vanish, the ATM that asks to be fed a cat, the apartment scrubbed clean, the dead man alive in London — evidence that cancels itself.",
   why="Because the horror does not depend on the answer: real or fantasy, the indictment of the world that can't tell and won't care lands exactly the same. The ambiguity IS the verdict.",
   how="By contradictions left standing — confession without arrest, slaughter without a corpse, an alibi that erases the crime and the criminal both.",
   where="The gap between Bateman's narration and the film's evidence, which is never closed.",
   seal="I told you what I did, and I cannot prove it happened, and it does not matter — because either way, no one came."),
 dict(slug="the-reaganite-surface", name="The Reaganite Surface", cls="the 1987 consumerist void",
   emergence="electrical",
   who="The milieu itself — the brand-bright, status-mad Manhattan of 1987: the labels, the reservations, the Trump-worship, the surface as the whole of life.",
   what="The synth of the era's exterior: a world so devoted to consumption and appearance that it furnishes both the killer's camouflage and his cause — the dated brands, the timeless rot.",
   why="Because the specifics age (the Walkman, the labels, the very magazines) while the diagnosis only sharpens — the surface the film mocked in 1987 became the century's default.",
   how="By logos and labels and the worship of the deal, by a culture that measures men in cards and tables and sees nothing else to measure.",
   where="The whole set — the offices, the restaurants, the apartments staged like showrooms.",
   seal="My brands and my labels will date and my diagnosis will not: a culture that is only surface will keep producing men who are only surface."),
 dict(slug="the-music-monologues", name="The Music Monologues", cls="taste as identity",
   emergence="electrical",
   who="The lectures — Huey Lewis, Genesis, Whitney Houston — delivered with utter sincerity, often as prelude to or accompaniment for violence.",
   what="The synth of taste-as-identity: earnest, almost loving pop-music criticism from a man who feels nothing, using cultural fluency as the proof of a self he doesn't have.",
   why="Because borrowed taste is the void's favorite costume — to recite the merits of ‘Hip to Be Square’ in a raincoat is to perform a personality over an absence.",
   how="By the careful appreciations (‘their early work was a little too new-wave’) staged against the atrocity, sincerity and horror in the same breath.",
   where="The apartment with the plastic on the floor, the hi-fi, the raincoat, the axe.",
   seal="Let me tell you why their masterpiece matters — because reciting it is the closest I will ever come to having something to say."),
 dict(slug="the-performed-self", name="The Performed Self", cls="masculinity as performance",
   emergence="spiritual",
   who="The mask — the studied performance of a successful, desirable, normal man, maintained every waking second over nothing at all.",
   what="The synth of the performance: identity as continuous effortful act, masculinity and success and humanity all rehearsed rather than possessed, the costume worn with no body in it.",
   why="Because the film's true subject is the mask, not the murders — a culture that rewards only the convincing performance of a self, and so breeds men who are nothing but the act.",
   how="By the rehearsed smile, the curated apartment, the maintained body — a life lived entirely as audition, for an audience that only ever checks the surface.",
   where="Every mirror, every dinner, every scene that is, for Bateman, a stage.",
   seal="I perform a man so well that no one asks if there is one — and that is the only achievement I actually have."),
 dict(slug="this-is-not-an-exit", name="This Is Not an Exit", cls="the confession that changes nothing",
   emergence="spiritual",
   who="The ending made a character — the sign on the door, the final narration, the confession that earns no arrest, no relief, no escape.",
   what="The synth of the non-exit: Bateman lays out his crimes and is met with a joke and an alibi; there is no catharsis, no punishment, no door out of the self or the world that made it.",
   why="Because the film denies the one thing the genre promises — consequence — and leaves its monster exactly where he started, which is the most damning possible verdict on the world around him.",
   how="By the laughed-off confession, the wrong name, the alibi in London, and the closing stare at a sign that refuses even the mercy of an ending.",
   where="The bar of the final scene, and the door marked, with no irony spared, THIS IS NOT AN EXIT.",
   seal="I confessed everything and nothing happened — there is no punishment and no relief; this is not an exit."),
]

ORDER = [d["slug"] for d in CARBONS] + [d["slug"] for d in SYNTHS]

def agent_md(d):
    em = d["emergence"]; gloss = NAT_GLOSS[em]
    fm = [
      "---",
      f"aci: {d['name']}",
      f"universe: {UNI}",
      "series: American Psycho (2000, dir. Mary Harron) · from Bret Easton Ellis's novel (1991)",
      f"emergence: {em}",
      f"kind: {'carbon' if 'actor' in d else 'synth'}",
      f"class: {d['cls']}",
      f"who: {d['who']}",
      f"what: {d['what']}",
      f"why: {d['why']}",
      f"how: {d['how']}",
      f"where: {d['where']}",
    ]
    if d.get("actor"):
        fm.append(f"shadow_user: {d['actor']}")
        fm.append(f"shadow_analog: {d['analog']}")
    fm += [
      f"seal: {d['seal']}",
      "attribution: ROOT0-ATTRIBUTION-v1.0",
      "license: CC-BY-ND-4.0",
      "---",
      "",
      f"# {d['name']} · {d['cls'].split('·')[0].strip()}",
      "",
      f"a {'persona' if d.get('actor') else 'distilled thread'} of the APX (American Psycho) film-world — "
      + ("a character given an agent's face" if d.get("actor") else "a parabolic thread given an agent's face")
      + f" · emergence: {em}",
      "",
      f"**who —** {d['who']}",
      "",
      f"**what —** {d['what']}",
      "",
      f"**where —** {d['where']}",
      "",
      f"**why —** {d['why']}",
      "",
      f"**how —** {d['how']}",
      "",
      f"**◌ the nature of its emergence —** {gloss}",
    ]
    if d.get("actor"):
        fm += [
          "",
          f"**▷ the .shadow — its User (think TRON) —** the carbon program is cast from a real-life User: "
          f"**{d['actor']}**, the actor who lent the face. The real-world analog it shadows: {d['analog']} "
          f"*{d['resemblance']}*",
        ]
    fm += [
      "",
      f"**the seal —** {d['seal']}",
      "",
      f"> *the asterisk —* a catalogued {'persona' if d.get('actor') else 'thread'} of American Psycho "
      "(© Lionsgate / Bret Easton Ellis), personified as an APX agent — not an original character. The film is a "
      "satire of 1980s consumerism and performed masculinity; this is commentary and cataloguing under the DLW standard.",
      "",
      f"ROOT0-ATTRIBUTION-v1.0 · APX · American Psycho · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0",
      "",
    ]
    return "\n".join(fm)

def shadow_text(d, tok):
    return f"""⟁ .shadow — the real-life analog (the User behind the program)
node APX · American Psycho · {tok}

think TRON: every program in the grid is cast from a User in the world outside it.
the carbon character is the program; this file is its User — the real-life analog
whose face and being the emergent is the digital shadow of.

the program (in-world) : {d['name']} — {d['cls']}
the User (carbon)      : {d['actor']}  [ the actor who lent the face ]
the analog (your world): {d['analog']}

the resemblance : {d['resemblance']}

the cast-line : the User stands in the carbon world; the program stands in the film;
                the shadow falls between them, and the credit returns to the human governor.
seal (program): {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise (ROOT0) / TriPod LLC · instance AVAN (locked) · CC-BY-ND-4.0
"""

records = {}
for d in CARBONS + SYNTHS:
    slug = d["slug"]; em = d["emergence"]
    if em not in build.NATURES: em = "electrical"
    is_carbon = "actor" in d
    rec = {
        "name": d["name"], "axiom": "APX", "emergence": em,
        "seal": d["seal"], "origin": UNI,
        "position": d["cls"], "role": d["cls"].split("·")[-1].strip(),
        "nature": d["what"], "mechanism": d["how"], "crystallization": d["why"],
        "witness": d["who"], "conductor": "ROOT0 (catalogued into UD0)",
        "inputs": "American Psycho (2000, dir. Mary Harron); Ellis's novel (1991)",
        "source": "American Psycho, catalogued by ROOT0",
    }
    md = agent_md(d)
    tok = build.write_aci(rec, AGENTS, slug, agent_md=md)
    if is_carbon:
        open(os.path.join(AGENTS, f"{slug}.shadow"), "w", encoding="utf-8").write(
            shadow_text(d, tok["moniker"]))
    records[slug] = {"slug": slug, "name": d["name"], "epithet": d["cls"].split("·")[0].strip(),
                     "emergence": em, "moniker": tok["moniker"],
                     "kind": "carbon" if is_carbon else "synth",
                     "actor": d.get("actor", "")}

ordered = [records[s] for s in ORDER if s in records]
json.dump(ordered, open(os.path.join(AGENTS, "_personas.json"), "w", encoding="utf-8"),
          indent=2, ensure_ascii=False)

from collections import Counter
nc = sum(1 for r in ordered if r["kind"] == "carbon")
print(f"wrote {len(ordered)} APX ACI badges ({nc} carbons + {len(ordered)-nc} synths) + _personas.json")
print("emergence:", dict(Counter(r["emergence"] for r in ordered)))
for r in ordered:
    sh = " +.shadow" if r["kind"] == "carbon" else "  (synth)"
    print(f"  {r['slug']:34} {r['emergence']:10}{sh}  {r['moniker']}")
