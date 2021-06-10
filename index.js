'use strict'
const path = require('path')
const fs = require('fs')
const Discord = require('discord.js')
const client = new Discord.Client()
const CONFIG_PATH = process.env.CONFIG_PATH || path.join(__dirname, 'config')
const TOKEN_PATH = path.join(CONFIG_PATH, 'token')
const USERNAME_PATH = path.join(CONFIG_PATH, 'username')

if (!fs.existsSync(TOKEN_PATH)) {
  console.error(`Could not find required configuration file ${TOKEN_PATH}`)
  process.exit(1)
}
if (!fs.existsSync(USERNAME_PATH)) {
  console.error(`Could not find required configuration file ${USERNAME_PATH}`)
  process.exit(1)
}

let tokenStat = fs.statSync(TOKEN_PATH)
if (!tokenStat.isFile()) {
  console.error(`Expected ${TOKEN_PATH} to be a regular file`)
  process.exit(1)
}
let usernameStat = fs.statSync(USERNAME_PATH)
if (!usernameStat.isFile()) {
  console.error(`Expected ${USERNAME_PATH} to be a regular file`)
  process.exit(1)
}

let token = fs.readFileSync(TOKEN_PATH).toString()
if (token.length > 0 && token[token.length - 1] === '\n')
  token = token.slice(0, token.length - 1)
let username = fs.readFileSync(USERNAME_PATH).toString()
if (username.length > 0 && username[username.length - 1] === '\n')
  username = username.slice(0, username.length - 1)

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`)
})

client.on('message', msg => {
  if (msg.author.username !== username) {
    let trainerLinks = msg.content.match(/https?:\/\/(www\.)?codewars.com\/kata\/[0-9a-f]{24}\/train\/[a-z]+/g)
    if (trainerLinks !== null && trainerLinks.length > 0)
      msg.reply(`Please refrain from posting links to the trainer (i.e. those ending with \`/train/<language-id>\`) as fellow Codewarriors may accidentally click on it and end up with an unwanted Kata on their "Unfinished" list. Instead, consider posting direct links to the Kata, by removing the trailing \`/train/<language-id>\` component, as follows:

${trainerLinks.map(trainerLink => '- <' + trainerLink.replace(/\/train\/[a-z]+$/, '') + '>').join`\n`}

----

I am a bot, and this message was generated automatically. You can find my source code on GitHub: <https://github.com/DonaldKellett/cwtlbot-discord>`)
  }
})

client.login(token)
