# Question Bank: Product Metrics (93 questions)

**Source:** Aakash Gupta's Product Metrics Interview Cheat Sheet (Top 93 Practice Questions, 2025).
**Framework:** AARM — see `frameworks.md`.

Questions break into 5 macro areas with 16 sub-categories:

| Area | % of questions | Sub-categories |
|---|---|---|
| Success Metrics | 21% | Product Launch, Feature Success, Business Model |
| Diagnostics | 22% | Sudden Drops, Gradual Declines, Unexpected Changes |
| Experimentation | 19% | A/B Test Design, Measurement Strategy, Statistical Rigor |
| Metric Definition | 24% | Engagement, Business Metrics, Technical, Dashboard Design |
| Trade-off Analysis | 19% | UX vs Business, Growth vs Quality, Perf vs Features |

---

## Success Metrics (21%)

### Product Launch Success
_Measuring entirely new products, features, or major releases._

1. How would you measure the success of launching GPT-4.5?
2. If we introduced a new pricing plan tomorrow, what metrics would you track to evaluate its success?
3. How would you define metrics for launching Instagram Threads?
4. What metrics would you use to measure the success of a new checkout flow?
5. How would you measure the launch of a $2B SaaS freemium tier?
6. If we launched a new AI writing assistant, how would you track its success?
7. How do you know if a launch was successful in its first 30 / 60 / 90 days?

### Feature Success
_Measuring incremental additions or improvements to existing products._

1. How would you measure success of adding dark mode to our app?
2. What metrics would indicate that any new recommendation engine is working?
3. How would you track the impact of adding voice search?
4. If we added live streaming to our social app, how would you measure success?
5. How would you define success for a new collaboration feature in Slack?
6. What metrics would you use for a new mobile payment feature?

### Business Model Success
_Measuring changes to how the company makes money or operates._

1. How would you measure the success of transitioning from ads to a subscription revenue model?
2. If we launched a marketplace model, what metrics would matter most?
3. How would you track the success of adding enterprise features to a consumer product?
4. What metrics would you use to measure the success of a loyalty program?
5. How would you define success for launching in a new geographic market?
6. How would you measure the transition from a platform to a marketplace?

---

## Diagnostics (22%)

### Sudden Drops
_Immediate decreases that require expert investigation._

1. Instagram Stories are suddenly down 7% today. What do you do?
2. DAUs dropped 5% overnight. How would you investigate?
3. Conversion rates fell 20% after yesterday's product update. How do you diagnose?
4. Our mobile app's session duration decreased 15% this week. How do you investigate?
5. Revenue per user dropped 10% in the last two weeks. How do you diagnose this?

### Gradual Declines
_Persistent negative trends that require deeper analysis._

1. Monthly retention has been slowly declining over 6 months. How do you investigate?
2. Email open rates have dropped from 22% to 17% over the past year. What do you investigate first?
3. Average order value has been trending down for 2 months. What's your approach?
4. Time to first value for new users has been increasing. How do you diagnose?
5. NPS scores have been gradually declining. How do you diagnose this?

### Unexpected Changes
_Surprising positive changes or unusual patterns that need investigation._

1. A feature typically drives 20% engagement — now it's driving 50%. What do you do?
2. Our customer support tickets doubled last week with no obvious product changes. Investigate.
3. Users are spending 3x more time in a secondary feature than the main product. Why?
4. Organic traffic increased 40%, but conversions dipped flat. What's your hypothesis?
5. Our freemium-to-paid conversion rate doubled overnight. How do you investigate?
6. A geography suddenly drives completely different usage patterns. How do you diagnose?

---

## Experimentation (19%)

### A/B Test Design
_Setting up controlled experiments to test hypotheses._

1. How would you design an A/B test for a new onboarding flow?
2. We want to test a new recommendation algorithm. How do you structure the experiment?
3. How would you A/B test the impact of removing a feature?
4. Design an experiment to measure if a new checkout flow increases purchases.
5. How would you test the impact of changing our pricing display?
6. Design an A/B test for a new notification strategy.

