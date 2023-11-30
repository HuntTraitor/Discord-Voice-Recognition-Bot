const { SlashCommandBuilder, TeamMemberMembershipState} = require('discord.js');
const { getVoiceConnection } = require('@discordjs/voice');
const getFile = require("../helpers/listeningStream");
const { joinVoiceChannel } = require('@discordjs/voice');

/*
    Bot joins voice channel and listens for audio streams from different memebrs.
    If an audio stream is detected, it calls createListeningStream on the audio stream.
*/
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
        const voiceChannel = member.voice.channel;
        const connection = getVoiceConnection(interaction.guild.id);
        connection.receiver.speaking.on('start', (userId) => { //SHOULD WE HANDLE SOCKETS HERE AND JUST PASS THE SOCKET????
            //get the username
            const guildMember = voiceChannel.guild.members.cache.get(userId);
            const username = guildMember.displayName || guildMember.user.username;

            //create socket here and pass it to avoid bug maybe haha
            getFile.createListeningStream(connection.receiver, userId, username, filename); //create socket here and pass it
        });
        
        //gets the guild ID and time and sets the filename that we want to send
        const guildId = interaction.member.guild.id;
        const time = new Date();
        timestamp = time.toISOString().slice(0,19).replace("T", " "); //formatting timestamp
        const filename = `${guildId}--${timestamp}.txt`
        await interaction.reply('🔥🔥✍🔥🔥Now Transcribing🔥🔥✍🔥🔥');
    }
}
