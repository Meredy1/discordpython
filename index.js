const Discord = require("discord.js");
const client = new Discord.Client(); 
const config = require("./config.json");

client.on('message', message => {
     if (message.author.bot) return;
     if (message.channel.type == 'dm') return;
     if (!message.content.toLowerCase().startsWith(config.prefix.toLowerCase())) return;
     if (message.content.startsWith(`<@!${client.user.id}>`) || message.content.startsWith(`<@${client.user.id}>`)) return;

    const args = message.content
        .trim().slice(config.prefix.length)
        .split(/ +/g);
    const command = args.shift().toLowerCase();

    try {
        const commandFile = require(`./commands/${command}.js`)
        commandFile.run(client, message, args);
    } catch (err) {
    console.error('Erro:' + err);
  }
});

//status mudando
client.on("ready", () => {
    let activities = [
        `O meu prefix é " ! "`,
        `Bot Created by: Caio ✝ #8380`,
        `Estou ativo em ${client.guilds.cache.size} servidores!`,
        `Estou ativo em ${client.channels.cache.size} canais!`,
        `Estou gerenciando ${client.users.cache.size} usuários!`
    ],
    i = 0;
    setInterval( () =>
    client.user.setActivity(`${activities[i++ %activities.length]}`, {
        type: "PLAYING"
    }), 5000);
    client.user
    .setStatus("online")
    .catch(console.error);
console.log(`Estou Online!, Estou ativo em ${client.guilds.cache.size} servidores, e estou gerenciando ${client.users.cache.size} usuários!`)
});

client.login(config.token);