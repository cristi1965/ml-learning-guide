# Independent review round 1

Date: 2026-10-10. Reviewed current 48-lesson expansion against curriculum/PLAN.md. No other review reports read. No application changes made.

## Findings requiring changes

1. **P1 — Reset forgets reference assistance** (`lab-ui.js:15`). Actual mobile Chromium reproduction: load reference answer → run → `参考答案辅助通过（不计独立完成）`; reset starter → paste the exact answer just seen → run → `当前练习已独立通过检查`. The same answer and learner are relabeled independent because reset clears `referenceSeen`. Keep reference exposure persistent for that exercise/version. If a fresh assessment is desired, supply a different transfer task rather than clearing history.

2. **P2 — LayerNorm checker accepts no normalized values** (`curriculum/models.json:333`, lesson 35). The first assertion uses `all(... zip(...))` without asserting output length. Executed this wrong implementation against the actual tests and it passed:
   ```python
   def normalize(values, eps=1e-5):
       return [0,0] if values[0]==values[1] else []
   ```
   Assert matching shape before approximate element comparison; include a three-element nonconstant input. This is a specific false-positive check, not merely a request for exhaustive tests.

3. **P2 — Reproducibility capstone does not check its central outputs** (`curriculum/models.json:1849`, lesson 48). Executed the following and both assertions passed:
   ```python
   def report(labels, predictions, seed):
       return {'order': [], 'data_hash': str(labels),
               'accuracy': sum(a==b for a,b in zip(labels,predictions))/len(labels)}
   ```
   It ignores the seed, never returns a permutation, and returns raw data rather than a SHA256 fingerprint. Validate permutation contents/length, expected seeded order for selected examples, and a known SHA256 digest. Keep claims limited to the supplied toy data: no held-out provenance can be proven by this function alone.

4. **P2 — Neuron gradient tests never exercise weights or bias** (`curriculum/models.json:109`, lesson 33). Both tests use `w=b=0`, so an implementation assuming sigmoid output is always 0.5 passes:
   ```python
   def gradients(x,w,b,y):
       return 2*(.5-y)*.25*x, 2*(.5-y)*.25
   ```
   Add at least one nonzero logit and preferably compare with a finite-difference gradient. This directly checks the lesson's forward→chain-rule dependency.

## Evidence and limits

Read the lab definitions across intro/foundations/models and implementation in runner.js, lab-ui.js, app.js, and editor-src/editor.js. Reference formulas sampled in the new lessons were consistent with their stated simplified boundaries; this is not an exhaustive audit of every upstream training file.

Actual browser: headless Chromium, http://127.0.0.1:8771, 390×844. Displayed lesson 1/48 and 48 catalog buttons, no page errors in the tested route. Followed first lesson walkthrough, performed a Python exercise through visible controls, and verified assisted→reset→independent misclassification with real Pyodide execution. Screenshot: `evidence/review-round1-mobile.png`. No claim of human learner evaluation or physical-device testing.

Small wrong-implementation probes ran with local Python against the exact curriculum tests. The global progress text correctly says “小测通过”; no conflation with Python completion found there. Mobile full catalog was reachable. Existing 16-lesson intro scope is presented separately from all 48 lessons; no stale 16-total count observed.

## SHA256 of inspected assets

Hashes taken before the browser run; later author edits are outside this review snapshot.

| Asset | SHA256 |
|---|---|
| curriculum/intro.json | 535431654e831d4f754da7d251b8bc67e1c5bb5d75660c4df62b485c50dd4bbd |
| curriculum/foundations.json | 55f15e4988510a8df063b59f7c0202f8ee1859e194ef35b8019ed35f5bedb8ce |
| curriculum/models.json | f84d291f4282ae13b42cf9fbd01f9b2720adeceb7850a8ddfa7b036299c86445 |
| runner.js | bf76d215546d627caedfed29d5407b19d119c5f308e0f133f00a7a25c69824f5 |
| lab-ui.js | 9d564b74153faad073a7318a984b65d1aa2de8f917ad40cffbbfc1ca325db33e |
| app.js | 05f91051f7b39b009e62fdbd8182bc0266364f6161118c6bfefc63dded508f63 |
| content.js | 44512b2da35b9a963ad6668ca4864d6c255528ecf1cf646d6ded30ab34bc2762 |
| index.html | b3facdc81e74ef06f505f5a53337af485090a396570cb0ceead47dcf1580d540 |
| editor-src/editor.js | 838143fc058e490d98f95dc67762dab54dffa7da37735ab1df1b762ed0c2b3ae |

## Closure verification after author fixes

Findings 1, 2, and 3 are **closed**. Repeated the real mobile Chromium walkthrough → starter failure → reference success → reset → paste → rerun sequence: result remained `参考答案辅助通过（不计独立完成）`. Wrong LayerNorm and capstone implementations above now fail the revised assertions; both reference implementations pass. Finding 4 remains open at this snapshot. No exam anti-cheat guarantee is requested; these are self-study feedback accuracy issues.

Reverified snapshot hashes:

| Asset | SHA256 |
|---|---|
| curriculum/intro.json | 535431654e831d4f754da7d251b8bc67e1c5bb5d75660c4df62b485c50dd4bbd |
| curriculum/foundations.json | 55f15e4988510a8df063b59f7c0202f8ee1859e194ef35b8019ed35f5bedb8ce |
| curriculum/models.json | 1bcf6f315a98a7b94dab5bf0a19b8d19d445a5932fa7f98b8f82c2ab261282ec |
| runner.js | bf76d215546d627caedfed29d5407b19d119c5f308e0f133f00a7a25c69824f5 |
| lab-ui.js | 17175cc061bc500200b9f14bace23bbb2bf18fabce6d9971d5223eb66427e673 |
| app.js | 05f91051f7b39b009e62fdbd8182bc0266364f6161118c6bfefc63dded508f63 |
| content.js | f2301044626a55a8c996926c075e75327409d2be0419e3f43b9af546b4bdb475 |
| index.html | b3facdc81e74ef06f505f5a53337af485090a396570cb0ceead47dcf1580d540 |
| editor-src/editor.js | 838143fc058e490d98f95dc67762dab54dffa7da37735ab1df1b762ed0c2b3ae |

### Final closure

Finding 4 is also **closed**: the added nonzero-logit finite-difference assertions reject the constant-p=0.5 implementation, while the reference passes. All four reported findings are closed; no outstanding blocker from this bounded review.

Final inspected changed assets:

| Asset | SHA256 |
|---|---|
| curriculum/models.json | a78d2907ee7790a0d29b23728270d8776887c79f88904420a78d279e6ed46832 |
| content.js | eec1a7b0a3be500891c30df6eed0b9f85c7167659c9c3331cc00749b43f14285 |
| course.html | c4ad1c9d491fd86d2b8d38fca5aff37bf332019f56e5392f12b580a0a1050ab7 |
| lab-ui.js | 4ffcce7376517405222d2a9beec014e11095e3d5b596dcdde40d41cc76513300 |
