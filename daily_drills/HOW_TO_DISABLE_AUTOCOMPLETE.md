# 🔇 How to Type With Zero Autocomplete

> The interview is a Google Doc — no autocomplete, no AI, no IntelliSense.
> Practice in the same conditions.

## ✅ Already done for you

A workspace-scoped `.vscode/settings.json` was added at the project root.
**This applies ONLY when this folder is open in VS Code.** Your other projects are unaffected.

What's now disabled in this project:

- ❌ Inline suggestions (the gray ghost text)
- ❌ GitHub Copilot
- ❌ IntelliSense popup as you type
- ❌ Trigger-character suggestions (after `.`, `(`, etc.)
- ❌ Tab completion
- ❌ Parameter hints
- ❌ Hover popups
- ❌ Word-based suggestions
- ❌ Python auto-import / function-parens completion
- ❌ Pylance language server

## 🔁 To re-enable later (after the interview)

Just delete `.vscode/settings.json` or set the values back to defaults.

## 📌 Restart VS Code after settings change

Close and reopen the project window, or run `Developer: Reload Window` from the command palette (Cmd+Shift+P).

## 🛡️ Extra safety — manually disable Copilot per session

1. Click the Copilot icon in the bottom status bar
2. "Disable Globally" or "Disable for this Workspace"

## 🧪 Verify it's off

1. Open any drill file (e.g. `01_hashmap.py`)
2. Type `import` and press space
3. **You should see NOTHING pop up.** No suggestions, no ghost text.
4. Type `seen = {}` then on next line type `s` — should NOT autocomplete to `seen`.

If anything still pops up, check for other AI extensions (Cursor, Tabnine, Codeium, etc.) — disable them per-workspace.

## 🎯 Even better — practice in Google Docs

For the absolute most realistic prep:

1. Open a new Google Doc
2. Set font to monospace (Consolas or Courier New)
3. Type the entire drill function from memory
4. Copy back to a `.py` file to run tests

This simulates the actual Amazon coding interface.
