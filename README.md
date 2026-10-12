# Friday Night Funkin: Pythonic Edition 🎤🐍

> **Disclaimer:** This project was built when I was 13 years old. Viewer discretion is strongly advised. Looking directly at the source code may cause confusion, headaches, and an overwhelming urge to rewrite everything using proper Object-Oriented Programming.

Friday Night Funkin' but it's Pythonic.

---

## ❓ Why?

To be honest, I don't know.

---

## 🏛️ The 13-Year-Old Developer Hall of Shame (Code Quirks)

If you peek under the hood of `main.py`, you'll witness some legendary beginner developer architecture:

* **Global Variable Abuse:** Why encapsulate state in a class when you can just drop `global` everywhere and pray it works?
* **The "Yacine" Easter Egg:** Deep within the config generator, you'll find a very important configuration key: `"YACINE EST PD": True`. Critical for game stability.
* **Magic Numbers & Cursed Constants:** `note.y = -69` is a core mathematical formula required for precise rhythm game sync.
* **Wild Type-Checking:** Functions like `changeScore(pos="None")` accept booleans, strings, and existential dread interchangeably.
* **Bulletproof Error Handling:** `try... except:` blocks that catch *literally* every error because who has time to debug specific exceptions?

---

## 📋 To-Do List (As of 3 Years Ago)

- [x] Charts
- [x] Music
- [x] Main menu
- [ ] Game stats and info
- [ ] Game UI
- [ ] Saving score and stats
- [ ] Low graphic settings
- [ ] Week system
- [x] More songs
- [ ] Characters and backgrounds
- [ ] Arrow customization
- [ ] Custom keybinds
- [ ] Multi-key system
- [ ] Settings menu
- [ ] Dialogues
- [ ] Cutscenes
- [ ] Chart editor
- [ ] Mod support
- [ ] Mod maker

*(Spoiler alert: Most of the bottom half remained undone as reality set in.)*

---

## ⚙️ Requirements & Installation

If you are brave enough to run this relic, you'll need Python and `pygame`:

```bash
pip install pygame
```

1. Clone or download the repository.
2. Ensure you have the `assets/` folder packed with all the songs, charts, and images.
3. Run the game:

```bash
python main.py
```

---

## 💖 Credits

Made with ❤ by **GuestTox** (and a slightly more traumatized older version of him looking back at this code). 

* [GitHub Profile](https://github.com/GuestTox) 
* [Website](https://guesttox.github.io)
