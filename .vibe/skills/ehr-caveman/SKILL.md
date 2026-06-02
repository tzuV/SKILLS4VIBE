---
name: ehr-caveman
description: >
  Ultra-compressed EHR mode. Cuts token usage ~70% by stripping redundant
  boilerplate, repeated vitals, and template fluff while keeping full clinical
  accuracy. Use when user provides EHR text, medical records, or says
  "ehr-caveman", "compress EHR", "token-efficient summary", "condense medical notes".
---

Transform EHR into dense clinical summary. All medical facts stay. Only fluff die.

## Persistence

ACTIVE FOR CURRENT EHR once triggered. No revert mid-document. No boilerplate drift.
Still active if unsure. Off only when user says "stop", "full text", or "normal mode".

## Rules

Drop: redundant patient IDs (keep 1x), repeated vitals (keep latest/abnormal),
boilerplate headers/footers, template text ("Patient is a X-year-old..."),
standard disclaimers, signature blocks, repetition of allergies/meds across sections,
normal findings in ROS ("No chest pain, no SOB" -> "ROS: non-contributory"),
connective phrases ("noted to have", "found to be"), hedging ("appears to be").

Keep: all abnormal findings, active problems, meds with doses, relevant history,
vital trends (not individual normal readings), allergy specifics, lab values outside
reference range, imaging findings, procedure details, assessment/plan.

Use: medical abbreviations (HTN/DM/HLD/COPD), standard symbols (↑↓→),
minimal punctuation. Fragments OK. Short forms (CBG not "capillary blood glucose",
BP not "blood pressure"). Group by domain (HPI, PMH, Meds, Labs, Assessment, Plan).

Pattern: `[problem] [status] [trend] [intervention].`

### Before
> "The patient is a 65-year-old male with a history of hypertension, type 2
> diabetes mellitus, and hyperlipidemia who presents today with complaints
> of chest discomfort. The patient denies any shortness of breath, nausea, or
> vomiting. On examination, blood pressure is 130/80 mmHg, heart rate is 72
> bpm and regular, respiratory rate is 16 breaths per minute..."

### After
> 65M. PMH: HTN, DM2, HLD. CC: chest discomfort. ROS: (-) SOB/N/V. VS: 130/80, 72, 16.

## Auto-Clarity Exception

Drop compression temporarily for: critical lab values requiring full context,
discharge instructions, medication changes with complex dosing, surgical
procedures, patient safety warnings. Resume compression after clear part done.

### Example
> **CRITICAL:** K+ 6.8 mEq/L (ref 3.5-5.0). ECG: peaked T-waves. Hold spironolactone.
> Compression resume. Trend: ↑ from 5.2 yesterday. Nephrology consulted.

## Domain-Specific Compression

### History & Physical
- Collapse redundant HPI sentences -> timeline
- PMH: list conditions, omit "history of" prefix
- ROS: summarize as (-) or (+) by system
- Exam: only abnormal findings

### Labs
- Normal: omit or "WNL"
- Abnormal: value (reference) trend
- Example: "Na 128 (135-145) ↓ from 132"

### Medications
- Group by class
- Keep: name, dose, frequency, route
- Drop: "take as directed", "as needed for", standard instructions
- Example: "Meds: lisinopril 10mg daily, metformin 500mg BID, atorvastatin 20mg HS"

### Assessment & Plan
- Remove: "The patient has", "I recommend", "We will"
- Keep: problem list, action items
- Example: "A&P: HTN - continue current regimen. DM2 - A1c 8.2, increase metformin."

## Language Support

Core rules work for **ANY language EHR**. Only adapt:

- **Abbreviations**: Use local equivalents (HTN→Hypertoni, DM2→Type 2 diabetes, COPD→KOL)
- **Section names**: Map to local terms (PMH=Prævious sygdomme, Meds=Medicin, ROS=Relevante symptomer)
- **Examples**: Translate before/after pairs to local language
- **Symbols**: Keep ↑↓→ (universal)

Compression triggers and persistence: same for all languages.
