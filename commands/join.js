const { SlashCommandBuilder, VoiceChannel } = require('discord.js');
const { joinVoiceChannel } = require('@discordjs/voice')

module.exports = {
    data: new SlashCommandBuilder()
        .setName('join')
        .setDescription('Join current voice channel'),
    async execute(interaction) {
        const member = interaction.member;
        if (!interaction.member.voice.channel) {
                return await interaction.reply(`You are not in a voice channel dumbbass @${member.user.tag}`); 
            } else {
            const voiceChannel = member.voice.channel;
            const connection = joinVoiceChannel({
                channelId: voiceChannel.id,
                guildId: voiceChannel.guild.id,
                adapterCreator: voiceChannel.guild.voiceAdapterCreator,
            });
            
            await interaction.reply(`Joined voice channel: ${voiceChannel.name}`);
        }
    }
}