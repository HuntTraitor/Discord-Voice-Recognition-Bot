const { SlashCommandBuilder, TeamMemberMembershipState} = require('discord.js');
const { getVoiceConnection } = require('@discordjs/voice');
const getFile = require("../helpers/listeningStream");
const { joinVoiceChannel } = require('@discordjs/voice');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('listen')
        .setDescription('Listen to voice channel'),
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
        }

        const connection = getVoiceConnection(interaction.guild.id);
        connection.receiver.speaking.on('start', (userId) => {
            console.log(userId);
            console.log(getFile);
            getFile.createListeningStream(connection.receiver, userId, userId);
        });
        await interaction.reply('I am listening......');
    }
}