# 🐍 Python Cheat Sheet — Grace's Quick Reference

**You do NOT need to memorize any of this.** Glance at it whenever you need the exact spelling.
Every developer keeps a reference like this. Understanding > memorizing.

---

## 📢 Printing (the program's voice)
```python
print("Hello!")                 # show text on screen
print("Hi, " + name + "!")      # glue strings together with +
```

## 📦 Variables (labeled boxes that store a value)
```python
name = "Grace"                  # = means "put this in the box" (store)
age = 47                        # numbers don't need quotes
```

## ⌨️ Input (the program's ears)
```python
name = input("What is your name? ")   # ALWAYS gives back a STRING (text)
```
⚠️ Even if the user types `8`, you get the *text* `"8"`, not the *number* `8`.

## 🔤 Strings vs Numbers (types)
```python
"8"    # a string (text) — from input(), or anything in quotes
8      # a number — for doing math
"8" == 8    # False!  text is not the same as a number
```

## ✅ Making decisions — if / else
```python
if answer == "green":           # == CHECKS if two things are the same
    print("Correct!")           # indented = "inside" the if
else:
    print("Not quite.")
```
- `=` stores · `==` checks · colon `:` starts a block · indent 4 spaces.

## 📋 Lists (one box holding many items, in order)
```python
colors = ["red", "green", "blue"]   # square brackets [ ] make a list
colors[0]        # "red"   ← counting starts at 0!
colors[1]        # "green"
colors[2]        # "blue"
len(colors)      # 3  (how many items)
```

## 🔁 For loops — the different ways (all do "repeat something")

**👉 The decision rule (WHY you pick each one):**
- One list, just need each item? → **Style 1** (cleaner, use by default)
- Need to know the POSITION (to pair with another list, or number items "Question 1:")? → **Style 2**, because you need `i`

**Way 1 (Style 1) — loop over the items (cleanest, most common):**
```python
for color in colors:
    print(color)          # the temp box holds the ITEM itself — use it directly, no [ ]
```

**Way 2 (Style 2) — loop over positions (when you need the index number i):**
```python
for i in range(len(colors)):
    print(colors[i])      # the temp box holds a NUMBER (0,1,2...) — use colors[i] to get the item
```
🔑 WHY this exists: the position `i` is like a ROW NUMBER. It lets you read across
TWO matching lists at the same spot — this is how the quiz pairs each question with its answer:
```python
for i in range(len(questions)):
    print(questions[i])   # question at row i
    print(answers[i])     # its matching answer, SAME row i
```

**Way 3 — enumerate (get the item AND its position at once):**
```python
for i, color in enumerate(colors):
    print(i, color)
```

**Way 4 — repeat a fixed number of times:**
```python
for x in range(3):
    print("Hello")     # prints Hello 3 times
```

🧠 The ONE rule to remember:
- `for X in myList:`            → X is an ITEM, use it directly
- `for i in range(len(myList)):` → i is a NUMBER, use myList[i] to get the item

The skeleton to remember (the SHAPE, not the letters):
```
for  <temp box>  in  <the list>  :
    <do this to each one>          ← indented
```

---

## 🐛 Reading errors (they are HELPFUL notes — read bottom to top)
| Error | What it usually means |
|-------|----------------------|
| `SyntaxError: expected ':'` | You forgot a colon `:` after `for` / `if` / `else` |
| `IndentationError` | A line isn't indented (or is indented wrong) |
| `TypeError` | Mixed incompatible types (e.g. list + string, or "8" + 8) |
| `NameError` | Misspelled a variable name (Python often suggests the fix!) |

**Debugging loop:** run → read the error → fix ONE thing → run again.
⚠️ Bugs hide on paths you don't test — always test the "wrong answer" path too.

---

## 💾 Git — save your work to GitHub (the daily loop)
```bash
git add .                       # 1. stage a snapshot of your changes
git commit -m "what I did"      # 2. save it with a note
git push                        # 3. upload to GitHub
```
