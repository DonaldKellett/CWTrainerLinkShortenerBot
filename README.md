# cwtlbot-discord

Codewars Trainer Link Bot for Discord

_17/06/2021: There are now concrete plans for an official Codewars Discord bot so I've decided that this project will no longer be accepting contributions. Nevertheless, the source code and existing packages will remain available - feel free to use them as a reference, or feel free to fork this project and develop your own bot in compliance to the AGPL 3.0 (or any later version at your discretion) license._

## Installing

### Using the provided snap (Ubuntu 20.04 and other supported systems)

1. Install `cwtlbot-discord` [from the Snap store](https://snapcraft.io/cwtlbot-discord)
1. Run the initialization script as root: `$ sudo cwtlbot-discord --init`
1. Start the `snap.cwtlbot-discord.cwtlbot-discordd` service as root and enable it to autostart at boot: `$ sudo systemctl enable --now snap.cwtlbot-discord.cwtlbot-discordd.service`
1. Profit :-)

### Using the provided RPM (Fedora 34 and similar systems)

1. Download the RPM package to your local system: `$ wget https://github.com/DonaldKellett/cwtlbot-discord/releases/download/v0.1.1/cwtlbot-discord-0.1.1-1.fc34.noarch.rpm`
1. Install from the local RPM: `$ sudo dnf install /path/to/your/cwtlbot-discord-0.1.1-1.fc34.noarch.rpm`
1. Run the initialization script as root: `$ sudo cwtlbot-discord --init`
1. Start the `cwtlbot-discord` service as root and enable it to autostart at boot: `$ sudo systemctl enable --now cwtlbot-discord.service`
1. Profit :-)

### Using the provided deb (Ubuntu 21.04 and similar systems)

Follow the same steps as in installing from the RPM, but change the download link and installation command accordingly (steps 1-2):

```bash
$ wget https://github.com/DonaldKellett/cwtlbot-discord/releases/download/v0.1.1/cwtlbot-discord_0.1.1_all.deb
$ sudo apt install /path/to/your/cwtlbot-discord_0.1.1_all.deb
```

### Using the provided Docker image (Windows, macOS, Linux)

Ensure that Docker is installed on your system and run the following commands as superuser if necessary.

1. Pull the image from Docker Hub: `$ docker image pull donaldsebleung/cwtlbot-discord:0.1.1`
1. Assuming the login token for your bot is `YOUR_BOT_LOGIN_TOKEN` and its username is `YOUR_BOT_USERNAME`, create and run a Docker container using the following command:
   
   ```bash
   $ docker container run -d \
       --name my-discord-bot \
       --env LOGIN_TOKEN=YOUR_BOT_LOGIN_TOKEN \
       --env USERNAME=YOUR_BOT_USERNAME \
       --restart always \
       donaldsebleung/cwtlbot-discord:0.1.1
   ```
   
   A breakdown of the command line options used:
   
   - `-d`: Run the container in background
   - `--name my-discord-bot`: Name our container `my-discord-bot`
   - `--env LOGIN_TOKEN=YOUR_BOT_LOGIN_TOKEN`: Set the login token to `YOUR_BOT_LOGIN_TOKEN`
   - `--env USERNAME=YOUR_BOT_USERNAME`: Set the username to `YOUR_BOT_USERNAME`
   - `--restart always`: Have the container autostart on boot, as long as the Docker engine is running
1. Profit :-)

Once you're done with the container: `$ docker container stop my-discord-bot && docker container rm my-discord-bot`

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
