---
date created: 2023-08-23 12:09
date updated: 2023-08-23 12:29
---

## Introduction:

BCSTM stands for "Binary Cafe Stream", a proprietary audio streaming format developed by Nintendo. This format is mainly used in Nintendo's game platforms such as the Nintendo 3DS to store audio data, mainly background music and sometimes sound effects.

## Structure and Components:

1. **Audio Data**: At their core, BCSTM files contain the actual audio data. This can be music tracks, voice lines, sound effects, or any other audio used in games.
2. **Headers: BCSTM files start with a header section that contains metadata about the audio, such as the audio format (e.g. PCM16, DSP ADPCM), sample rate, loop points, channel count, and other important details that determine how the audio should be played.
3. **Loop Points: One of the distinguishing features of BCSTM is its support for defining loop points directly in the audio file. This is especially useful and important for background music in games, where a track needs to loop seamlessly.
4. **Channels**: BCSTM files can store multi-channel audio data, ensuring support for stereo sound and sometimes even more complex audio channel setups, such as smooth transitions with different sounds between areas with the same main theme.
