#!/usr/bin/env python3
"""
Generate book-based insights for daily briefing (Tyler Cowen style)

Pulls from John's reading history and creates synthesized insights
connecting ideas across books, disciplines, and current context.
"""

import random
from datetime import datetime

# Book-based insights - curated connections across John's reading
INSIGHTS = [
    {
        "theme": "Progress and Stubborn Attachments",
        "books": ["Stubborn Attachments (Cowen)", "How Big Things Get Done (Flyvbjerg)", "The ONE Thing (Keller)"],
        "insight": """Tyler Cowen's *Stubborn Attachments* argues for sustainable economic growth as a moral imperative—compound growth over centuries transforms civilization. But Flyvbjerg's *How Big Things Get Done* shows most mega-projects fail because of planning fallacy and poor execution.

**The tension:** Cowen wants us to optimize for long-term growth; Flyvbjerg shows we're terrible at executing big things. Keller's "ONE Thing" offers the bridge: focus ruthlessly on the single action with the biggest long-term multiplier.

**For your work:** CMU's CMS detector assembly (~5000 modules over 2+ years) is exactly the kind of big project Flyvbjerg studies. What's the ONE thing that prevents cascading delays? What planning blind spots are you carrying? The compound effects of small execution improvements dwarf the clever physics.""",
        "relevance": "Current: CMS module assembly, project management"
    },
    {
        "theme": "Knowledge Work in the AI Age",
        "books": ["21 Lessons for 21st Century (Harari)", "Deep Work (Newport)", "Case Against Education (Caplan)"],
        "insight": """Harari warns that AI will make most human skills obsolete faster than we can retrain. Newport argues *deep work* is becoming rare and therefore valuable. Caplan claims education is mostly signaling, not skill-building.

**Synthesis:** If Harari is right about AI velocity, and Caplan is right that most education is signaling, then Newport's deep work becomes the *only* defensible moat. LLMs can't yet do what you do at 3 AM debugging a coffea analysis with 15 tabs of documentation and a physics intuition built over 15 years.

**The catch:** Your PhD students are learning in the AI era. Are they developing deep work capacity or learning to prompt-engineer? The ones who can hold complex physics models in working memory will be fine. The ones who outsource thinking to ChatGPT are building on sand.

**Question for you:** When you review a student's analysis, can you tell whether they *understand* the systematic uncertainty or just asked Claude to calculate it?""",
        "relevance": "Teaching, AI impact on physics research"
    },
    {
        "theme": "The Feynman-Weinberg Tension",
        "books": ["QED (Feynman)", "Dreams of a Final Theory (Weinberg)", "The Character of Physical Law (Feynman)"],
        "insight": """Feynman and Weinberg represent two philosophies of physics understanding:

**Feynman:** "What I cannot create, I do not understand." Obsessed with *intuition*—finding the picture, the analogy, the way to *feel* what the math means. QED is a masterclass in building intuition for impossible quantum behavior.

**Weinberg:** Embrace the math. The equations *are* the reality. "Dreams of a Final Theory" is unapologetically reductionist—fundamental laws all the way down, and if you can't visualize it, that's your problem, not nature's.

**Who's right?** Both and neither. Weinberg-style rigor keeps you honest; Feynman-style intuition makes you productive. You need Weinberg when designing triggers (precision matters). You need Feynman when debugging 2 AM anomalies (what does this *mean*?).

**Your Shakespeare habit** is actually Feynman training: Hamlet forces you to hold contradictory models of human psychology simultaneously. That's *exactly* what QFT demands—particle and wave, real and virtual, all at once.""",
        "relevance": "Physics pedagogy, your current readings"
    },
    {
        "theme": "Skin in the Game: Physics Edition",
        "books": ["Skin in the Game (Taleb)", "Black Swan (Taleb)", "Data Reduction and Error Analysis (Bevington)"],
        "insight": """Taleb's core insight: *Don't trust people who don't have skin in the game.* Most forecasters, consultants, and pundits have upside without downside.

**Physics version:** Every experimental physicist has skin in the game. You're not writing op-eds about particle physics—you're building detectors, analyzing data, claiming discoveries. If you're wrong about a systematic uncertainty, *your name is on the paper*. That's the ultimate skin in the game.

But here's where it gets interesting: Taleb would argue most theorists *don't* have skin in the game. String theorists can be wrong for 40 years with no consequence. No falsifiable predictions = no risk = no skin.

**Your advantage as an experimentalist:** You live in Taleb's world of *fat tails* (rare events with huge impact). The Higgs discovery, unexpected Run 3 anomalies—these are Black Swans. Bevington's error analysis is about quantifying the unknown unknowns.

**Connection to Caplan:** Caplan says education is signaling. But a PhD in experimental particle physics? That's *costly signaling* with real skin—you can't fake detector knowledge or survive a thesis defense without substance.""",
        "relevance": "Experimental vs theoretical physics, risk-taking"
    },
    {
        "theme": "The Mimetic Trap",
        "books": ["I See Satan Fall Like Lightning (Girard)", "Elephant in the Brain (Simler/Hanson)", "Talent (Cowen/Gross)"],
        "insight": """René Girard's mimetic theory: We don't want things for their intrinsic value. We want them because *others* want them. Mimetic desire drives competition, violence, scapegoating.

Simler and Hanson extend this: Most of our behavior is status-seeking we won't admit to ourselves. We're not as rational as we think. We copy what prestigious people do.

**Academic implications:** How much of your research agenda is genuinely curiosity-driven vs. mimetically copying what prestigious labs (CERN, Fermilab) prioritize? Girard would say mimetic desire is *unavoidable*—the question is whether you're aware of it.

**Cowen's "Talent" twist:** Great talent-spotters resist mimesis. They find the person everyone else overlooked because they're not copying conventional signals. Cowen looks for *persistence* and *genuine curiosity*, not pedigree.

**For hiring:** When you interview lab technicians (like Austin Tarman), are you screening for competence or mimetically copying prestige signals (where they worked, who recommended them)? The reference checks are good—that's avoiding mimetic traps by going direct to the source.

**Your reading pattern itself:** Shakespeare, Feynman, Tyler Cowen, Girard—these aren't mimetically popular in physics departments. That's a signal you're thinking independently.""",
        "relevance": "Hiring decisions, research priorities"
    },
    {
        "theme": "Legibility and the Second Brain",
        "books": ["How to Take Smart Notes (Ahrens)", "Getting Things Done (Allen)", "Bullet Journal Method"],
        "insight": """James Scott's *Seeing Like a State* (you haven't read it yet, but should) argues that *legibility*—making complex systems simple and visible—is how states control. But hyper-legibility destroys local knowledge.

**Your org-roam system:** 1,267 notes, UUID-linked, daily journals, cross-referenced. This is *high-legibility* for yourself and *zero-legibility* to anyone else. That's a feature, not a bug.

**Ahrens' Zettelkasten method** (which org-roam implements) creates a "conversation with yourself over time." Your notes on Stubborn Attachments link to your CMS work, which links to your Shakespeare reading. The connections emerge organically, not through imposed hierarchy.

**GTD and Bullet Journal tension:** GTD wants complete capture and zero mental residue. Bullet Journal wants rapid, tactile logging. You're trying both. Here's the synthesis: GTD for *commitments* (things that must happen), Bullet Journal for *exploration* (things you're thinking about), org-roam for *connection* (ideas across time).

**AI risk:** If you die tomorrow, your org-roam dies with you. The UUID links are opaque. But that's also why it's *thinking infrastructure*, not just storage. LLMs can't yet replicate 15 years of cross-referenced reading and lived context.

**Suggestion:** Export your org-roam graph visualization weekly. If it's growing denser (more connections per new note), you're building knowledge. If it's growing linearly (just adding notes), you're hoarding.""",
        "relevance": "Knowledge management, second brain building"
    },
    {
        "theme": "Shakespeare and Quantum Mechanics",
        "books": ["Hamlet", "The Emergent Multiverse (Wallace)", "Free Will (Sam Harris)"],
        "insight": """Hamlet's tragedy: He can see multiple futures, weigh infinite possibilities, but can't act. "The native hue of resolution / Is sicklied o'er with the pale cast of thought."

**David Wallace's Many-Worlds QM:** Every quantum measurement splits reality. All outcomes happen. The wavefunction never collapses. This isn't philosophy—it's what the math says if you take it seriously.

**Sam Harris on free will:** It's an illusion. You don't choose your thoughts; they arise from prior causes you didn't control. Consciousness is along for the ride.

**The connection:** Hamlet, Many-Worlds, and no-free-will all point to the same vertigo: *You're not in control.* Hamlet obsesses over choice while being a pawn of fate. Many-Worlds says every choice spawns a universe where you chose differently. Harris says "you" didn't choose at all.

**But here's the physicist's escape hatch:** Wallace's Many-Worlds requires *decoherence*—once the quantum system interacts with the environment, the branches separate and become classical. You *can't* access the other yous. Functionally, you're in one timeline, making one choice, living one life.

**The practical takeaway:** Hamlet's paralysis comes from trying to simulate all futures perfectly. Your CMS work requires the opposite—make the best decision with available data, iterate, and move on. Decoherence is a feature: once you commit to a trigger threshold, the alternate universes don't matter.

**Your Shakespeare habit** is training you to simulate *social* quantum mechanics—people are superpositions of motives until they act. That's useful for managing a research group.""",
        "relevance": "Philosophy, decision-making under uncertainty"
    },
    {
        "theme": "The Cook's Advantage",
        "books": ["Salt Fat Acid Heat (Nosrat)", "On Food and Cooking (McGee)", "Antifragile (Taleb)"],
        "insight": """Samin Nosrat's *Salt Fat Acid Heat* reduces cooking to four fundamental concepts. McGee's *On Food and Cooking* explains the chemistry. Both are reductionist—break complex systems into building blocks.

**Taleb's antifragile twist:** Great cooks aren't following recipes; they're improvising with constraints. Too much salt? Add acid. Sauce broke? Add fat. They *benefit* from randomness because they've internalized principles, not procedures.

**Physics parallel:** You're not running canned analysis scripts—you're debugging coffea4bees, adapting to Run 3 data quirks, inventing new systematic checks. That's antifragile research: constraints (the detector, the data) force creativity.

**The danger:** Talismanic thinking. Beginners think great cooks have secret techniques. Actually, they just understand *why* salt dissolves in water, *why* acid brightens flavors, *why* fat carries flavor. The physics is the superpower.

**Your food science reading:** This isn't a hobby—it's the same skill as particle physics. Both require understanding the *generative model* (what produces the outcome) rather than memorizing patterns (correlation without causation).

**Connection to Feynman:** Feynman was famously interested in biology after his physics Nobel. Why? Because complex emergent behavior (life, flavor, consciousness) follows from simple rules (chemistry, thermodynamics). Cooking and particle physics are both reverse-engineering the universe.

**Practical:** When you're stuck on a HGC systematic uncertainty, try Nosrat's method: reduce to fundamentals (what are the four "flavors" of detector effects?), understand the mechanism (not just the correlation), then improvise with constraints.""",
        "relevance": "Problem-solving methodology, your cooking interest"
    }
]

def get_daily_insight():
    """
    Select an insight for today's briefing.
    
    Could be randomized, or could follow a pattern (themes in rotation),
    or could be contextual (tied to John's recent journal entries).
    
    For now: random selection
    """
    insight = random.choice(INSIGHTS)
    
    # Format for briefing
    output = f"""━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📚 INSIGHT FROM YOUR READING

**{insight['theme']}**

*Drawing from: {', '.join(insight['books'])}*

{insight['insight']}

*Relevant to: {insight['relevance']}*
"""
    
    return output

if __name__ == "__main__":
    print(get_daily_insight())
