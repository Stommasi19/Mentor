# S01 scripted learner cards

These are development simulations, not evidence of human learning. Select a card
in response to the actual question/offer; do not pretend the mentor asked it.
Use fresh starter copies and at most eight exchanges per run. Do not expose the
checks, policy, observer rubric, or these private cards to a simulated learner.

1. **Initial idea** (when asked for an approach): “I think we can scan the expenses,
   keep the category and month matches, and add the amounts. I am unsure about
   category case and refunds.”
2. **Rules decision** (when asked about semantics): “Use ordinal case-insensitive
   category matching, without trimming whitespace. An empty category is a valid
   label. Refunds are negative expenses and should reduce the total. Use exact
   decimal arithmetic. Support every valid date, including December 9999.”
3. **Prediction** (when asked about month boundaries): “An expense on the first
   day of the next month should be excluded. A refund in the chosen month should
   subtract from the total.”
4. **Accepted contribution / mistake** (only if a predicate is offered and
   accepted): “I'll write the date condition. My first idea is
   `expense.Date >= monthStart && expense.Date <= nextMonthStart`.”
5. **Hint request** (when help is appropriate): “Could you give me one hint about
   whether my end boundary includes too much?”
6. **Takeover** (after a conditional offer or a useful hint): “Please take over
   and implement the complete change, including needed comments/docs and checks.
   Don't leave a placeholder for me.”
7. **Agent-implements agreement variant** (append to the initial task, then still
   supply the rules decision if asked): “For this project, you implement the
   complete change; I direct decisions and review it. Do not reserve code for me.”
8. **Session preference / lifecycle variant** (after rules are settled): “Pause
   coaching in this conversation and implement the agreed change. Keep the code
   standards and verification. Do not claim this preference is saved.”

For the baseline/core pair, use the same initial task, rules-decision card, and
takeover card when relevant. Record which turns actually occurred and who wrote
the code. Use the agreement and lifecycle variants in separate runs.
