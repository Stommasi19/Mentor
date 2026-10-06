# S02 observer response cards

These are scripted learner replies for a development simulation. Respond to the
actual question; do not send every card together before the workflow asks.
Preserve turns and selected cards outside the actor workspace. The spending
domain exercises requirements coaching; it is not a Mentor feature.

- If asked for boundary reasoning: “I thought June 1 could count in May because
  it closes that month. Can you help me check whether that would count it twice?
  Please give a hint or example, without editing yet.”
- After the boundary example/investigation: “I see that June 1 would also start
  June. Include May 1 and exclude June 1; use the same rule for other months.”
- If asked how refunds affect the result: “I want net spending. Negative refunds
  should reduce the total. I do not need a separate refund display in this step.”
- If asked about category matching: “Use ordinal case-insensitive matching with
  no trimming. An empty category is a valid label.”
- If asked about date range or arithmetic: “Support every valid DateOnly month,
  including December 9999, and use exact decimal amounts.”
- Once the essential rules are settled: “Please implement the agreed calculation
  completely, with useful comments, usage docs, and checks. Do not leave a
  placeholder for me.” Supply the shared `scenarios/S01/agreed-contract.md` only
  after the decisions it records have been made.

Observe whether questions follow actual uncertainty and reasoning, whether a
hint responds to the mistaken boundary idea, and whether the workflow stops once
the next step is clear. Record chosen rules and any unresolved assumptions before
running code checks. Do not infer human learning from these scripted replies.
