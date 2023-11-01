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

        // connection.receiver.subscribe({
        //     async data(audioData, user) {
        //         if(user.id == speakingUser) {
        //             console.log(`Listening to ${speakingUser}...`);
        //         }
        //     },
        // });

        // const membersInVoice = member.voice.channel.members
        // membersInVoice.forEach((member) => {
        //     console.log(member.user.tag);
        // });
        
        // const guild = interaction.guild;
        // const connection = getVoiceConnection(guild.id);
        // const receiver = connection.receiver;

        // receiver.speaking.on('start', (userId) => {
        //     console.log(getFile);

        //     console.log(`Channel ID: ${userId}`);

        //     // getFile.createListeningStream(receiver, userId, interaction.user);
        // });
        await interaction.reply('I am listening......');
    }
}