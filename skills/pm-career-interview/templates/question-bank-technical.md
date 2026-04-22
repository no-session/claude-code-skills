# Question Bank: Technical (60 questions)

**Source:** Aakash Gupta's Technical Interview Questions Cheat Sheet (Top 60 Practice Questions).

Technical PM interviews are about demonstrating *technical credibility*, not CS PhD chops. You need to hold your own with engineers on architecture, APIs, and trade-offs. **Coding rounds are rare for PMs but common at FAANG + some infra/dev-tools companies.**

7 categories. The first 3 matter most for non-infra PM roles. The last 4 are for technical/infra/platform PM roles (Google Cloud, AWS, Stripe, Twilio, etc.).

---

## Category 1 — Eng Collab (15% of questions)

_Behavioral-flavored, but about engineering collaboration specifically._

1. Tell me about a time you worked with an engineer on a roadmap.
2. How do you work with engineers effectively?
3. What are the main mistakes PMs make when working with engineering?
4. How do you ensure that the technical team is aligned with the product vision?
5. How do you earn credibility with eng?
6. How would you handle negative user feedback about YouTube comments, and how might you address it with the engineering team?
7. What is the importance of engineers and technical teams as stakeholders?
8. How do you bring "the user" into the technical team?

---

## Category 2 — Tech Stories (18%)

_"Walk me through a technical thing you did."_

1. Explain to me the architecture of a past technical product your team built.
2. Share a technically complex problem your team had to solve. What were the components that took the most time? What solutions were considered?
3. What are the top 3 technology trends that will change the landscape in the next decade?
4. Tell me about a time you handled a difficult technical stakeholder.
5. What are the key conflicts between the development and business teams?
6. Have you designed a technical solution that then became a commercial app?
7. Talk about a technical blocker and what you did to remediate it.

---

## Category 3 — Case (15%)

_Technical troubleshooting or design cases._

1. Our app is experiencing a forever spinning circle. How can we solve it?
2. Your product is a video streaming service, and you want to save on bandwidth costs. How?
3. You have a successful website. Now you want to build a mobile version. How would you?
4. How would you decrease the amount of storage needed for messages in Gmail?
5. Design an algorithm for a self-driving car.
6. How would you diagnose a connection issue with Instagram?
7. How would you create a high-speed network to communicate with team members on Mars?
8. How much storage would offline maps take?
9. You open Uber and you don't see any available cars. What could the issue be?

**Framing:** For troubleshooting, use a classic **debug tree**: client → network → server → dependencies. For design, walk through **functional requirements → non-functional (scale, latency, reliability) → high-level architecture → trade-offs**.

---

## Category 4 — Computer Science (22%)

_Fundamentals. You don't need depth — you need to hold a conversation._

1. What happens when you type Google.com into the web browser?
2. What are the different types of load balancing algorithms?
3. How would you explain cloud computing to your grandfather?
4. How would you describe an API to a non-technical person?
5. Explain to my grandfather how the Internet works.
6. How does Google Maps compute ETA?
7. Why is Gmail search slower than Google search?
8. How do you improve response time and latency for a website?
9. How would you explain neural networks to a non-technical audience?
10. What's the best way to connect SQL databases and why?
11. How are passwords securely passed from servers to clients?
12. What are the tradeoffs of agile development?
13. Why should you use HTTPS over HTTP?
14. What is multi-threading?
15. How would you choose a programming language to build your product?
16. What are the different kinds of sorting algorithms?
17. What happens when a file is deleted?
18. What is a container?

### Fluency Checklist (must be able to explain in 60s each)

- HTTP request lifecycle (DNS → TCP → TLS → HTTP → response → render)
- API (REST vs GraphQL, auth, status codes, idempotency)
- Databases (SQL vs NoSQL, indexes, ACID, eventual consistency)
- Caching layers (CDN, browser, server-side, Redis)
- Load balancing (round robin, least connections, sticky sessions)
- Queues vs streams (SQS/RabbitMQ vs Kafka)
- Authentication (passwords → hashing, OAuth, JWT, MFA)
- Encryption (HTTPS, TLS handshake, public/private key at a high level)
- Concurrency (threads, async, race conditions)
- Containers vs VMs (Docker, Kubernetes at a conceptual level)

---

## Category 5 — System Design

_Harder than CS fundamentals. Common at Google, Meta, senior+ levels._

Classic prompts to drill:
1. Design Twitter's timeline.
2. Design Uber's dispatch system.
3. Design WhatsApp / a messaging system.
4. Design a URL shortener.
5. Design Google Drive's sync.
6. Design Instagram's feed.
7. Design a ride-sharing ETA system.
8. Design a distributed cache.
9. Design YouTube's recommendation system (high-level).
10. Design a rate limiter.

**Structure:**
1. Clarify (scale, features in scope, SLAs)
2. Define APIs (3-5 endpoints)
3. High-level diagram (client → LB → services → DB + cache + queue)
4. Deep-dive on 1-2 components
5. Trade-offs (consistency vs availability, read-heavy vs write-heavy, etc.)
6. Scale considerations (sharding, replication, caching)

---

## Category 6 — Basic Coding (10%)

_Rare for PM roles. Common at Google and specific infra-PM loops._

1. Write a program that traverses a linked list.
2. Write code to find even number of occurrences from a given list of integers.
3. Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
4. Write a function that returns how many digits are in a number.
5. How would you write a method to randomly shuffle an array of numbers?
6. What's the big-O time of Linear Sort?
7. What is the computational complexity of hash tables?
8. Write a program to find common items between two linked lists.
9. Given reverse polish notation, return the integer value of the expression: `"5,3,+,2,/"` would be `5 + 3 = 8` then `8 / 2 = 4`.
10. Write a program to find if an integer is a palindrome.
11. Write a program to reverse a string using no built-in functions.
12. Parse all lines in a CSV file with a given string.
13. Write a program to identify all equal elements between two arrays.

**Advice:** If you're prepping for a PM coding round, LeetCode Easy/Medium for arrays, strings, hash maps covers 90% of cases. You're being tested on clarity of thinking and communication, not optimal Big O.

---

## Category 7 — Product Technicalities (7%)

_Tests whether you know the technical workings of the company's product._

1. How does our product work?
2. How would you explain Twitter to an elderly person?
3. Walk me through the pain points of a developer using our API.
4. Our engineering teams use X & Y methodologies. What's your opinion? Have you used them?
5. Are you familiar with X system we use here? How have you used it?
6. We used to rely on X company for Y service; we're bringing it in-house. Would you be comfortable with this project?
7. How do you think the iPhone is machined?
8. If you had to float an iPhone in mid-air, how would you do it?
9. How would you implement the sync feature of Google Drive / Google Docs? How would you design the DB?

---

## Drill Strategy

For a non-infra PM role (consumer, B2B SaaS, marketplace):
- **Categories 1, 2, 3, 4** are table stakes. Drill the fluency checklist above.
- **Category 7** is usually company-specific — spend 2-3 hours on the target company's tech stack.
- **Skip Categories 5, 6** unless explicitly asked.

For an infra/platform/dev-tools PM role (Google Cloud, AWS, Stripe, Twilio, Vercel, Databricks):
- **All 7 categories matter.** Add system design drills weekly.
- Know your target company's architecture at a deep level (read engineering blog).
- Be able to describe at least 2 of your past products at architecture depth.
