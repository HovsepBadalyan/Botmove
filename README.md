# BotMove 🤖

BotMove is a Telegram bot built with Python that allows users to interact with parsed data through a simple Telegram interface.

## Features

* Telegram bot integration
* User-friendly keyboard menu
* Data parsing from external sources
* Fast and simple command handling
* Modular project structure

## Project Structure

```text
BotMove/
│
├── bot.py          # Telegram bot logic
├── parser.py       # Data parser
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/HovsepBadalyan/Botmove.git
cd Botmove
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
BOT_TOKEN=your_telegram_bot_token
```

Or insert your bot token directly into the source code (not recommended for production).

## Usage

Run the bot:

```bash
python bot.py
```

After starting, open Telegram and send:

```text
/start
```

The bot will display available options and return parsed information based on the selected category.

## Technologies Used

* Python 3
* pyTelegramBotAPI (TeleBot)
* Selenium
* Requests
* BeautifulSoup (if used)

## Future Improvements

* Database integration
* User statistics
* Admin panel
* Caching system
* Improved parser performance

## Author

**Hovsep Badalyan**

GitHub: https://github.com/HovsepBadalyan

## License

This project is licensed under the MIT License.
