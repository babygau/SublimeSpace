sublimespace_keymaps = \
[
  # Bug Found:
  # Keys not worked with `hyper`: `e`

  # Universal cancel command with `hyper`
  # Use `hyper+space` key to quit everything
  { "keys": ["ctrl+shift+alt+super+space"], "command": "_enter_normal_mode", "args": { "mode": "mode_insert" }, "context": [{ "key": "vi_insert_mode_aware" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "hide_panel", "args": { "cancel": True }, "context": [{ "key": "panel_visible" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "hide_overlay", "context": [{ "key": "overlay_visible" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "hide_popup", "context": [{ "key": "popup_visible" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "single_selection", "context": [{ "key": "num_selections", "operator": "not_equal", "operand": 1 }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "clear_fields", "context": [{ "key": "has_next_field" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "clear_fields", "context": [{ "key": "has_prev_field" }] },

  { "keys": ["ctrl+shift+alt+super+space"], "command": "power_cursor_exit", "context": [{ "key": "in_cursor_transition" }] },

  # Multiple cursor keybinding
  # Don't need to bind expand selections because
  # they can be done with native Vim visual line
  # and visual block
  # Dependencies: `PowerCursor`
  # Keybinding: `hyper+d`, `hyper+m`, `hyper+u`, `hyper+;`
  { "keys": ["ctrl+shift+alt+super+d"], "command": "find_under_expand", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["ctrl+shift+alt+super+u"], "command": "find_under_expand_skip", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["ctrl+shift+alt+super+m"], "command": "power_cursor_add", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["ctrl+shift+alt+super+;"], "command": "power_cursor_activate", "context": [{ "key": "vi_command_mode_aware" }, { "key": "in_cursor_transition" }] },

  { "keys": ["ctrl+shift+alt+super+u"], "command": "power_cursor_remove", "context": [{ "key": "vi_command_mode_aware" }, { "key": "in_cursor_transition" }] },

  # Remap `escape` to `f d`
  # in `normal-mode`, overlay, panel and popup
  { "keys": ["f", "d"], "command": "_enter_normal_mode", "args": { "mode": "mode_insert" }, "context": [{ "key": "vi_insert_mode_aware" }] },

  { "keys": ["f", "d"], "command": "_enter_normal_mode", "args": { "mode": "mode_visual_line" }, "context": [{ "key": "vi_mode_visual_line" }] },

  { "keys": ["f", "d"], "command": "_enter_normal_mode", "args": { "mode": "mode_visual" }, "context": [{ "key": "vi_mode_visual" }] },

  { "keys": ["f", "d"], "command": "hide_panel", "args": { "cancel": True }, "context": [{ "key": "panel_visible" }] },

  { "keys": ["f", "d"], "command": "hide_overlay", "context": [{ "key": "overlay_visible" }] },

  { "keys": ["f", "d"], "command": "hide_popup", "context": [{ "key": "popup_visible" }] },

  { "keys": ["f", "d"], "command": "clear_fields", "context": [{ "key": "has_next_field" }] },

  { "keys": ["f", "d"], "command": "clear_fields", "context": [{ "key": "has_prev_field" }] },

  { "keys": ["f", "d"], "command": "power_cursor_exit", "context": [{ "key": "in_cursor_transition" }] },

  # Bind `ctrl+j` and `ctrl+k` to `down` and `up` respectively
  { "keys": ["ctrl+j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [ {"key": "overlay_visible" }] },

  { "keys": ["ctrl+k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [ {"key": "overlay_visible" }] },

  # Bind `hyper+j` and `hyper+k` to `down` and `up` respectively
  { "keys": ["ctrl+shift+alt+super+j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [ {"key": "overlay_visible" }] },

  { "keys": ["ctrl+shift+alt+super+k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [ {"key": "overlay_visible" }] },

  # Unbind `space` in `normal-mode`
  # in order to make it a `prefix` keybinding
  { "keys": [" "], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }] },

  # Unbind `f` and `F` in favour of `ace-jump` plugin
  { "keys": ["f"], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["f"], "command": "noop", "context": [{ "key": "vi_mode_visual" }] },

  { "keys": ["F"], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["F"], "command": "noop", "context": [{ "key": "vi_mode_visual" }] },

  # Unbind `n` and `N` in favour of native Sublime find feature
  { "keys": ["n"], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["n"], "command": "noop", "context": [{ "key": "vi_mode_visual" }] },

  { "keys": ["N"], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["N"], "command": "noop", "context": [{ "key": "vi_mode_visual" }] },

  # Remap Sublime command palette to `space :`
  # Spacemaps alike
  { "keys": [" ", ":"], "command": "show_overlay", "args": { "overlay": "command_palette" }, "context": [{ "key": "vi_command_mode_aware" }] },
  # Favourite binding
  { "keys": [" ", " "], "command": "show_overlay", "args": { "overlay": "command_palette" }, "context": [{ "key": "vi_command_mode_aware" }] },

  # Find and replace
  # Also remap Vintageous `/`, `?`, `n`, and `N` keybinding
  # Keybinding: `space s f`, `space s F`, `space s r`, `space s R`

  { "keys": ["/"], "command": "show_panel", "args": { "panel": "find", "reverse": False }, "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["?"], "command": "show_panel", "args": { "panel": "find", "reverse": True }, "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["enter"], "command": "chain", "args": { "commands": [ ["find_next"], ["hide_panel", { "cancel": True }] ] }, "context": [{ "key": "panel", "operand": "find" }, { "key": "panel_has_focus" }] },

  { "keys": ["n"], "command": "find_next", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["N"], "command": "find_prev", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": [" ", "s"], "category": "search" },

  { "keys": [" ", "s", "f"], "command": "show_panel", "args": { "panel": "find", "reverse": False }, "context": [{ "key": "vi_command_mode_aware" }], "description": "search next" },

  { "keys": [" ", "s", "F"], "command": "show_panel", "args": { "panel": "find", "reverse": True }, "context": [{ "key": "vi_command_mode_aware" }], "description": "search previous" },

  { "keys": [" ", "s", "r"], "command": "show_panel", "args": { "panel": "replace", "reverse": False }, "context": [{ "key": "vi_command_mode_aware" }], "description": "search and replace next" },

  { "keys": [" ", "s", "R"], "command": "show_panel", "args": { "panel": "replace", "reverse": True }, "context": [{ "key": "vi_command_mode_aware" }], "description": "search and replace previous" },

  # File settings
  # Keybinding `space f`
  { "keys": [" ", "f"], "category": "file" },

  { "keys": [" ", "f", "o"], "command": "new_file", "context": [{ "key": "vi_command_mode_aware" }], "description": "open new file" },

  { "keys": [" ", "f", "O"], "command": "advanced_new_file_new", "context": [{ "key": "vi_command_mode_aware" }], "description": "open new file" },

  { "keys": [" ", "f", "f"], "command": "show_overlay", "args": { "overlay": "goto", "show_files": True }, "context": [{ "key": "vi_command_mode_aware" }], "description": "find file/buffer" },

  { "keys": [" ", "f", "d"], "command": "close", "context": [{ "key": "vi_command_mode_aware" }], "description": "delete file/buffer" },

  { "keys": [" ", "f", "K"], "command": "close_all", "context": [{ "key": "vi_command_mode_aware" }], "description": "close all files/buffers" },

  { "keys": [" ", "f", "m"], "command": "advanced_new_file_move", "context": [{ "key": "vi_command_mode_aware" }], "description": "move/rename file"},

  { "keys": [" ", "f", "n"], "command": "next_view", "context": [{ "key": "vi_command_mode_aware" }], "description": "next file/buffer" },

  { "keys": [" ", "f", "p"], "command": "prev_view", "context": [{ "key": "vi_command_mode_aware" }], "description": "previous file/buffer" },

  { "keys": [" ", "f", "s"], "command": "save", "context": [{ "key": "vi_command_mode_aware" }], "description": "save file/buffer" },

  { "keys": [" ", "f", "S"], "command": "prompt_save_as", "context": [{ "key": "vi_command_mode_aware" }], "description": "save as file/buffer" },

  # Buffer settings
  # Keybinding: `space b`
  { "keys": [" ", "b"], "category": "buffer" },

  { "keys": [" ", "b", "o"], "command": "new_file", "context": [{ "key": "vi_command_mode_aware" }], "description": "open new file/buffer" },

  { "keys": [" ", "b", "O"], "command": "advanced_new_file_new", "context": [{ "key": "vi_command_mode_aware" }], "description": "open new file/buffer" },

  { "keys": [" ", "b", "b"], "command": "show_overlay", "args": { "overlay": "goto", "show_files": True }, "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": [" ", "b", "d"], "command": "close", "context": [{ "key": "vi_command_mode_aware" }] },

  {
    # TODO: There is no official support
    # for `Close Other Tab` command yet
    "keys": [" ", "b", "k"], "command": "noop", "context": [{ "key": "vi_command_mode_aware" }], "description": "close other file/buffers"
  },

  { "keys": [" ", "b", "K"], "command": "close_all", "context": [{ "key": "vi_command_mode_aware" }], "description": "close all files/buffers"},

  { "keys": [" ", "b", "m"], "command": "advanced_new_file_move", "context": [{ "key": "vi_command_mode_aware" }], "description": "move/rename file"},

  { "keys": [" ", "b", "n"], "command": "next_view", "context": [{ "key": "vi_command_mode_aware" }], "description": "next file/buffer" },

  { "keys": [" ", "b", "p"], "command": "prev_view", "context": [{ "key": "vi_command_mode_aware" }], "description": "previous file/buffer" },

  { "keys": [" ", "b", "s"], "command": "save", "context": [{ "key": "vi_command_mode_aware" }], "description": "save file/buffer" },

  { "keys": [" ", "b", "S"], "command": "prompt_save_as", "context": [{ "key": "vi_command_mode_aware" }], "description": "save as file/buffer" },

  # Project settings
  # Dependencies: `Project Manager` plugin
  # Keybinding: `space p`
  { "keys": [" ", "p"], "category": "project" },

  { "keys": [" ", "p", "f"], "command": "show_overlay", "args": { "overlay": "goto", "show_files": True }, "context": [{ "key": "vi_command_mode_aware" }], "description": "find file" },

  { "keys": [" ", "p", "t"], "command": "focus_file_on_sidebar", "context": [{ "key": "vi_command_mode_aware" }], "description": "toggle sidebar" },

  { "keys": [" ", "p", "p"], "command": "project_manager", "args": { "action": "switch" }, "context": [{ "key": "vi_command_mode_aware" }], "description": "switch project" },

  { "keys": [" ", "p", "o"], "command": "project_manager", "args": { "action": "new" }, "context": [{ "key": "vi_command_mode_aware" }], "description": "open project" },

  { "keys": [" ", "p", "r"], "command": "project_manager", "args": { "action": "rename" }, "context": [{ "key": "vi_command_mode_aware" }], "description": "rename project" },

  { "keys": [" ", "p", "d"], "command": "project_manager", "args": { "action": "remove" }, "context": [{ "key": "vi_command_mode_aware" }], "description": "delete project" },

  { "keys": [" ", "p", "e"], "command": "project_manager", "args": { "action": "edit" }, "context": [{ "key": "vi_command_mode_aware" }], "description": "edit project" },

  { "keys": [" ", "p", "a"], "command": "project_manager_add_project", "context": [{ "key": "vi_command_mode_aware" }], "description": "add project" },

  { "keys": [" ", "p", "i"], "command": "project_manager_import_project", "context": [{ "key": "vi_command_mode_aware" }], "description": "import project" },

  # Windows settings
  # Keybinding: `space w`
  { "keys": [" ", "w"], "category": "windows" },

  { "keys": [" ", "w", "c"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "maximise window" },

  { "keys": [" ", "w", "m"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "maximise window" },

  { "keys": [" ", "w", "s"], "command": "set_layout", "args": { "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split horizontally" },

  { "keys": [" ", "w", "-"], "command": "set_layout", "args": { "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split horizontally" },

  { "keys": [" ", "w", "v"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 0.5, 1.0], "cells": [[0, 0, 1, 1], [0, 1, 1, 2]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split vertically" },

  { "keys": [" ", "w", "/"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 0.5, 1.0], "cells": [[0, 0, 1, 1], [0, 1, 1, 2]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split vertically" },

  { "keys": [" ", "0"], "command": "focus_file_on_sidebar", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus sidebar" },

  { "keys": [" ", "1"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "maximise window" },

  { "keys": [" ", "2"], "command": "set_layout", "args": { "cols": [0.0, 0.5, 1.0], "rows": [0.0, 1.0], "cells": [[0, 0, 1, 1], [1, 0, 2, 1]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split horizontally" },

  { "keys": [" ", "3"], "command": "set_layout", "args": { "cols": [0.0, 1.0], "rows": [0.0, 0.5, 1.0], "cells": [[0, 0, 1, 1], [0, 1, 1, 2]] }, "context": [{ "key": "vi_command_mode_aware" }], "description": "split vertically" },

  { "keys": [" ", "w", "h"], "command": "focus_neighboring_group", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus left panel" },

  { "keys": [" ", "w", "l"], "command": "focus_neighboring_group", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus right panel" },

  { "keys": [" ", "w", "j"], "command": "focus_neighboring_group", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus down panel" },

  { "keys": [" ", "w", "k"], "command": "focus_neighboring_group", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus up panel" },

  { "keys": [" ", "w", "t"], "command": "focus_file_on_sidebar", "context": [{ "key": "vi_command_mode_aware" }], "description": "focus sidebar" },

  { "keys": [" ", "w", "1"], "command": "focus_group", "args": { "group": 0 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 1" },

  { "keys": [" ", "w", "2"], "command": "focus_group", "args": { "group": 1 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 2" },

  { "keys": [" ", "w", "3"], "command": "focus_group", "args": { "group": 2 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 3" },

  { "keys": [" ", "w", "4"], "command": "focus_group", "args": { "group": 3 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 4" },

  { "keys": [" ", "w", "5"], "command": "focus_group", "args": { "group": 4 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 5" },

  { "keys": [" ", "w", "6"], "command": "focus_group", "args": { "group": 5 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 6" },

  { "keys": [" ", "w", "7"], "command": "focus_group", "args": { "group": 6 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 7" },

  { "keys": [" ", "w", "8"], "command": "focus_group", "args": { "group": 7 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 8" },

  { "keys": [" ", "w", "9"], "command": "focus_group", "args": { "group": 8 }, "context": [{ "key": "vi_command_mode_aware" }], "description": "focus window 9" },

  # Git settings
  # Dependencies: `GitSaavy`
  # Keybindings: `space g`
  { "keys": [" ", "g"], "category": "git"},

  { "keys": [" ", "g", "s"], "command": "gs_show_status", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "status" },

  { "keys": [" ", "g", "P"], "command": "gs_push", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "push" },

  { "keys": [" ", "g", "p"], "command": "gs_pull", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "pull" },

  { "keys": [" ", "g", "n"], "command": "gs_checkout_new_branch",  "args": {},"context": [{ "key": "vi_command_mode_aware" }], "description": "new branch" },

  { "keys": [" ", "g", "c"], "command": "gs_checkout_branch", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "checkout" },

  { "keys": [" ", "g", "l"], "command": "gs_log", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "log" },

  { "keys": [" ", "g", "f"], "command": "gs_fetch", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "fetch" },

  { "keys": [" ", "g", "a"], "command": "gs_commit", "args": { "amend": True }, "context": [{ "key": "vi_command_mode_aware" }], "description": "amend" },

  { "keys": [" ", "g", "d"], "command": "gs_diff", "args": {}, "context": [{ "key": "vi_command_mode_aware" }], "description": "diff" },

  { "keys": ["j"], "command": "gs_status_navigate_file", "args": {"forward": True}, "context": [{ "key": "setting.git_savvy.status_view" }] },

  { "keys": ["k"], "command": "gs_status_navigate_file", "args": {"forward": False}, "context": [{ "key": "setting.git_savvy.status_view" }] },

  { "keys": ["q"], "command": "close", "args": {}, "context": [{ "key": "setting.git_savvy.status_view" }] },

  { "keys": ["q"], "command": "close", "args": {}, "context": [{ "key": "setting.git_savvy.diff_view" }] },

  { "keys": ["q"], "command": "close", "args": {}, "context": [{ "key": "setting.git_savvy.inline_diff_view" }] },

  # Error settings
  # Dependencies: `SublimeLinter`
  # Keybindings: `space e`
  { "keys": [" ", "e"], "category": "errors" },

  { "keys": [" ", "e", "l"], "command": "sublimelinter_show_all_errors", "context": [{ "key": "vi_command_mode_aware" }], "description": "list lint errors" },

  { "keys": [" ", "e", "n"], "command": "sublimelinter_goto_error", "context": [{ "key": "vi_command_mode_aware" }], "description": "next lint error", "args": {"direction": "next"}},

  { "keys": [" ", "e", "p"], "command": "sublimelinter_show_all_errors", "context": [{ "key": "vi_command_mode_aware" }], "description": "prev lint error", "args": {"direction": "previous"}},

  # Side bar settings
  { "keys": ["h"], "command": "move", "args": {"by": "characters", "forward": False}, "context": [ {"key": "control", "operand": "sidebar_tree"} ] },

  { "keys": ["j"], "command": "move", "args": {"by": "lines", "forward": True}, "context": [ {"key": "control", "operand": "sidebar_tree"} ] },

  { "keys": ["k"], "command": "move", "args": {"by": "lines", "forward": False}, "context": [ {"key": "control", "operand": "sidebar_tree"} ] },

  { "keys": ["l"], "command": "move", "args": {"by": "characters", "forward": True}, "context": [ {"key": "control", "operand": "sidebar_tree"} ] },

  # Ace-Jump Plugins
  # Keybinding: `space y`, `f` and `F`
  { "keys": ["f"], "command": "ace_jump_char", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["f"], "command": "chain", "args": { "commands": [ ["ace_jump_select"], ["ace_jump_char"] ] }, "context": [{ "key": "vi_mode_visual" }] },

  { "keys": ["F"], "command": "ace_jump_word", "context": [{ "key": "vi_command_mode_aware" }] },

  { "keys": ["F"], "command": "chain", "args": { "commands": [ ["ace_jump_select"], ["ace_jump_word"] ] }, "context": [{ "key": "vi_mode_visual" }] },

  { "keys": [" ", "y"], "command": "ace_jump_line", "context": [{ "key": "vi_command_mode_aware" }] },

  # Toggle settings
  # Keybinding: `space t`
  # Dependencies: `FocusFileOnSidebar`

  # Disabled in favour of `FocusFileOnSidebar` plugin
  #{ "keys": [" ", "t", "t"], "command": "toggle_side_bar", "context": [{ "key": "vi_command_mode_aware" }] },
  { "keys": [" ", "t"], "category": "toggles" },

  { "keys": [" ", "t", "s"], "command": "toggle_status_bar", "description": "toggle statusbar" },

  { "keys": [" ", "t", "t"], "command": "focus_file_on_sidebar", "context": [{ "key": "vi_command_mode_aware" }], "description": "toggle sidebar" },

  { "keys": [" ", "t", "d"], "command": "toggle_distraction_free", "context": [{ "key": "vi_command_mode_aware" }], "description": "toggle distraction mode" },

  { "keys": [" ", "t", "m"], "command": "toggle_minimap", "args": {}, "description": "toggle minimap" },

  { "keys": [" ", "t", "l"], "command": "toggle_setting", "args": {"setting": "line_numbers"}, "description": "toggle line numbers" },

  { "keys": [" ", "t", "T"], "command": "toggle_tabs", "args": {}, "description": "toggle tabs" },
]

