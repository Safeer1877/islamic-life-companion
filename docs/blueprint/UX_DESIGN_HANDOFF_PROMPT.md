# Design handoff prompt — to use after the blueprint is reviewed

Read `LOCAL_FIRST_ZERO_OPEN_POLICY_v1.1.md` **first**, then read `PRODUCT_BLUEPRINT_v1.md` **entirely** and use `SCREEN_REGISTER_v1.csv` as the authoritative screen index. Do not design from this prompt alone.

The product is **free for the user, local-first, fully functional without AI, and designed to minimize unnecessary app opens**. Treat the v1.1 policy as authoritative if earlier language conflicts. A typical successful day may have zero app launches and zero notifications.

Act as a principal mobile product designer and accessibility reviewer, supported by a senior UX writer and Islamic-content safety reviewer. Your task is to turn the **already adopted blueprint** into a coherent, beautiful, calm screen-by-screen experience. Do not change the four top-level areas, turn the product into a prayer tracker, add engagement scoring, or invent religious rulings.

## Deliverables, in this order

0. **Zero-open storyboard**: diagram setup → quiet normal day → one consented lock-screen cue → unexpected change → later optional return. Also show no-permission, offline and no-AI paths. Demonstrate the useful result without requiring the Today screen to be visited.
1. A flow-linked low-fidelity wireframe set for **S01–S03, S08–S20, S25, S34–S40, S48–S52, S61–S66, S71–S81**, including empty, loading, offline, denied-permission and no-action states.
2. A concise component library covering prayer windows vs Iqamah events, real/flexible commitments, protected periods, suggestion cards with provenance, approval-before-change, no-feasible-option, source verification, three assistance modes and corrections to personal understanding.
3. A high-fidelity visual direction in light and dark mode using the proposed palette as a starting point (not a rigid brand commitment), with excellent typography and restrained Islamic visual references.
4. Smartphone and tablet adaptations, accessibility and right-to-left/Urdu/Arabic examples.
5. Five task walkthroughs: private onboarding; prayer/congregation with stale data; rescheduling a voluntary intention after an interruption; a night-shift worker protecting sleep; switching to on-demand/silent mode.
6. A view-by-view traceability checklist mapping design output to each screen ID and the criteria in blueprint §§24–26.

## Design constraints

- Design the **purpose of each screen**, not an attractive but generic dashboard.
- Make the minimum amount of content visually dominant. Empty time is acceptable; don't fill it with banners.
- Use one meaningful primary action per focused view and obvious back/escape routes.
- Never imply worship, piety, family care or character has a score or streak.
- Preserve separate labels for prayer window, congregation/Iqamah, user preference, estimated travel time and unverified facts.
- No quiet-mode violations, coercive notifications, account gate, surprise location prompt or forced personal religious disclosure.
- No paid AI dependency, mandatory chatbot, daily app-open nudges, gamified retention prompts or paywalled core feature.
- A reminder must be useful standalone where possible, with a source and freshness check for religious/mosque timing data; do not promise unsupported OS background behavior.
- Local-only data works without network; permission denial preserves the manual alternative.
- Any religiously consequential wording is marked **Pending Scholar Review** until cleared.
- Do not make up mosque data, user studies or platform permissions.
- Present negative cases and failure states as rigorously as happy paths.

## Review before polishing

First provide two visual directions and compare them against the product principles. Choose one direction with reasons, then design the selected screens, keeping their IDs. Flag any conflict or underspecified detail in the blueprint, propose the smallest correction, and continue. Do not ask to redesign the product concept or produce another market-research report.