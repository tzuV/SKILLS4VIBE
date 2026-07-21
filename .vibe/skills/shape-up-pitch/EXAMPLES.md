# Shape Up Pitch Examples

## Example 1: To-Do Grouping Feature

Based on the example mentioned in the Shape Up book.

```
# To-Do Grouping Pitch

## Problem
Customers with many to-dos are creating workarounds by prefixing tasks with emoji to group related items. For example, they use 🛒 for shopping, 📚 for reading, etc. This makes their to-do lists hard to scan because the emoji are inconsistent and mean different things to different people. When we interviewed 5 customers, all had developed similar workarounds independently.

## Appetite
2 weeks, Small Batch

## Solution
Add optional grouping to the to-do list. Groups can be created, named, and color-coded. Tasks can be dragged into groups or assigned via a dropdown. Groups are collapsible. When viewing all to-dos, groups appear as labeled sections. When viewing a group, only tasks in that group appear.

[Fat-marker sketch showing a to-do list with 3 groups, each with a different color header]

## Rabbit holes
- Groups won't support nesting in v1 (no groups within groups)
- We'll use a simple color picker with 8 predefined colors, not a full color wheel
- Group order is manual (drag to reorder), not alphabetical

## No-gos
- No automatic grouping based on task attributes
- No sharing groups between users
- No group-level statistics or reporting
- No mobile app implementation in v1
```

---

## Example 2: Notification System Redesign

```
# Notification System Redesign Pitch

## Problem
Currently, users receive a flood of notifications with no way to prioritize or filter them. In user tests, 70% of participants said they ignore notifications entirely because there are too many. The open rate on notification emails is only 12%, suggesting users are overwhelmed.

Watch these videos: [Video 1 - User ignoring notifications], [Video 2 - User struggling to find important notification]

## Appetite
6 weeks, Big Batch

## Solution
Introduce a notification preference system with three tiers:
1. **Critical** - Must see (e.g., payment failures, security alerts)
2. **Important** - Should see (e.g., mentions, direct messages)
3. **Informational** - Nice to know (e.g., product updates, tips)

Users can set their preferred notification method (email, in-app, both, none) for each tier. Add a notification digest option for informational notifications.

[Data visualization showing current notification volume by type]
[Fat-marker sketch showing notification settings UI with 3 tiers]

## Rabbit holes
- We'll use the existing email infrastructure; no changes to email templates in v1
- Digest frequency will be daily only, not customizable
- "Critical" notifications cannot be disabled, only the delivery method can be changed

## No-gos
- No per-notification customization
- No third-party integrations (Slack, etc.)
- No notification center UI redesign (just settings)
- No historical notification management
```

---

## Example 3: Payment Form Project

Based on the example mentioned in the Shape Up book.

```
# Payment Form Project Pitch

## Problem
Small businesses using our platform need to collect payments but have no easy way to create custom payment forms. They're currently using third-party services that don't integrate with our ecosystem, leading to fragmented customer data.

## Appetite
4 weeks, Big Batch

## Solution
Create a payment form builder that allows users to:
- Create custom payment forms with their logo and brand colors
- Add fields for payment amount, description, and customer info
- Generate a shareable URL for the form
- View payment history in their dashboard

[Fat-marker sketch showing form builder interface]
[Fat-marker sketch showing what the customer sees]

## Rabbit holes
- For v1, payment forms will NOT live on custom domains. All forms will be at ourdomain.com/pay/[id]
- We'll only support Stripe as the payment processor initially
- Form design will use a simple theme system, not full CSS customization

## No-gos
- No WYSIWYG editing of the form layout
- No embedded forms (iframe or JavaScript) in v1
- No recurring payment support
- No custom payment processors beyond Stripe
```

---

## Example 4: Mobile App Onboarding

```
# Mobile App Onboarding Redesign Pitch

## Problem
New mobile app users drop off during onboarding at a rate of 40%. Analytics show they get stuck on the permissions screen where we ask for location, camera, and notification access all at once. User feedback: "I don't even know what this app does yet and it's asking for all my data."

## Appetite
3 weeks, Small Batch

## Solution
Redesign onboarding to:
1. Show value first - 3 screens demonstrating key features
2. Ask for permissions just-in-time when the feature is first used
3. Add a "skip for now" option for all permissions
4. Include a brief explanation of why each permission is needed

[Screenshots showing current onboarding flow with drop-off points]
[Fat-marker sketch showing new onboarding flow]

## Rabbit holes
- We'll use the existing permission request library, not a custom implementation
- "Just-in-time" means when the user first tries to use a feature that needs that permission
- We won't track which permissions users skipped for v1

## No-gos
- No social login integration
- No phone number verification
- No multi-step form collection
- No A/B testing framework (we'll measure success via existing analytics)
```

---

## Example 5: Search Improvement

```
# Search Improvement Pitch

## Problem
Users report that search results are often irrelevant. When searching for "invoice 2024", they get results from 2023 and 2022. When searching for customer names, they get partial matches that don't make sense. Support tickets show this is the #1 frustration with our platform.

## Appetite
2 weeks, Small Batch

## Solution
Improve search ranking by:
1. Boosting exact matches over partial matches
2. Prioritizing recent results (last 12 months) when date context is detected
3. Adding a simple filter for date ranges in the search UI
4. Surfacing "did you mean" suggestions for common typos

[Screenshot showing current poor search results]
[Fat-marker sketch showing new search UI with date filter]

## Rabbit holes
- We'll use the existing search backend (Elasticsearch) and adjust query parameters
- Date boosting will only apply when the query contains 4-digit numbers
- "Did you mean" will use a simple edit distance algorithm, not ML

## No-gos
- No full search reimplementation
- No custom ranking models
- No advanced filtering (facets, etc.)
- No search analytics dashboard
```

---

## Template for Creating Your Own Pitch

```
# [Project Name] Pitch

## Problem
[Start with a specific story or observation. Include data if available.]

## Appetite
[X weeks, Small Batch/Big Batch]
[Briefly explain why this appetite]

## Solution
[Describe the core concept in 2-3 sentences. Reference any sketches.]

[Insert fat-marker sketches here with captions]

## Rabbit holes
- [Detail 1 that might cause debate or confusion]
- [Assumption 2 that needs to be stated]
- [Technical constraint 3]

## No-gos
- [Feature or use case explicitly excluded]
- [Scope that would make this too big]
- [Integration or platform not supported in v1]
```

---

## Quick Checklist Before Finalizing

- [ ] Problem is a specific story, not vague
- [ ] Appetite is stated as a time box
- [ ] Solution is high-level but concrete
- [ ] All 5 ingredients are present
- [ ] Sketches are fat-marker style, not detailed mocks
- [ ] No-gos prevent scope creep
- [ ] Rabbit holes address potential debates
