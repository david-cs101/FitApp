# Feature: peso-y-nutricion

## Objective
Add two new views to FitPlan, reachable from the header like the existing "Histórico" view:
1. **Peso** — body-weight log (fasted, same time), trend chart, weekly averages and bulking progress.
2. **Comida** — nutrition recommendations for David (lean bulk), acting as a personal trainer/nutritionist.

## Why
David is on a lean-bulk plan agreed in a previous session (2026-09-23): ~2,900 kcal, 150 g protein, 85 g fat, ~385 g carbs; creatine 3–5 g/day, optional whey. Adjustments depend on the weekly average body weight, which the app does not track yet.

## Scope / constraints
- Single-file PWA (`index.html`), data stored in localStorage + `/api/save` (`data.json`).
- New persisted key `fit_body`: `[{date:'YYYY-MM-DD', kg, note}]`, one entry per date.
- Food preferences: no tomato, no bell pepper.
- Bump service worker cache so the new version reaches the phone.
- Route: direct inline (one non-trivial file, already understood). TDD: off (no test runner in project); checks = manual render in browser.

## Tasks
- [ ] T1 — Header navigation (Plan / Histórico / Peso / Comida) + Peso view (log, SVG trend chart, weekly averages, coach adjustment hint)
- [ ] T2 — Comida view (targets, meal plan with swaps, supplements, rules) + SW cache bump

## Acceptance criteria
- Peso: add/replace today's weight, delete entries, chart renders with ≥2 entries, weekly average and weekly delta shown, recommendation follows rules: <+0.1 kg/week for 2 weeks → +150–200 kcal; >+0.5 kg/week → −150 kcal.
- Comida: targets scale with latest body weight (protein 2.2 g/kg); menu excludes tomato/pepper.
- Existing plan and history views keep working; data persists after reload.

## Progress / evidence
- (pending)
