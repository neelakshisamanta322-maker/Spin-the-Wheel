
# 🎰 Spin the Wheel — Python Betting Game

A simple interactive console-based betting game where players deposit money, place bets, and spin a wheel to win or lose based on random outcomes.


---

## 📌 **Game Features**

* 💷 Deposit any amount of money to start playing
* 🎡 Spin a 5-colour wheel with different outcomes
* 💰 Bet any amount within your current balance
* 🔁 Play unlimited rounds until you decide to stop
* 🏦 Option to withdraw final balance at the end

---

## 🎡 **Wheel Outcomes**

Each spin lands on one of five colours:

| Colour     | Result                    |
| ---------- | ------------------------- |
| **Green**  | You win **2×** your bet   |
| **Blue**   | You **lose** your bet     |
| **Yellow** | You win **1.5×** your bet |
| **Red**    | Your bet is **returned**  |
| **Orange** | You **lose** your bet     |

---

## 🧠 **How the Code Works**

1. **Displays game introduction** and explains the rules
2. **Prompts player to deposit money**
3. Enters a loop where the player:

   * Enters a **bet amount**
   * The program **validates** the bet
   * A random number (1–5) determines outcome
4. The program **updates balance** based on result
5. Asks user whether to **play again or exit**
6. At exit, offers to **withdraw balance**

---

## 🛠️ **Technologies Used**

* **Python 3**
* `random` module for generating wheel outcomes

---

## ▶️ **How to Run**

```bash
python lottery.py
```

---

## 📁 **File Included**

* `lottery.py` — main game script 

---

