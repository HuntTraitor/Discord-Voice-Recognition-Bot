const { pipeline } = require('stream');
const prism = require('prism-media');
const fs = require('fs');
const { EndBehaviorType} = require('@discordjs/voice');

function createListeningStream(receiver, userId, user) {
    const opusStream = receiver.subscribe(userId, {
        end: {
            behavior: EndBehaviorType.AfterSilence,
            duration: 500,
        },
    });

    const timestamp = Date.now();
    const filename = `./recordings/${user}_${timestamp}.pcm`;
    const out = fs.createWriteStream(filename);

    const opusDecorder = new prism.opus.Decoder({
        frameSize: 960,
        channels: 2,
        rate: 48000
    });

    const logStream = new (require('stream').Transform)({
        transform(chunk, encoding, callback) {
            callback(null, chunk);
        }
    });

    pipeline(opusStream, opusDecorder, logStream, out, (err) => {
        if (err) {
            console.error('Pipeline failed.', err);
        } else {
            console.log('Pipeline succeeded');
        }
    })
}

module.exports = { createListeningStream };