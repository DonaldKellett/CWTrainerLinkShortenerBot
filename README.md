# cwtlbot-discord

Codewars Trainer Link Bot for Discord

## Installing

### Using the provided RPM (Fedora 34 and similar systems)

1. Download the RPM package to your local system: `$ wget https://github.com/DonaldKellett/cwtlbot-discord/releases/download/v0.1.0/cwtlbot-discord-0.1.0-1.fc34.noarch.rpm`
1. Install from the local RPM: `$ sudo dnf install /path/to/your/cwtlbot-discord-0.1.0-1.fc34.noarch.rpm`
1. Run the initialization script as root:
   
   ```bash
   $ sudo su -
   # cwtlbot-discord --init
   # exit
   ```   
1. Start the `cwtlbot-discord` service as root and enable it to autostart at boot: `$ sudo systemctl enable --now cwtlbot-discord.service`
1. Profit :-)

### From source

Ensure Node.js v12.x.x+ and `npm` are installed on your system.

1. Clone/download the repo to your system with Node.js installed: `$ git clone https://github.com/DonaldKellett/cwtlbot-discord.git`
1. Change directory to the root of this repo: `$ cd /path/to/your/cwtlbot-discord`
1. Create the configuration file `config/token` with the login token `LOGIN_TOKEN` for your bot: `$ echo LOGIN_TOKEN > config/token`
1. Edit the configuration file `config/username` to contain the username `USERNAME` for your bot: `$ echo USERNAME > config/username`
1. Ensuring that you are in the root directory of this repo, run `$ npm install` to install all the required Node.js modules and dependencies
1. Run `$ npm start` to start the bot and enjoy :-)

The behavior of the bot can be further configured via the following environment variables:

- `CONFIG_PATH`: Controls where the bot reads its configuration. Defaults to `/path/to/your/cwtlbot-discord/config`

## License

[AGPL 3.0](./LICENSE) or any later version at your discretion
