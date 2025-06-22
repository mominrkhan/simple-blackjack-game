# 🃏 Simple Blackjack Game — Python Terminal Edition

A classic Blackjack game playable right in your terminal!  
Built from scratch with clean Python OOP, logging, and a sleek user experience — all without any GUI or frameworks.  
Just pure logic, cards, and cool vibes.

---

## 💻 How It’s Made

**🛠 Tech Used:**  
- Python 3.13  
- `@dataclass` for clean and readable card definitions  
- OOP architecture: `Card`, `Deck`, `Hand`, `BlackjackGame`  
- Python’s built-in `logging` module for pro-style output  
- Terminal UI (pure CLI experience)  
- Input validation & Ace-handling logic (Blackjack rules FTW)  
- Clean CLI-based interaction loop with balance tracking and betting  

---

## ⚡ Optimizations

- ✅ Converted card objects to `@dataclass` for simplicity and performance  
- ✅ Used `logging` instead of `print()` for cleaner output and file logging  
- ✅ Fully encapsulated game logic (easier to test and extend)  
- ✅ Smart Ace value adjustment (prevents unnecessary busts)  
- ✅ Game logs saved to `blackjack_log.txt` for replay/review  

---

## 🧠 Lessons Learned

- Refactored procedural code into modular, testable OOP components  
- Replaced all `print()` with structured logging using `logging`  
- Simulated realistic Blackjack edge cases (e.g. double aces, ties)  
- Designed CLI game flow that feels polished and responsive  
- Learned how to use Python’s built-in modules to handle real-world gameplay logic  

---

## 📸 Game in Action

<img width="315" alt="Screenshot 2025-06-22 at 4 34 54 AM" src="https://github.com/user-attachments/assets/d208cbd5-2d86-4454-90cd-8b6233d20793" />

---

## 🏁 Try It Yourself

Clone the repo and run the game:

```bash
git clone https://github.com/mominrkhan/simple-blackjack-game.git
cd simple-blackjack-game
python blackjack.py
