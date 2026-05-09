# Customer Interview Script (Mom Test)

Adapted from Rob Fitzpatrick, *The Mom Test*. Use this script *before* any product is built. Goal: extract whether the problem is real, painful, frequent, and currently spending money — without contaminating the data with your idea.

## Setup

- **Length:** 20-30 minutes. Don't go longer; you'll learn less per minute.
- **Format:** 1:1, voice or video. Group is fine for early scoping but loses signal.
- **Recording:** Always ask permission. Recording is fine; transcripts are gold.
- **Talking ratio:** Aim for 30% you, 70% them. If you're talking more, you're pitching.
- **Don't pitch.** Don't describe your idea until the very end (if at all). The moment you say "I'm building X," every answer that follows is contaminated.

## The opening (60 seconds)

> "Thanks for jumping on. I'm trying to understand how people in [their role / their industry] handle [their domain area, broadly]. I'm not selling anything — I just want to learn how the work actually happens. Mind if I record this so I'm not scribbling notes the whole time?"

**Key moves:**
- Frame as **research about their work**, not your product
- Don't name your hypothesis
- Get permission to record

---

## The five sections (rough timing)

### 1. Their world (5 min)
Establish baseline. Get them comfortable talking about their day.

- "Walk me through what you actually do day-to-day."
- "What's a typical week look like?"
- "What's the hardest part of [the relevant function]?"
- "Who else is involved in [process]?"
- "What tools are you using right now? Walk me through them."

**Listen for:** Tools they use (current alternatives), people who slow them down, manual workarounds, frustration cues.

---

### 2. The pain story (10 min — the heart of the interview)

This is where you find out if the problem is real. Use **past-tense, specific** prompts only.

- **"Tell me about the last time you had to [do the relevant task]."**
- "Walk me through it from start to finish."
- "How long did it take?"
- "What went wrong?"
- "What did you do when [the bad thing happened]?"
- "Who else got involved?"
- "What did it cost you — time, money, deals, sleep?"
- "How often does this happen?"

**Follow-up patterns:**
- They say "it sucks" → "Tell me about a specific time it sucked."
- They say "it takes forever" → "How long did it take last time?"
- They say "we hate [tool]" → "When did you last try to switch?"

**The story litmus test:** By the end of this section, you should be able to retell their last bad experience with specific numbers, dates, and named alternatives. If you can't, you got platitudes, not data.

---

### 3. Current solutions and money (5 min)

Establish what they're already doing and paying for.

- "How are you handling [problem] today?"
- "What tools or services have you tried?"
- "Why did you pick [their current tool]?"
- "What does it cost you — both money and time?"
- "When did you last consider switching?"
- "Have you ever paid someone to fix this manually?"
- "Has your team ever built something internal for it?"

**Listen for:** Real spending, internal tools (= unmet demand), past switching attempts (= active dissatisfaction), specific frustrations with current tools.

**Why this matters:** Existing spend on bad alternatives is the single strongest pre-build signal. "I'm currently paying $200/mo for [tool] but it doesn't [thing]" is gold. "I'd pay if something existed" is fluff.

---

### 4. The dream (3 min — optional)

Only after you've extracted the pain story.

- "If you could wave a magic wand, what would the ideal version of [process] look like?"
- "What would have to be true for you to switch from your current setup?"
- "If a tool existed that solved [the specific pain they described], how much would it be worth to you per month?"

**Be skeptical of these answers.** Future-tense statements about future spending are aspirational, not predictive. Note them, but weight them at 0.2x compared to past-behavior data.

---

### 5. The introduction ask (2 min)

Always end with this. It's the highest-signal close.

- "Who else should I talk to about this?"
- "Can you intro me?"
- "If I built something to solve [their specific pain], would you want to be one of the first to try it? At what price?"
- "Mind if I follow up in [X weeks]?"

**The intro is the test.** If they enthusiastically intro you to 2-3 peers, they think the problem is real. If they hedge ("hmm, let me think about it"), the pain wasn't strong enough.

---

## The seven Mom Test rules (cheat sheet)

| Rule | Bad question | Good question |
|---|---|---|
| Talk about their life, not your idea | "Would you use [our product]?" | "Walk me through the last time you had to [do the thing]." |
| Specific past, not generic future | "Do you usually have this problem?" | "When did you last have this problem?" |
| Listen, don't pitch | (You explain your idea for 2 min) | "Tell me more — what happened next?" |
| Anchor in real money | "Would you pay for this?" | "What are you paying for [current alternative]?" |
| Anchor in time/work cost | "Is it annoying?" | "How many hours did you spend on it last week?" |
| Watch for compliments | "Cool idea!" → smile | "Cool idea!" → "Glad you think so. So tell me — when did you last try something like this?" |
| Ask for the next intro | (You wrap up) | "Who else should I talk to?" |

---

## What to write up immediately after

Within 1 hour of the interview, while it's fresh, fill in:

```
Interviewee: [first name, role, company size]
Date: [YYYY-MM-DD]

THEIR WORLD (1-2 sentences)
- What they do, who they work with.

THE STORY (the most specific pain story they told)
- When: [date or rough timeframe]
- What happened: [the sequence]
- Cost: [time, money, deals lost]
- Frequency: [how often]
- Their words: [direct quote, exact phrasing]

CURRENT ALTERNATIVES (the literal list)
- [Tool 1] — $X/mo, complaint: [...]
- [Tool 2] — internal hack, complaint: [...]
- [Manual process] — N hours/week, complaint: [...]

WTP SIGNAL (Tier 1: behavior, Tier 2: stated, Tier 3: hypothetical)
- Tier 1: [are they paying for an alternative? how much?]
- Tier 2: [did they name a price they'd pay?]
- Tier 3: [hypothetical reactions — discount these]

EMOTIONAL TEMPERATURE
- 1 (indifferent) → 5 (rage)
- Score: [...]
- Why: [specific tells — voice tone, profanity, body language]

INTRO ASK RESULT
- Did they offer 1+ intros? Y/N
- Names: [...]

THREE QUOTES (verbatim, for use in the landing page later)
1. "..."
2. "..."
3. "..."

INTERVIEWER FAILURES
- Where I broke the Mom Test (be honest):
- What I'd do differently next time:
```

The verbatim quotes are extremely high-value — they become headline copy when you do landing page tests later. The "interviewer failures" section is what makes interview #6 better than interview #1.

---

## When to stop interviewing

You're done with the first round when:

- You can predict the next interviewee's pain story before they tell it
- The same 2-3 alternatives keep coming up unprompted
- 3+ people have offered intros
- 1+ person has volunteered to pay before you mentioned price

Typical: **8-15 interviews** to hit this point. Stopping at 3 is too early; doing 50 is procrastination disguised as research.

After the first round, the next move is **always** a landing page or pre-sell — not more interviews.
