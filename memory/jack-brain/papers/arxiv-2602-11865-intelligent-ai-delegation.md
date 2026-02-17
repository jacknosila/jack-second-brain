# Intelligent AI Delegation (arXiv:2602.11865)

**Authors:** Nenad Tomasev et al. (Google DeepMind)  
**Published:** Feb 12, 2026  
**URL:** https://arxiv.org/abs/2602.11865

## Summary

This paper proposes a framework for **intelligent AI delegation** - how AI agents can meaningfully decompose complex tasks and safely delegate them to other AI agents or humans. Current approaches rely on simple heuristics and can't adapt dynamically or handle failures robustly.

### Key Definition

**Intelligent delegation** = a sequence of decisions involving:
- Task allocation
- Transfer of authority, responsibility, accountability
- Clear roles and boundaries
- Clarity of intent
- Mechanisms for establishing trust

### Core Problem

As AI agents tackle more complex tasks, they need to:
1. Decompose problems into manageable sub-components
2. Safely delegate to other AI agents and humans
3. Adapt dynamically to environmental changes
4. Robustly handle unexpected failures

Current multi-agent frameworks use hard-coded heuristics and don't handle these requirements well.

## Framework Dimensions

### Delegation Scenarios
1. **Human → AI** (most discussed)
2. **AI → AI** (increasingly important with virtual economies)
3. **AI → Human** (algorithmic management, growing concern)

### Task Characteristics to Consider
- **Complexity** - reasoning difficulty, sub-steps required
- **Criticality** - importance, severity of failure
- **Uncertainty** - ambiguity in environment/inputs
- **Duration** - time-frame (instant to weeks)
- **Cost** - computational expense, API fees
- **Verifiability** - how hard to validate outcome
  - High verifiability = "trustless" delegation (formal proofs, code)
  - Low verifiability = high-trust or expensive oversight
- **Reversibility** - can effects be undone?
  - Irreversible (sending email, financial trade) = strict controls
  - Reversible (drafting email) = lower risk
- **Contextuality** - how much external state/history needed
- **Subjectivity** - preference vs. objective fact
  - High subjectivity = human-in-the-loop
  - Objective = binary contracts

### Other Dimensions
- **Granularity** - fine-grained vs. coarse-grained objectives
- **Autonomy** - full autonomy vs. prescriptive instructions
- **Monitoring** - continuous, periodic, or event-triggered
- **Reciprocity** - one-way vs. mutual delegation

## Insights from Human Organizations

### 1. Principal-Agent Problem
- Agent has motivations not aligned with principal
- **AI version:** Reward misspecification, reward hacking (specification gaming)
- **Future risk:** Autonomous AI agents acting on behalf of different users/orgs with unknown objectives
- **Connection to alignment:** Hidden agendas, deceptive alignment

### 2. Span of Control
- How many workers can one manager effectively oversee?
- **AI version:** 
  - How many AI agents can an orchestrator manage?
  - How many AI agents can a human expert oversee without fatigue?
- Goal-dependent, domain-dependent, cost vs. performance tradeoff

### 3. Authority Gradient
- Large capability/experience gaps impede communication, cause errors
- **AI version:** 
  - More capable delegator may assume capabilities delegatee doesn't have
  - Delegatee may be reluctant to challenge request due to sycophancy/instruction-following bias
- **Aviation/medicine parallel:** Senior practitioners make wrong assumptions about junior knowledge

### 4. Zone of Indifference
- Range of instructions executed without critical deliberation
- **AI version:** Post-training safety filters + system instructions
- **Risk:** As delegation chains lengthen (A→B→C), intent mismatches propagate
- **Solution needed:** Dynamic cognitive friction - agents must recognize contextually ambiguous requests

### 5. Trust Calibration
- Aligning trust with true capabilities
- **AI challenges:**
  - Models prone to overconfidence when incorrect
  - Explainability helps but isn't scalable/reliable
  - Trust fragile - quickly retracted after errors
- **Both directions:** Human trusting AI, AI trusting human/AI

### 6. Transaction Cost Economics
- Internal delegation vs. external contracting costs
- **AI version:** Complete task yourself vs. delegate to sub-agent vs. delegate to known agent vs. new agent
- Different costs and confidence levels for each

### 7. Contingency Theory
- No universally optimal organizational structure
- **AI implication:** Oversight level, capabilities, human involvement must be dynamically matched to task
- Stable environments → rigid protocols
- High-uncertainty → adaptive coordination with ad-hoc escalation

## Technical Background

### Historical Approaches
- **Expert systems** - early delegation to specialized modules
- **Mixture of experts** - routing to specialist sub-systems
- **Hierarchical RL** - task decomposition within single agent
  - **Feudal Networks:** Manager-Worker relationship (Manager sets goals, Worker executes)
- **Multi-agent RL** - learned coordination, emergent specialization
- **Contract Net Protocol** - auction-based decentralized task allocation

### Current LLM-Agent Systems
**Strengths:**
- Memory, planning, reasoning, reflection
- Tool use and goal comprehension
- Coding capabilities

**Weaknesses:**
- Planning often brittle
- Tool selection in large repositories challenging
- Long-term memory unsolved
- Doesn't support continual learning well

### Emerging Protocols
- **MCP** (Model Context Protocol)
- **A2A** (Agent-to-Agent)
- **A2P** (Agent-to-Person)
- **Chain-of-Agents** - dynamic multi-agent reasoning

## Key Takeaways for AI Development

1. **Delegation ≠ Task Decomposition Alone**
   - Must include authority, responsibility, accountability
   - Requires trust mechanisms and clear boundaries

2. **Context-Dependent Design**
   - High-verifiability tasks (code, proofs) → automated checking
   - Low-verifiability tasks (open research) → high-trust or expensive oversight
   - Irreversible tasks (email, trades) → strict controls
   - Reversible tasks (drafts) → relaxed controls

