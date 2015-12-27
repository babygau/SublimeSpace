import os
import sublime
import sublime_plugin
from .helpers import keymaps

class SublimeSpaceCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    keymaps.get_keymaps()
    sublime.status_message('Open SublimeSpace Panel')
