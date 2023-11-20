const prism = require('prism-media');
const net = require('net');
const { EndBehaviorType} = require('@discordjs/voice');
const { embedLength } = require('discord.js');

function createListeningStream(receiver, userId, username, filename) {
    
    //terminates after 200 ms of silence
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
        console.log(`connected to ${ip}:${port}`);
        /*
            Sending the first two packets of data for the username and the filename(to specify guild)
            This is done by taking the first 4 bytes and encoding that as the length of the string 
            followed by the string itself.
         */
        const username_buffer = Buffer.from(username, 'utf-8')
        const username_length = username_buffer.length
        const username_bytes = Buffer.alloc(4)
        username_bytes.writeInt32LE(username_length, 0);
        const combined_username_buffer = Buffer.alloc(4 + username_length);
        combined_username_buffer.writeUInt32LE(username_length, 0);
        username_buffer.copy(combined_username_buffer, 4);
        socket.write(combined_username_buffer);
        
        const filename_buffer = Buffer.from(filename, 'utf-8')
        const filename_length = filename_buffer.length
        const filename_bytes = Buffer.alloc(4);
        filename_bytes.writeInt32LE(filename_length, 0);
        const combined_filename_buffer = Buffer.alloc(4 + filename_length);
        combined_filename_buffer.writeUInt32LE(filename_length, 0);
        filename_buffer.copy(combined_filename_buffer, 4); 
        socket.write(combined_filename_buffer);

        //write to trasncription service
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