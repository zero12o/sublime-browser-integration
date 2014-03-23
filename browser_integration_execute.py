from .browser_integration import *


class BrowserIntegrationExecuteCommand(sublime_plugin.TextCommand):
    plugin_name = "Execute selected code"
    plugin_description = "Executes selected JavaScript code in the browser."

    @require_browser
    @async
    def run(self, edit):
        for region in self.view.sel():
            if region.empty():
                continue

            s = self.view.substr(region)
            status("Executing `%s`" % s)
            result = browser.execute(s)

            if result is not None:
                view = sublime.active_window().new_file()
                view.set_syntax_file(
                    "Packages/JavaScript/JavaScript.tmLanguage")
                view.run_command("insert_into_view", {"text": str(result)})