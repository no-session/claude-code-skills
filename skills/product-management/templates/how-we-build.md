# How We Build

Our approach to building product — the operating system for how product, engineering, and design work together to ship great things.

---

## Our Philosophy

Building great product is a team sport. We believe the best outcomes come from small, empowered teams with clear ownership, tight feedback loops, and a bias toward shipping. This document describes how we turn that belief into practice.

---

## Team Structure: Pods

We organize into **pods** — small, cross-functional teams that own a problem space end-to-end.

### Pod Composition
A typical pod includes:
- **1 PM** — owns the "what" and "why"
- **1 Designer** — owns the user experience
- **2-5 Engineers** — own the "how" and technical execution
- **Embedded support** (as needed) — data analyst, QA, etc.

### Pod Principles
- **Autonomous:** Pods make their own tactical decisions within their problem space. They don't need permission to ship.
- **Accountable:** Each pod owns metrics, not just features. They're measured by outcomes.
- **Stable:** Pod composition stays consistent for at least a quarter. Context-switching across pods is expensive.
- **Small:** If a pod needs more than 7 people, it should split into two pods.

### Pod Ownership Areas

| Pod | Problem Space | Key Metrics |
|-----|--------------|-------------|
| [Pod 1] | [What they own] | [What they measure] |
| [Pod 2] | [What they own] | [What they measure] |
| [Pod 3] | [What they own] | [What they measure] |

---

## The Build Cycle

We operate in **6-week cycles** with a **2-week cooldown** between them.

### 6-Week Build Phase

| Week | Focus |
|------|-------|
| **Week 1** | Kickoff, detailed planning, design finalization, technical spikes |
| **Week 2-3** | Core development. Ship internal alpha by end of Week 3. |
| **Week 4-5** | Polish, edge cases, integration testing. Ship beta to internal dogfooding or friendly customers. |
| **Week 6** | QA, documentation, launch prep. Ship to production. |

### 2-Week Cooldown

The cooldown isn't vacation — it's for:
- **Bug fixes and polish** from the previous cycle
- **Technical debt paydown** (each engineer picks one item)
- **Exploration and prototyping** for the next cycle
- **Customer research** — PMs spend time with users
- **Learning** — tech talks, reading, experimentation

### Why Cycles Over Sprints
- 6 weeks is long enough to build something meaningful but short enough to maintain urgency.
- The cooldown prevents burnout and creates space for the "important but not urgent" work.
- Fixed cycles create predictability for stakeholders without micromanaging the team.

---

## The Product Development Lifecycle

### Phase 1: Discovery (1-2 weeks)
**Goal:** Validate that the problem is worth solving.

- PM writes a **Problem Brief** (1 page max): What's the problem? Who has it? How big is it? What's our evidence?
- Team reviews the brief and asks: "Is this the most important thing we could work on?"
- PM conducts **5-10 customer conversations** focused on the problem (not solutions).
- **Exit criteria:** Clear problem statement with evidence. Team agrees this is worth pursuing.

### Phase 2: Definition (1-2 weeks)
**Goal:** Align on the solution approach.

- PM writes the **PRD** (using our PRD template).
- Designer creates **low-fi concepts** or wireframes.
- Engineering provides **technical assessment** — feasibility, risks, architectural considerations.
- Team reviews together in a **Solution Review** meeting.
- **Exit criteria:** Approved PRD with clear scope, success metrics, and timeline.

### Phase 3: Build (4-6 weeks, varies by scope)
**Goal:** Ship a working solution.

- Pod works autonomously within the agreed scope.
- **Daily standups** (15 min max) for coordination.
- **Weekly demo** to the broader team — show working software, not slides.
- PM is available for questions and scope negotiations — not micromanaging.
- **Exit criteria:** Feature complete, tested, and ready for launch.

### Phase 4: Launch (1 week)
**Goal:** Get the feature into users' hands and start learning.

- **Launch checklist:** Documentation, analytics instrumentation, feature flags, rollout plan.
- **Staged rollout:** Internal → beta users → % rollout → GA.
- PM writes a **launch brief** for internal stakeholders: what shipped, why, how to talk about it.
- **Exit criteria:** Feature is GA, dashboards are live, support team is briefed.

### Phase 5: Learn (Ongoing)
**Goal:** Validate that the solution actually works.

- PM monitors success metrics for **4-6 weeks** post-launch.
- Team conducts **5+ customer interviews** about the new feature.
- PM writes a **Ship Report** (1 page): What shipped, what we learned, what we'd do differently, next steps.
- **Decision point:** Iterate, expand, maintain, or sunset.

---

## Meetings and Rituals

### Weekly

| Meeting | Duration | Who | Purpose |
|---------|----------|-----|---------|
| **Pod Standup** | 15 min/day | Pod | Coordination and blockers |
| **Pod Demo** | 30 min | Pod + stakeholders | Show working software |
| **Design Review** | 45 min | PM + Design + Eng leads | Review design work in progress |

### Per-Cycle

| Meeting | Duration | Who | Purpose |
|---------|----------|-----|---------|
| **Cycle Planning** | 2 hours | All pods | Commit to cycle goals |
| **Cycle Retro** | 1 hour | All pods | What worked, what didn't, what to change |
| **Roadmap Review** | 1 hour | PMs + Leadership | Update and align on quarterly direction |

### Quarterly

| Meeting | Duration | Who | Purpose |
|---------|----------|-----|---------|
| **Quarterly Planning** | Half-day | PMs + Eng leads + Leadership | Set quarterly goals, assign pods, allocate resources |
| **Customer Advisory Board** | 2 hours | PMs + key customers | Validate direction, gather feedback |

---

## Decision-Making

### RACI-ish (Simplified)

We don't love bureaucratic RACI charts, but clarity on who decides matters:

| Decision Type | Decides | Consulted | Informed |
|--------------|---------|-----------|----------|
| What problem to solve | PM | Eng Lead, Designer, Leadership | Team |
| Solution approach | PM + Designer + Eng Lead (consensus) | Team | Stakeholders |
| Technical architecture | Eng Lead | PM, Engineers | Designer |
| Visual/interaction design | Designer | PM, Eng Lead | Team |
| Scope trade-offs (within cycle) | Pod (PM + Eng Lead) | — | Leadership |
| Scope trade-offs (cross-cycle) | PM + Leadership | Eng Lead | Team |
| Launch timing | PM | Eng Lead, Leadership | Everyone |

### The "Two-Way Door" Test
- **One-way door** (irreversible): Requires broad input and leadership sign-off. Take your time.
- **Two-way door** (reversible): The pod decides and moves fast. Don't escalate.

---

## Shipping Principles

1. **Ship small, ship often.** Break big features into independently valuable increments.
2. **Feature flags everything.** We decouple deployment from release. Code goes to production continuously; features are enabled deliberately.
3. **Instrument before you launch.** If you can't measure it, you can't learn from it.
4. **Write the launch email before you build.** If you can't explain why a customer should care in two sentences, rethink the scope.
5. **No silent launches.** Even small changes get a brief internal announcement. Surprises erode trust.

---

*This is how we build today. It should evolve as we grow. If something in this doc is consistently getting in the way, raise it in retro and let's change it.*