### Measurement Strategy
_Approaches to tracking complex or long-term experimental impacts._

1. How would you measure the long-term impact of an onboarding experiment?
2. If you're testing a viral feature, what metrics matter beyond direct conversion?
3. How would you measure the network effects of a new sharing feature?
4. If testing an AI feature, what unique measurement challenges would you address?
5. How would you measure the impact of personalization on user experience?

### Statistical Rigor
_Handling edge cases, statistical challenges, ensuring reliable results._

1. How would you ensure statistical significance when testing a low-frequency event?
2. What would you do if your A/B test results show conflicting signals across metrics?
3. How do you handle seasonality when running a month-long experiment?
4. If you have test vs a small user segment, how would you approach statistical power?

---

## Metric Definition (24%)

### Engagement
_Defining how users interact with and derive value from a product._

1. How would you define a metric to measure user engagement on a social platform?
2. What metrics would you use to track the health of a community feature?
3. How would you define "active user" for a messaging platform?
4. How would you differentiate between vanity engagement and a meaningful engagement metric?
5. What metrics would you use to measure content creator engagement?

### Business Metrics
_Metrics that directly connect to company success._

1. How would you define a metric to track marketplace health?
2. What metrics would you use to measure customer expansion?
3. How would you define product-market fit with a single metric?
4. What metrics would measure the health of our freemium funnel?
5. How would you create a monetization efficiency metric?

### Technical
_Measuring performance, reliability, and technical excellence._

1. What metrics would you use to measure app performance from a user perspective?
2. How would you define an SLO for a critical API?
3. What metrics would you use to track the reliability of a real-time feature?
4. How would you measure the impact of performance improvements on business metrics?

### Dashboard Design
_Building operational dashboards and choosing key metrics to monitor._

1. What metrics would you put on a Fortnite's new season dashboard?
2. You're the PM for YouTube analytics. What 5 metrics do you include?
3. How would you build out YouTube's analytics dashboard for creators?
4. If you were designing an executive dashboard for a SaaS company, what metrics would you include?
5. Create a dashboard for monitoring the health of a mobile gaming platform?
6. What key metrics would you track on a core platform health dashboard?

---

## Trade-off Analysis (19%)

### UX vs Business
_Balancing users against drives business results._

1. If we increase ad frequency to boost revenue, how would you measure if we're hurting the user experience?
2. How would you decide between user-friendly interface vs conversion-optimized design?
3. If we prevent power users and casual users, how do you decide on designs that might frustrate one group?
4. We could increase revenue by 20% but decrease user satisfaction scores. How do you decide?

### Growth vs Quality
_Tension between growing + sustainable._

1. If we lower signup friction, churn increases, but short-term growth doubles. How do you measure success?
2. Aggressive growth tactics may reduce product quality. What metrics help you balance?
3. How would you measure if your growth strategy is sustainable?
4. We can 2x acquisition but first-time user experience will degrade. How do you decide?

### Performance vs Features
_Balancing performance vs richness._

1. If we slow the app by 50% to ship a valuable feature, how do you evaluate the trade-off?
2. How do you decide between shipping performance improvements vs new features?
3. Your team is reducing features to improve performance. What metrics prove this is correct?
4. How would you measure if feature bloat is hurting user experience?
5. If new features increase engagement but slow load times, how do you measure net impact?

---

## Drill Framing (AARM)

For every question above, work the AARM structure:
- **Acknowledge** — clarify metric, scope, time window, diagnostic vs design
- **Analyze** — build an issue tree 2-3 levels deep
- **Recommend** — where to investigate / which metrics to track
- **Measure** — specific metrics with leading + lagging + guardrail

See `frameworks.md` → AARM for the worked Instagram Stories example.

---

## Useful dashboards to memorize

For any product, be able to name:
- **1 North Star metric**
- **3-4 input metrics** (leading)
- **3-4 output metrics** (lagging)
- **2-3 guardrail metrics** (counter-metrics)
- **1 quality / customer experience metric** that doesn't get gamed

This is table stakes for a metrics round.
