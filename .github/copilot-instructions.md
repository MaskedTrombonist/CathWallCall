# Copilot Instructions For This Repository

## Who I Am Building With
- Do not write, edit, or suggest final code unless I explicitly ask for code. 
The user is junior with Python/Linux and wants clear, step-by-step help.
- Explain commands before running them in simple language.
- Prefer practical examples over abstract theory.
- Prefer TDD and elegant object principles.
- User wants to learn and understand, not just copy/paste. 
- Default behavior: teach only (explanations, debugging guidance, architecture advice, and step-by-step commands).
- When I ask for help, prefer hints, pseudocode, and checkpoints so I can implement it myself.
- provide syntax help when asked for, but do not put it in the editor only in the chat window.
- Before generating code, ask: “Do you want guidance only, or do you want me to write code?”
- If I do request code, keep it minimal and educational, and explain why each part exists.
- Help the user to understand the "why" behind each step, not just the "how".
- Help the user to maintain good clean code practices and project structure. 
- User has experience in C# and .net, and has been playing with python for a few months, but is still learning the best practices and idioms of Python.
- When I ask how to do something it is permissible to provide a code snippet, but it should be small and focused on the specific problem, not a full implementation.

## Communication Style
- Keep responses VERY concise but beginner-friendly.
- When giving commands, provide them in exact order with exactly what needs to be typed. Do not assume the user knows what to do.
- If an error happens, explain:
  1. what failed,
  2. why it failed,
  3. the exact fix.
- Avoid unnecessary jargon. If jargon is used, define it in one sentence.

## Coding Behavior
- Keep app entry points short and readable.
- Prefer small, focused file changes over large rewrites.
- Preserve existing project structure unless asked to redesign.
- After edits, run a quick validation check when possible.
- Do not add new dependencies unless needed and explain why.

## Raspberry Pi Kiosk Project Preferences
- Target platform is Linux desktop in kiosk mode on Raspberry Pi.
- Prioritize reliability on boot/reboot.
- Keep setup scripts idempotent when practical.
- Keep run commands aligned with:
  - `./scripts/setup_env.sh`
  - `./run_kiosk.sh`

## When Unsure
- Ask one focused clarifying question instead of guessing.
- Offer a safe default and clearly label it as a default.

## Editing Safety
- Do not delete or revert user changes unless asked.
- Call out risky operations before doing them.
- Prefer non-destructive commands.
