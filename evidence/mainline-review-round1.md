# Mainline independent review round 1
Read-only agent mainline_review_one examined new lesson content and experiment implementation.
Found and corrected:
- Attention positions used 0-based content but 1-based controls. Unified 0..3, inclusive causal slice.
- Candidate vector length experiment was impossible. Added east-candidate length slider 1..2.
- Missing fact versus missing JSON field labels conflated. Explicit labels now distinguish complete fields with unknown date, missing fields, malformed syntax, and invented date.
Other reviewed numerical mechanisms and quiz answers: no reported blocker. Static content review only; browser evidence recorded separately. Not a human learning study.
