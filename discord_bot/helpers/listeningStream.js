const prism = require('prism-media');
const net = require('net');
const { EndBehaviorType} = require('@discordjs/voice');
const { embedLength } = require('discord.js');

function createListeningStream(receiver, userId, username) {
    const opusStream = receiver.subscribe(userId, {
        end: {
            behavior: EndBehaviorType.AfterSilence,
            duration: 200,
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

        const bytes = Buffer.alloc(4)

        console.log(`connected to ${ip}:${port}`);
        const username_buffer = Buffer.from(username, 'utf-8')
        const buffer_length = username_buffer.length
        
        bytes.writeInt32LE(buffer_length, 0);
        
        const combinedBuffer = Buffer.alloc(4 + buffer_length);
        combinedBuffer.writeUInt32LE(buffer_length, 0);
        username_buffer.copy(combinedBuffer, 4);
        socket.write(combinedBuffer)

        opusStream.on('data', (opusPacket) => {
            opusDecoder.write(opusPacket)
            const pcmAudioStream = opusDecoder.read();
            if (pcmAudioStream) {
                socket.write(pcmAudioStream, (err) => {
                    if (err) {
                        console.error('Error sending audio data:',err);
                    } else {
                        // console.log(`Audio data sent successfully to ${ip}:${port}`);
                    }
                });
            }
        });

        opusStream.on('end', () => {
            console.log("Closed socket");
            socket.end();
        });
    });
}

module.exports = { createListeningStream };