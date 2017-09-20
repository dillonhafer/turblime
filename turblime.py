import sublime
import sublime_plugin

class RspecLineCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.view = self.window.active_view()
    project = self.window.folders()[0]
    path = self.view.file_name()

    for sel in self.view.sel():
      line = self.view.rowcol(sel.begin())[0] + 1

    test_command = "rspec %s:%s" % (path, line)
    command = "echo 'Running %s' ; bash -cl 'cd %s && %s'" % (test_command, project, test_command)
    self.view.window().run_command('exec', {'shell_cmd': command})

class RspecFileCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.view = self.window.active_view()
    project = self.window.folders()[0]
    path = self.view.file_name()

    test_command = "rspec %s" % path
    command = "echo 'Running %s' ; bash -cl 'cd %s && %s'" % (test_command, project, test_command)
    self.view.window().run_command('exec', {'shell_cmd': command})
