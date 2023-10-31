const { SlashCommandBuilder, VoiceChannel } = require('discord.js');
const { getVoiceConnection } = require('@discordjs/voice')

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
                await interaction.reply(`Left voice Channel.`);
            } else {
                await interaction.reply(`Im not in a voice channel bruh.`);
            }
        }
    }
}