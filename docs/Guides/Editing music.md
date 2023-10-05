---
date created: 2023-08-23 12:09
date updated: 2023-10-05 10:20
tags:
  - '#EditingGuide'
---

## Requirements

- [[LoopingAudioConverter]]
- Your music track of choice

### Case Specific Requirements

^52bc7c

- [foobar2000](https://www.foobar2000.org/download)
  - [foobar2000: Components Repository - vgmstream decoder](https://www.foobar2000.org/components/view/foo_input_vgmstream)
- [Audacity](https://www.audacityteam.org/download/)

## Editing Music

Editing Music is not hard. Depending on what you actually want to achieve.
Let's start with replacing entire songs, because that's what most of the people want to do.

1. Get your song.
   The format does not matter since we will be converting it anyways.

2. ![[image-20231005094023625.png]]
   Here you got the base settings you need to keep in mind.
   - First **Add** your file.
   - Select **Output format: [VGAudio] [[BCSTM]]**
   - I set my **New sample rate (Hz):** to 16000 to reduce the file size.
     - Keep in mind that setting the sample rate too low will reduce the audio quality.
   - Looped Songs:
     - Tick the **Export all through loop end** box.
       - I recommend setting a desired song duration instead of a defined number of loops.
     - **Loop options: Add loop information if missing (start-to-end)**
   - Since most games use stereo channels or even more channels we want to select **Put all channels in one file**

3. Now simply rename the converted .bcstm file to the song you want to replace. (see [[tree_basegame]])

There are some special cases though.
Check [[Editing music#^52bc7c|the special case requirements]] to get foobar.
Then you can open up the .[[bcstm]] properties to check the channel count.
For example the Able Sisters Song.

![[image-20231005100606850.png]]

Here we can see that the song has 4 instead of 2 channels.
This is because all channels have various sound effects that play on different occasions.

[Audacity tutorial follows...]
