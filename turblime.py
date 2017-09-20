import sublime
import sublime_plugin

def echo_command(working_dir, command):
  s = "echo 'Running %s' ; bash -cl 'cd %s && %s'" % (command, working_dir, command)
  return s

def rspec_command(self, line=False):
  view = self.window.active_view()
  project = self.window.folders()[0]
  path = self.window.active_view().file_name()

  if line == False:
    test_command = "rspec %s" % path
  else:
    for sel in view.sel():
      line = view.rowcol(sel.begin())[0] + 1
    test_command = "rspec %s:%s" % (path, line)

  return echo_command(project, test_command)

class RspecLineCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.active_view().window().run_command('exec', {'shell_cmd': rspec_command(self, True)})

class RspecFileCommand(sublime_plugin.WindowCommand):
  def run(self):
    self.window.active_view().window().run_command('exec', {'shell_cmd': rspec_command(self)})
