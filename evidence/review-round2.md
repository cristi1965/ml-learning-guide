# Independent blind final regression review — round 2

No prior review reports were read. No production files were modified.

## Scope and outcome

No critical mathematical or browser-lab execution blocker found in this bounded review. Reviewed all 48 lesson example/quiz-answer/lab-solution summaries; examined detailed prerequisite bridges and teaching walks in lesson IDs 1, 5, 9, 10, 12, 13, 21, 25, 33, 34, 36, 40, 44, 47. This is representative pedagogical review, not verification of all 158 upstream files or full model training.

- Executed all 48 reference solutions against their supplied tests with local Python: 48 passed. This confirms internal consistency only, not test exhaustiveness.
- Live Chromium/Playwright at http://127.0.0.1:8771/course.html: lesson 1 starter correctly failed with AssertionError; reference answer passed and was explicitly marked assisted, not independently completed. Navigated to lesson 41 (ID 40) and executed its stable-softmax reference successfully in the actual browser Python runtime.
- Screenshot: `evidence/review-round2-browser.png` (full-page capture after attention exercise).
- Initial shell Node 14 could not run Playwright; switched to bundled modern Node and browser checks completed.

## Observations

1. **Closed after targeted verification, lesson 45 (ID 44), curriculum/models.json.** The lab now accepts integer or one-hot targets and includes equivalence checks for [0,1] and [1,0]. Inspected the implementation and clarified hint, executed the revised reference/tests locally, then independently loaded the rebuilt live page and ran this lesson in browser Python: all checks passed. No remaining finding on this item.
2. Intro gradient lesson explicitly defers derivative derivation and distinguishes full squared loss from the source half-MSE convention. Later gradient lesson consistently uses half-MSE; no factor-of-two contradiction found.
3. Intro CNN/ResNet, attention, and Transformer introduce multiple concepts quickly, but walkthroughs explicitly bridge local windows → residuals and weighted sum → query/key/value → causal masking. Appropriate for an overview route; not equivalent to independent implementation mastery.
4. Advanced labs explicitly state standard-library teaching calculations rather than full PyTorch/TensorFlow training. Adam is scoped to its first step and warns that actual multi-step optimization must retain moments. LayerNorm/dropout and convolution/pooling are distinguished correctly. Completion lesson explicitly separates the browser calculation from full MNIST reproduction.

## Checked file SHA-256

| File | SHA-256 |
|---|---|
| `curriculum/intro.json` | `535431654e831d4f754da7d251b8bc67e1c5bb5d75660c4df62b485c50dd4bbd` |
| `curriculum/foundations.json` | `55f15e4988510a8df063b59f7c0202f8ee1859e194ef35b8019ed35f5bedb8ce` |
| `curriculum/models.json` | `25bbc7be778afdffe120a04980b312c9c3745edb4ce67ff315e7197f80868438` |
| `content.js` | `368413f2879a65c31e72e763658b38e209b2a8419fd01177ee9c7b1e6a191792` |
| `app.js` | `f5cbf079e3f55f34a569946d7769d0e51d116b59ee872cd13ebfc97944f121c6` |
| `lab-ui.js` | `4ffcce7376517405222d2a9beec014e11095e3d5b596dcdde40d41cc76513300` |

Hashes refreshed after the targeted lesson 45 closure check; no broad re-review performed.
