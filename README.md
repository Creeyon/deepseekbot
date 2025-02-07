# Discord Bot Project

This project is a Discord bot that interacts with the DeepSeek AI API. It processes commands from users and returns responses as messages in Discord.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/discord-bot.git
   cd discord-bot
   ```

2. Create a `.env` file in the root directory and add your API keys:
   ```
   API_KEY=your_deepseek_api_key
   DISCORD_TOKEN=your_discord_bot_token
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the bot, execute the following command:
```
python src/bot.py
```

Make sure your bot is invited to a server and has the necessary permissions to read and send messages.

## Commands

The bot supports various commands that interact with the DeepSeek AI API. You can type commands in any text channel where the bot is present.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.