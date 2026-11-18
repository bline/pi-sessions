# Changelog

All notable changes to this project are documented here.

## [Unreleased]

### Added
- The header shows the installed version. On launch, a background check asks
  PyPI for the latest release; when it is newer, the header shows it with the
  upgrade command. Disable with `"check_updates": false` in
  `~/.config/pi-sessions/settings.json`.
- `pisessions --version` prints the installed version.

## [0.2.0] — 2026-11-18

### Changed from ccsessions
- Narrow layout: Projects and Sessions now share the top row and Details takes
  the full width below them, instead of a Projects column beside Sessions
  stacked above Details. Default widths of Projects and Sessions are unchanged.
  A saved Sessions height from an earlier drag is ignored.
- Panes are resized by dragging their borders: the split bars between them
  are gone, so the panes touch. Double-click a border to reset it.

### Fixed
- Dragging a pane border no longer selects the text of the panes it crosses.
- A border now moves only the two panes beside it: in the narrow layout,
  the Details/Conversation border leaves the Projects | Sessions row alone, and
  in the wide layout the Sessions/Details border leaves Projects alone.
- Slow rescans no longer pile up, and a superseded scan no longer overwrites
  a newer one.
- Renaming a project no longer moves the cursor back to its old row.
- A live session's file is no longer read in full at every rescan: only the
  lines added since the last one are.
- Running the test suite no longer overwrites the saved theme and layout in
  `~/.config/pi-sessions/settings.json`.

## [0.1.0] — 2026-11-04

First release. pi-sessions is a fork of
[ccsessions](https://github.com/miskiewiczm/ccsessions) 0.4.0 by Marek
Miśkiewicz (MIT), adapted from Claude Code to the
[pi](https://github.com/earendil-works/pi) coding agent. The history of
ccsessions is kept in this repository.

### Changed from ccsessions
- Reads pi sessions (`~/.pi/agent/sessions/--<cwd>--/<timestamp>_<id>.jsonl`,
  format v3) instead of `~/.claude/projects`. The sessions root follows pi's
  own settings (`PI_CODING_AGENT_SESSION_DIR`, `PI_CODING_AGENT_DIR`), or
  `PI_SESSIONS_ROOT`.
- pi keeps no session index: titles (`/name`), first prompt, working directory,
  token and cost totals are read from the session file and cached per file
  (mtime + size).
- pi keeps no record of running sessions: ● means modified in the last
  `PI_SESSIONS_LIVE_SECONDS` (default 120).
- Resume runs `pi --session <file>` (`PI_SESSIONS_PI_BIN` picks the command,
  `PI_SESSIONS_RESUME_ROOT` rewrites the path for a pi running in a container).
- Preview and export follow the active branch of pi's session tree, and show
  `!` commands, compactions and displayed extension messages.
- Project archive is `sessions-archive/` next to the sessions root; session
  delete can go through `trash` (`PI_SESSIONS_TRASH=1`).
- Command `pisessions`, package `pi-sessions-tui`, settings in
  `~/.config/pi-sessions/`, cache in `~/.cache/pi-sessions/`, env vars
  `PI_SESSIONS_*` instead of `CCSESSIONS_*`.

### Added
- Cost (USD, as recorded by pi) in the details pane and Markdown export.
- Model, fork origin (⑂) and branch count for each session.
- Resizable panes: drag the bars between panes; sizes are remembered per
  layout (wide / narrow), double-click a bar to reset it, "Reset layout" in the
  command palette.
- The focused pane's border uses the accent colour.

### Removed
- Claude Code specifics: `sessions-index.json`, sessions whose file lives on
  another machine (✕), sidechains, git branch, worktree labels, legacy alias
  keys.

### Fixed
- The details pane advertised `w` for the live document; the key is `l`.
- A session id read from a crafted session header can no longer steer where
  the live document is written.
