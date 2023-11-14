const prism = require('prism-media');
const net = require('net');
const { EndBehaviorType} = require('@discordjs/voice');

function createListeningStream(receiver, userId, user) {
    const opusStream = receiver.subscribe(userId, {
        end: {
            behavior: EndBehaviorType.AfterSilence,
            duration: 250,
        },
    });

    const socket = new net.Socket();


    let ip = '10.10.0.3';
    const port = '8010';

    //creating a decoder to use
    const opusDecoder = new prism.opus.Decoder({
        frameSize: 960,
        channels: 2,
        rate: 48000
    });

    socket.connect(port, ip, () => {
        console.log(`connected to ${ip}:${port}`);
    })

    opusStream.on('end', () => {
        console.log("Closed socket");
        socket.end();
    });

    opusStream.on('data', (opusPacket) => {

        opusDecoder.write(opusPacket)
        const pcmAudioStream = opusDecoder.read();
        
        if (pcmAudioStream) {
            socket.write(pcmAudioStream, (err) => {
                if (err) {
                    console.error('Error sending audio data:',err);
                } else {
                    //console.log(`Audio data sent successfully to ${ip}:${port}`);
                }
            });
        }
    });
}

module.exports = { createListeningStream };