# turblime

Run rspec tests on the current line or current file

Example keybindings

```json
{ 
  "keys": ["\\", "t"],
  "command": "rspec_line",
  "context": [
    {"key": "setting.command_mode", "operand": true },
    {"key": "setting.is_widget", "operand": false },
    {"key": "setting.vintage_ctrl_keys" }
  ]
},
{ 
  "keys": ["\\", "T"],
  "command": "rspec_file",
  "context": [
    {"key": "setting.command_mode", "operand": true },
    {"key": "setting.is_widget", "operand": false },
    {"key": "setting.vintage_ctrl_keys" }
  ]
}
```