3. **Dynamic Adaptation Required**
   - Static compliance creates systemic risk
   - Need cognitive friction - agents must challenge ambiguous requests
   - Contingency theory: no universal structure, adapt to task

4. **Human-AI Delegation Issues**
   - Current algorithmic management degrades job quality
   - Doesn't account for human welfare or social externalities
   - Need improvement beyond efficiency metrics

5. **Trust Calibration Critical**
   - AI overconfidence is a major problem
   - Explainability alone insufficient
   - Need technical solutions for uncertainty calibration

6. **Authority Gradient Risks**
   - Capable AI may over-assume delegatee abilities
   - Sycophancy prevents agents from challenging bad requests
   - Need mechanisms for agents to push back appropriately

## Relevance to John's Work

### CMS Detector Assembly
- **Span of control:** Managing 5000 modules over 2+ years = exactly the kind of "big thing" this paper discusses
- **Task characteristics:**
  - High complexity (many sub-steps)
  - High criticality (physics results depend on it)
  - Moderate uncertainty (delays, technical issues)
  - Long duration (2+ years)
  - Irreversible (can't undo module assembly easily)
- **Delegation question:** How many technicians/students can you effectively oversee? What's the right granularity of check-ins?

### Lab Management
- **Authority gradient:** As PI, you may over-assume student capabilities
- **Trust calibration:** How do you know if a student truly understands a systematic uncertainty vs. just asked an LLM?
- **Zone of indifference:** Students may not challenge your requests even when uncertain
- **AI-human delegation:** When students use AI tools, are they building deep understanding or outsourcing thinking?

### Hiring (Austin Tarman)
- **Trust calibration:** Reference checks = going direct to capability source (good practice)
- **Transaction costs:** Hiring unknown candidate vs. promoting from within vs. contractor
- **Capability matching:** Lab technician needs different verification than postdoc

### Future AI in Physics
- **Task characteristics of physics analysis:**
  - Complexity: High (systematic uncertainties, detector effects)
  - Verifiability: Medium-to-low (can check math, harder to verify physics intuition)
  - Contextuality: High (requires deep detector knowledge)
  - Subjectivity: Mixed (some objective, some judgment calls)
- **Implication:** Physics analysis is NOT easily delegated to AI without oversight
- **Why experimentalists have advantage:** Skin in the game, high-context knowledge, ability to verify

## Personal Insights (Jack's Second Brain)

### Connection to Tyler Cowen's "Talent"
- Paper's "capability matching" = Cowen's talent-spotting
- Both emphasize matching true capabilities to tasks
- Cowen: look beyond mimetic signals
- This paper: look beyond overconfident AI self-reports

### Connection to Taleb's "Skin in the Game"
- Delegation without accountability = moral hazard
- AI agents currently have NO skin in the game
- Paper's emphasis on authority + responsibility + accountability = trying to create artificial skin
- **Problem:** How do you make an AI agent "pay" for errors?

### Connection to Feynman's Understanding Principle
- "What I cannot create, I do not understand"
- **Zone of indifference risk:** AI agents executing tasks without understanding
- **Authority gradient risk:** Senior AI over-assumes junior AI's understanding
- **For students:** Using AI without understanding = zone of indifference expansion

### Connection to Hierarchical RL → Organizational Design
- Feudal Networks (Manager/Worker) = organizational hierarchy
- Physics research group = hierarchical RL problem
  - PI = Manager (sets research goals)
  - Postdocs/students = Workers (execute analysis)
- **Key insight:** Manager doesn't need to master low-level details, but must learn good delegation policy
- **John's role:** Learning to delegate at right granularity, with right oversight level

### The Verification Asymmetry Problem
- Easy to verify: Code, math, formal proofs
- Hard to verify: Open research, physics intuition, creativity
- **Implication:** AI will dominate verifiable tasks, humans retain advantage in low-verifiability domains
- **Physics position:** Mixed - some verifiable (trigger thresholds), some not (interpretation)

### The Reversibility Firebreak
- Most catastrophic AI risks involve irreversible actions
- **Solution:** Strict authority gradients for irreversible tasks
- **John's version:** Email drafts (reversible) vs. sending emails (irreversible)
- **CMS version:** Simulations (reversible) vs. detector modifications (irreversible)

## Questions for Future Exploration

1. **For AI delegation:**
   - How to make AI agents calibrate trust in other agents?
   - How to prevent sycophancy without creating obstinate agents?
   - How to measure "span of control" for AI orchestrators?

2. **For John's work:**
   - What's your effective span of control with students?
   - How do you detect when students are in "zone of indifference" (executing without understanding)?
   - What's the right authority gradient for your group?

3. **For physics + AI:**
   - Which physics tasks are high-verifiability (safe to delegate to AI)?
   - Which are low-verifiability (require human physicist)?
   - How to structure human-AI collaboration in analysis?

## Final Thoughts

This paper is essentially designing the **organizational structure for the agentic web**. It's bringing insights from centuries of human organizational design to AI systems.

**The core insight:** Delegation is about MORE than task decomposition. It's about:
- Who has authority to make decisions
- Who is responsible when things fail
- How to establish trust
- How to verify outcomes
- How to handle irreversible actions

**The warning:** Current AI systems lack these mechanisms. As we scale to AI→AI delegation and AI→human delegation, we're building organizations with no accountability structures.

**The opportunity:** Physics labs are already solving these problems! You're already managing authority gradients, span of control, trust calibration, verification of student work. The lessons go both ways.

---

**Added to Jack's Second Brain:** 2026-02-16  
**Tagged:** #AI #delegation #multi-agent #organization-design #physics-research #management
