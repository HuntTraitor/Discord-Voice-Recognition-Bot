const { Events } = require('discord.js');

//Detects when memebrs join of leave voice channel
module.exports = {
    name: Events.VoiceStateUpdate,
    execute(oldState, newState) {
        const member = newState.member;
        const guild = newState.guild;
        const channel = newState.channel;

        if (channel) {
            console.log(`${member.user.tag} joined voice channel: ${channel.name}`);
        } else {
            console.log(`${member.user.tag} left voice channel`);
        }
    }
}