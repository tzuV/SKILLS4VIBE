# Shape Up Pitch - Full Reference

Based on Chapter 6: Write the Pitch from Shape Up by Basecamp

## Purpose of a Pitch

The pitch presents a **good potential bet**. It's a presentation that captures work done so far and presents it in a form that enables people who schedule projects to make an informed bet.

A pitch is **not**:
- A specification document
- A research brief
- A list of requirements

A pitch **is**:
- A shaped piece of work ready for betting
- A communication tool for stakeholders
- A boundary-setting device

## The Five Ingredients (Deep Dive)

### 1. Problem

**Why it matters:** Without a problem, there's no basis for discussing whether a solution is good or bad. Jumping straight to "what to build" leads to endless debates about preferences rather than fitness for purpose.

**What to include:**
- A single specific story that shows why the status quo doesn't work
- Concrete examples from real customer behavior
- The impact of the current situation

**Example:**
> "Customers with long to-do lists are creating workarounds by using emoji prefixes to group related tasks together. This makes their lists hard to scan and the emoji mean different things to different people."

**Avoid:**
- Vague statements like "users find it hard to organize"
- Feature requests without context
- Assumptions without evidence

### 2. Appetite

**Why it matters:** Not only do we want to solve this use case, we want to do it within a specific time constraint. Stating the appetite prevents unproductive conversations about "better" solutions that don't fit the time box.

**What to include:**
- Time box: "2 weeks", "6 weeks", "small batch", "big batch"
- What this means for the scope
- Why this appetite was chosen

**Example:**
> "Appetite: 2 week small batch. This fits our cycle and forces us to find the simplest solution that works."

**Key insight:** Anybody can suggest expensive, complicated solutions. It takes work and design insight to get to a simple idea that fits in a small time box.

### 3. Solution

**Why it matters:** A problem without a solution is unshaped work. Pushing research and exploration down to the team level misaligns skillsets, time limits, and risk profiles.

**What to include:**
- Core elements of the solution
- Presented at a level that's easy to understand immediately
- High-level enough to allow design flexibility
- Concrete enough to evaluate fitness

**Avoid:**
- Detailed specifications
- Wireframes or high-fidelity mocks
- Technology choices (unless critical)
- Edge cases and rabbit holes (those go in ingredient 4)

### 4. Rabbit Holes

**Why it matters:** Some details aren't central to the concept but are worth calling out explicitly to avoid problems, debates, or wrong assumptions.

**What to include:**
- Technical constraints
- Design decisions that might be questioned
- Assumptions being made
- Known limitations of the approach

**Example:**
> "For v1, custom domains won't be supported. All payment forms will live at ourdomain.com/pay/[id]."

### 5. No-Gos

**Why it matters:** Explicitly stating what's NOT included prevents scope creep and makes the appetite constraint real.

**What to include:**
- Functionality intentionally excluded
- Use cases not being addressed
- Features that would be "nice to have"

**Example:**
> "No WYSIWYG editing. Users can only provide a logo and customize header text on a separate page."

## Visual Communication

### Fat-Marker Sketches

**When to use:** When ideas are inherently visual or too complicated for a schematic breadboard.

**How to create:**
- Use a fat brush/pen (physical or digital)
- Draw at a level of abstraction that shows the concept without over-specifying
- Keep lines thick to avoid detail

**Digital tools:** iPad with Notability, Procreate, or any drawing app with adjustable brush size.

### Embedded Sketches

**When to use:** When showing where new elements fit into existing interfaces.

**Technique:**
- Show the existing interface
- Add new elements with just enough detail to communicate placement
- Use a disclaimer: "Designers should feel free to explore other approaches"

### Annotated Sketches

**When to use:** When specific elements need explanation.

**Technique:**
- Use different colors for labels vs. the sketch itself
- Add call-outs with brief explanations
- Number elements for reference in the pitch text

## Presentation Format

### Asynchronous First

1. Post the pitch document where stakeholders can read it on their own time
2. Allow time for people to digest and comment
3. Comments should poke holes or contribute missing information, NOT vote yes/no

### Live Presentation

Only when necessary. If live:
- Keep it short (15 minutes max)
- Focus on the ingredients, not the document
- Be prepared to answer questions about trade-offs

### Basecamp's Approach

- Pitches posted as Messages in Basecamp
- Message Category called "Pitch" for easy filtering
- Posted to a Team called "Product Strategy" accessible by betting table members
- Sketches drawn on iPad and inserted as images
- Images captioned so they make sense in context

## Example Pitch Structure

```
# [Project Name] Pitch

## Problem
[Tell a specific story. Show, don't just tell.]

## Appetite
[X weeks, Small Batch/Big Batch]

## Solution
[High-level description with supporting sketches]

## Rabbit Holes
- [Detail 1 that could cause debate]
- [Assumption 2 that needs clarification]

## No-Gos
- [Feature A explicitly out of scope]
- [Use case B not addressed]
```

## Common Anti-Patterns

### The Solution Pitch
Pitch starts with "We should build X" without explaining why. Push back: "What problem does this solve?"

### The Research Brief
Pitch describes a problem area but has no solution. Response: "This needs more shaping work before it's ready to pitch."

### The Specification
Pitch includes detailed UI designs, database schemas, or API specs. Response: "This is overspecified. Let's pull back to the core concept."

### The Unconstrained Pitch
Pitch describes a solution without any time constraint. Response: "What appetite do you have in mind? This will help us evaluate if the solution fits."

### The Everything Pitch
Pitch tries to solve multiple problems at once. Response: "Can we split this into separate pitches? Each should have a clear, singular focus."

## Questions to Ask When Shaping a Pitch

1. **Is the problem specific enough?** Can you tell a story about a real person with a real need?
2. **Does the solution actually solve the problem?** Would the story have a better outcome with this solution?
3. **Does the solution fit the appetite?** Could this really be built in the stated time?
4. **Are there obvious rabbit holes?** What debates might come up that we should address preemptively?
5. **What's out of scope?** What would make this too big for the appetite?

## When a Pitch is Ready

A pitch is ready to present when:
- ✅ All 5 ingredients are present
- ✅ Problem is specific and compelling
- ✅ Solution is clear and fits the appetite
- ✅ Rabbit holes that could derail the project are addressed
- ✅ No-gos are explicit
- ✅ Visual aids help understanding without overspecifying

## After the Pitch

The next step is the **betting table** where pitches are evaluated and turned into scheduled projects. See the betting process for more details.
