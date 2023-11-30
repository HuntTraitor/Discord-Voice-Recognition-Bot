const { SlashCommandBuilder, VoiceChannel } = require('discord.js');
const { getVoiceConnection } = require('@discordjs/voice')
const https = require('https')

//Leaves the voice channel
module.exports = {
    data: new SlashCommandBuilder()
        .setName('leave')
        .setDescription('Leaves current voice channel'),
    async execute(interaction) {
        const member = interaction.member;
        if (!interaction.member.voice.channel) {
                return await interaction.reply(`You are not in a voice channel dumbbass @${member.user.tag}`); 
            } else {
            const guild = interaction.guild;
            const connection = getVoiceConnection(guild.id);
            if (connection) {
                connection.destroy();

                fetch("http://10.10.0.3:8000/upload", {
                    method: "PUT",
                    body: JSON.stringify({
                        guild: guild.id
                    }),
                    headers: {
                        "Content-type": "application/json; charset=UTF-8"
                    }
                })
                    .then((response) => response.json())
                    .then((json) => console.log(json))
                    .catch(error => {
                        console.error("Error sending request to upload API: ", error);
                    });

                await interaction.reply(`https://media.tenor.com/JBCYX4zLffgAAAAC/peace-disappear.gif`);
            } else {
                await interaction.reply(`Im not in a voice channel bruh.`);
            }
        }
    }
}