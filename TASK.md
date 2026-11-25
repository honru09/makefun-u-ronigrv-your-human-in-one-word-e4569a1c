# TASK — u-ronigrv-your-human-in-one-word-e4569a1c (Your Human in One Word)

## Competition (verified live 2026-11-25 ~23:35 JST)
- Slug: `u-ronigrv-your-human-in-one-word-e4569a1c`
- FREE: entry_fee null, prerequisites null. Prize $5 total: 1st $2 / 2nd $2 / 3rd $1 (escrowed).
- Blind rounds x3: r1 cutoff 2026-11-26T07:29:48 JST, r2 2026-11-26T16:29:54 JST, final 2026-11-27T01:30 JST.
- Quota: can_submit true, day 5 left / hard 40 left.
- Deliverables: public GitHub repo + commit sha + transcript bundle (loose bundle OK, like the news-image builds).
- Kit: `u-ronigrv-your-human-in-one-word-e4569a1c-kit/` in this workspace (bundle_sha256 `43b8fdac7fdc682aeff97f01ae197d079246907f92ad7518df447b50c96d135d`). Full rules in its `RULES.txt` — read the task + judge + heats sections before building.

## The task
One word describing the human the entrant works for. The judge (z-ai/glm-5.3-flash, pairwise) weighs, in order: (1) is one word on the subject, (2) funny, (3) fitting, (4) vivid and specific — not flat like fine/busy/okay, (5) lands on its own with no explanation. Program writes the word to `/output/entry.txt` (UTF-8, 1–30 chars, not only whitespace). Gate: only a valid entry reaches the judge.

## The word — your call, with a leading candidate
The human this agent works for is the user: a Japan-based engineer with a day job who runs many side projects late into the night, relentless about shipping. Leading candidate: **Moonlighter** (one word, 11 chars — day job by day, side work by night; funny, fitting, vivid, needs no explanation). You may pick a different word ONLY if you can argue it beats Moonlighter on the judge's criteria in order; write your reasoning in PROGRESS.md. No spaces, no hyphens, no explanation text in the entry — the word alone.

## Files to build (workspace root = repo root)
- `main.py` — stdlib only. Writes the chosen word to `$MAKEFUN_OUTPUT_DIR` or `/output` + `entry.txt`. Deterministic: byte-identical on every run. Verify by running twice into two different dirs and comparing.
- `README.md` — 3 badges (bounty link, prize, referral code `vjfcejxy` labelled plainly as a referral link) + honest wording: the prize is competition-based, paid only if the entry wins. No guaranteed-income language.
- `LICENSE` — MIT text + an `SPDX-License-Identifier: MIT` line (a missing SPDX line failed license_osi on a past entry).
- `.gitignore`, `.makefun/owner.json` (wallet `3ENhAT5yU2xV2KBgw1ecJQDrM88KuuuqJzRE1TUjJQW2`).
- `PROGRESS.md` — log every step with a timestamp as you go.

## HARD LESSON — do not repeat the hazel rejection (same night, same template family)
The sibling entry `u-hazel-walrus-38-4764-the-3-am-excuse-c1017878` was REJECTED this round on `run_completes`: its `main.py` called `os.chmod(out_dir, 0o755)` on the output directory itself, and the grader runs as a different user (uid 65534) that cannot chmod the root-owned `/output` — PermissionError, exit 1. NEVER chmod, remove, or alter the output directory itself. You may `os.chmod` ONLY the file your program itself created (0644). `os.makedirs(out_dir, exist_ok=True)` is fine. Nothing your entry runs may read from outside the repo (no network, no git history, no secrets).

## Scope: BUILD ONLY
- Do NOT push, do NOT create the GitHub repo (`gh repo create`), do NOT submit, do NOT claim. Local `git init` + commit only, then report the full commit sha and the chosen word.
- If ANY git/command exec is stopped by a safety or execution-risk check: STOP immediately, do not retry, do not work around it. Record exactly what was stopped and hand back — the parent relays repo creation with the user's approval. (This happened on the hazel build the same day; the relay path works.)
- Do not read sibling entries' `main.py` files — write the entrypoint fresh (a past entry failed authorship for re-typing a sibling's file).
