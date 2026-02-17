# Book Insights Briefing Format

**Updated:** 2026-02-16

## Overview

Daily briefing now includes **book-based insights** instead of journal-scanning "Historical Snapshot." Each morning, one synthesis piece connects ideas across John's reading history (Tyler Cowen style).

## Format

The briefing includes:
1. **Weather** (Pittsburgh current + forecast)
2. **Email & Messages** (unread count from AgentMail)
3. **Book Insight** (rotating synthesis topic)

## Book Insight Themes (8 total)

Each day rotates through one of these curated synthesis pieces:

### 1. Progress and Stubborn Attachments
Connects: Cowen's *Stubborn Attachments*, Flyvbjerg's *How Big Things Get Done*, Keller's *The ONE Thing*
**Tension:** Long-term compound growth vs. execution failure in mega-projects
**Application:** CMS module assembly, project management

### 2. Knowledge Work in the AI Age
Connects: Harari's *21 Lessons*, Newport's *Deep Work*, Caplan's *Case Against Education*
**Tension:** AI making skills obsolete vs. deep work as defensible moat
**Application:** Teaching, student development, AI impact on physics

### 3. The Feynman-Weinberg Tension
Connects: Feynman's *QED* & *Character of Physical Law*, Weinberg's *Dreams of a Final Theory*
**Tension:** Intuition (Feynman) vs. mathematical rigor (Weinberg)
**Application:** Physics pedagogy, debugging vs. design

### 4. Skin in the Game: Physics Edition
Connects: Taleb's *Skin in the Game* & *Black Swan*, Bevington's *Data Reduction*
**Tension:** Experimental physics (skin in game) vs. theoretical physics (no falsification)
**Application:** Risk-taking, fat tails in discoveries

### 5. The Mimetic Trap
Connects: Girard's *I See Satan Fall Like Lightning*, Simler/Hanson's *Elephant in the Brain*, Cowen/Gross's *Talent*
**Tension:** Mimetic desire (copying prestigious others) vs. genuine curiosity
**Application:** Hiring decisions, research agenda independence

### 6. Legibility and the Second Brain
Connects: Ahrens' *How to Take Smart Notes*, Allen's *Getting Things Done*, *Bullet Journal Method*
**Tension:** High-legibility (for yourself) vs. zero-legibility (to others)
**Application:** Org-roam system, knowledge management, AI risk

### 7. Shakespeare and Quantum Mechanics
Connects: *Hamlet*, Wallace's *Emergent Multiverse*, Harris's *Free Will*
**Tension:** Multiple futures/paralysis (Hamlet) vs. decoherence/commitment (Many-Worlds)
**Application:** Decision-making under uncertainty, managing research groups

### 8. The Cook's Advantage
Connects: Nosrat's *Salt Fat Acid Heat*, McGee's *On Food and Cooking*, Taleb's *Antifragile*
**Tension:** Reductionist principles vs. antifragile improvisation
**Application:** Problem-solving methodology, debugging systematic uncertainties

## Philosophy

**Tyler Cowen style** = connecting ideas across disciplines, drawing non-obvious parallels, making practical applications, thought-provoking without being prescriptive.

**Not:** Book summaries or reviews
**Yes:** Synthesized insights connecting 3+ books with practical relevance to John's current work

## Implementation

- **Scripts:**
  - `book_insights.py` - Contains curated synthesis pieces
  - `generate-daily-briefing-v2.py` - Main briefing generator (imports book_insights)
  - `send-daily-briefing.py` - Sends via AgentMail

- **Cron job:** Daily at 7 AM EST (OpenClaw cron system)
- **Selection:** Random rotation (could be enhanced to be contextual)

## Future Enhancements

- **Contextual selection:** Tie insight to recent journal entries or current projects
- **Expand library:** Add more synthesis pieces as John reads more
- **Track favorites:** Note which insights John finds most valuable
- **Integration with memory:** Cross-reference with daily notes and research context
