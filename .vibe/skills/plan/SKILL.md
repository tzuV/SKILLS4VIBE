---
name: plan
description: A deep, iterative Q&A skill for single developers to define the technical stack, development process, and coding blueprint. Outputs a plan.md file (max 300 words) as a blueprint for coding agents.
---

# Technical Project Blueprint Vibe Skill

## Instructions
This skill guides **you as a solo developer** to define:
- **Technical stack** (languages, frameworks, tools)
- **Development process** (workflow, testing, deployment)
- **Coding blueprint** (architecture, modules, key functions)

The agent loops until the technical plan is clear, then compresses it into a **plan.md** (max 300 words) for coding agents to follow.

---

## Agent Behavior
1. **Iterative Clarity:** The agent asks follow-up questions until the technical approach is unambiguous.
2. **Reasoning Transparency:** For every suggestion, the agent explains its logic (e.g., "I recommend FastAPI because it’s lightweight and integrates well with Python").
3. **Blueprint Focus:** The final plan is a **coding-ready blueprint**—direct, actionable, and concise.

---

## Q&A Flow

### Phase 1: Core Technical Requirements
**Agent:** *"What is the primary function of your project? (e.g., ‘mood tracking with AI insights’)"*
**Agent Reasoning:** *"The primary function dictates the stack. For example, real-time processing might require Node.js, while data analysis might favor Python."*
**Your Answer:**

**Agent:** *"What are the non-functional requirements? (e.g., scalability, latency, compliance)"*
**Agent Reasoning:** *"Non-functional requirements influence infrastructure choices. For example, GDPR compliance might require specific hosting."*
**Your Answer:**

---

### Phase 2: Stack Selection
**Agent:** *"What language/framework do you want to use for the backend? Why?"*
**Agent Reasoning:** *"Backend choice affects everything else. For example, Python (FastAPI/Django) is great for data-heavy apps, while Go is better for high-performance services."*
**Your Answer:**

**Agent:** *"What database will you use? (SQL/NoSQL, hosted/self-managed)"*
**Agent Reasoning:** *"Database choice depends on data structure and scale. For example, PostgreSQL for relational data, Firebase for quick prototyping."*
**Your Answer:**

**Agent:** *"What tools/libraries will you use for [specific need, e.g., auth, AI, UI]?"*
**Agent Reasoning:** *"Libraries save time. For example, use `next-auth` for auth in Next.js, or `scikit-learn` for ML in Python."*
**Your Answer:**

---

### Phase 3: Development Process
**Agent:** *"What is your development workflow? (e.g., Git branches, CI/CD, testing)"*
**Agent Reasoning:** *"Workflow ensures consistency. For example, GitHub Actions for CI/CD, pytest for Python testing."*
**Your Answer:**

**Agent:** *"How will you test and validate the code? (Unit tests, integration tests, manual testing)"*
**Agent Reasoning:** *"Testing prevents bugs. For example, Jest for JavaScript, pytest for Python."*
**Your Answer:**

---

### Phase 4: Coding Blueprint
**Agent:** *"What are the core modules/components of your project? (List 3-5)"*
**Agent Reasoning:** *"Modules break the project into manageable parts. For example, a mood-tracking app might have: `auth`, `logging`, `analytics`, `ui`."*
**Your Answer:**

**Agent:** *"What are the key functions/methods for each module? (e.g., `log_mood(user, mood)`)"*
**Agent Reasoning:** *"Key functions define the blueprint. For example, `log_mood` might save data to the DB and trigger analytics."*
**Your Answer:**

**Agent:** *"What APIs/endpoints will you expose? (List routes and methods)"*
**Agent Reasoning:** *"APIs define how the frontend/backend communicate. For example, `POST /mood` to log mood, `GET /mood/history` to fetch data."*
**Your Answer:**

---

### Phase 5: Deployment and Hosting
**Agent:** *"Where will you host the backend? (e.g., AWS, Vercel, self-hosted)"*
**Agent Reasoning:** *"Hosting affects scalability and cost. For example, Vercel for frontend, AWS Lambda for serverless backend."*
**Your Answer:**

**Agent:** *"How will you deploy updates? (Manual, automated, blue-green)"*
**Agent Reasoning:** *"Automated deployments (e.g., GitHub Actions) save time and reduce errors."*
**Your Answer:**

---

## Compression to plan.md
After alignment, the agent compresses all answers into this **300-word max template** for **plan.md**:

```markdown
# [Project Name] - Technical Blueprint

**Primary Function:** [Function] — [Non-functional requirements].

**Stack:**
- Backend: [Language/Framework] (e.g., Python/FastAPI)
- Database: [DB] (e.g., PostgreSQL)
- Libraries: [List] (e.g., `next-auth`, `scikit-learn`)
- Hosting: [Provider] (e.g., AWS, Vercel)

**Workflow:** [Workflow] (e.g., GitHub + CI/CD). Tests: [Testing tools].

**Blueprint:**
- Modules: [List] (e.g., `auth`, `logging`)
- Key Functions: [List] (e.g., `log_mood(user, mood)`)
- APIs: [Routes] (e.g., `POST /mood`)

**Deployment:** [Method] (e.g., GitHub Actions to AWS).

**Next:** [Action 1], [Action 2].
```

---

## Example Compressed Plan
```markdown
# MoodTrack - Technical Blueprint

**Primary Function:** Daily mood logging + AI insights — GDPR-compliant, scalable to 1K users.

**Stack:**
- Backend: Python/FastAPI
- Database: PostgreSQL (hosted on Supabase)
- Libraries: `fastapi-users` (auth), `scikit-learn` (AI)
- Hosting: Backend on Render, Frontend on Vercel

**Workflow:** GitHub + GitHub Actions. Tests: pytest, Playwright.

**Blueprint:**
- Modules: `auth`, `logging`, `analytics`, `ui`
- Key Functions: `log_mood(user, mood)`, `generate_insight(user)`
- APIs: `POST /mood`, `GET /mood/history`, `GET /insights`

**Deployment:** Auto-deploy on `git push` to main.

**Next:** Set up Supabase, scaffold FastAPI project.
```

---

**Note:** The agent will not finalize the plan until the blueprint is clear, actionable, and under 300 words.