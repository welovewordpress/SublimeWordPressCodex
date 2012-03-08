# written by Matthias Krok (www.welovewordpress.de)
# based on Stackoverflow Search Plugin by Eric Martel (emartel@gmail.com / www.ericmartel.com)

# available commands
#   wordpress_codex_open_selection
#   wordpress_codex_search_selection
#   wordpress_codex_search_from_input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchWpCodexFor(text):
    url = 'http://wordpress.org/search/' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

def OpenWpFunctionReference(text):
    url = 'http://codex.wordpress.org/Function_Reference/' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class WordpressCodexOpenSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)
            OpenWpFunctionReference(text)

class WordpressCodexSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                selection = self.view.word(selection)

            text = self.view.substr(selection)            
            SearchWpCodexFor(text)

class WordpressCodexSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search WordPress Codex for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchWpCodexFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass