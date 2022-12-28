# Script documentation
## Functions
All functions are written in **upper cases** and begin with the `^` character.

### ^OPTS
The function responsible for configuring the script settings.
Allows you to set the operating system type, language (alphabet)
used in the script, and keyboard layout. <br>
If a function is not set, the program will set the default value.
If a non-existent option or its value is selected, the program will
return an error. <br>
**The `^OPTS` function is read only once, any subsequent calls to
it will be ignored by the descriptor.** <br>
Capitalization does not matter.
#### Options available to choose:
- `OS`: `WINDOWS`, `LINUX`, `MAC`
- `LANG`: `US`, `UK`, `ES`, `DE`, `FR`
- `LAYOUT`: `US`, `UK`, `ES`, `DE`, `FR`
#### Default settings
`^OPTS OS=WINDOWS;LANG=us;LAYOUT=us`
#### Syntax
`^OPTS <opt=value>;<opt=value>;<opt=value>`
#### Example
`^OPTS OS=Mac;LANG=us;LAYOUT=us` &larr; correct selection of all options<br>
`^OPTS LANG=de` &larr; only the language is set, the rest is default <br>
`^OPTS` &larr; default settings
```
^OPTS OS=WINDOWS;LANG=de;LAYOUT=de
^OPTS LANG=us;LAYOUT=us     This line will be ignored
```

---

### ^COM
This is a comment. Lines with this function are ignored by the descriptor.
#### Syntax
`^COM <comment>`
#### Example
`^COM This is my comment. I can write everything here!`

---

### ^END
Script completion function. After its execution, the program immediately
terminates its work. The lines below will no longer be executed.
#### Syntax
`^END`
#### Example
```
^END
This line will be ignored.
```

---

### ^WAIT
Pause function. The pause lasts for a certain amount of time.
Crawl time is read in seconds. It can be specified as an integer or
a floating type.
#### Syntax
`^WAIT <time>`
#### Example
`^WAIT 5` &larr; the script will pause for 5 seconds <br>
`^WAIT 0.5` &larr; the script will pause for 0.5 seconds <br>
`^WAIT 0.02` &larr; the script will pause for 20 milliseconds <br>

---

### ^KEY
This function allows to press a single key from the keyboard.<br>
Capitalization does not matter of the key name.
#### Syntax
`^KEY <key_name>` <br>
`^KEY <single_letter>`
#### Example
`^KEY space` &larr; pressing the spacebar <br>
`^KEY SPACE` &larr; pressing the space bar too <br>
`^KEY K` &larr; pressing the 'k' letter  <br>

---

### ^HOLD
A function similar to `^KEY`. Specifies how long a single
button should be held (pressed). We set the time at the
end of the command in the same form as in the `^WAIT`
function.
#### Syntax
`^HOLD <key_name> <time>` <br>
#### Example
`^HOLD s 3` &larr; press the 's' key for 3 seconds <br>
`^HOLD space 0.5` &larr; press the spacebar for 0.5 seconds <br>

---

### ^COMB
Allows you to press several buttons at once.
**Recommended to using keyboard shortcuts.***
#### Syntax
`^COMB <key_name> <key_name>` <br>
`^COMB <key_name> <single_letter>`
#### Example
`^COMB cmd space` &larr; cmd + spacebar <br>
`^COMB control c` &larr; copy shortcut <br>

---

### ^SENTEN
This feature allows you to type whole sentences at once.
**Each sequence ends with the enter key.**
#### Syntax
`^SENTEN <text>`
#### Example
`^SENTEN echo "Print my string"` &larr; bash command <br>

---

### ^WRITE
The function works similarly to `^SENET`, but between typing
each single letter must elapse the set time.
The time set at the end of the line after the sentence,
in the same format as for the `^WAIT` function. <br>
The function simply emits handwriting.
#### Syntax
`^WRITE <text> <time>`
#### Example
`^WRITE I'm writing this sentence like a person. 0.1` &larr;
the pause between each letter is 0.1 second <br>

---
