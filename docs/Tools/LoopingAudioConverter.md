---
date created: 2023-08-24 09:35
date updated: 2023-08-24 09:39
---

# [LoopingAudioConverter](https://github.com/libertyernie/LoopingAudioConverter)

## **Introduction**:

Looping Audio Converter is a sophisticated software solution specifically designed to act as an interface for various programs and libraries. It enables users to convert between an array of looping audio formats, making it a sought-after tool for those in the audio engineering and game modding domains.

## Downloads:

[Releases · libertyernie/LoopingAudioConverter (github.com)](https://github.com/libertyernie/LoopingAudioConverter/releases)

## **Key Features**:

### **Supported Importers**:

- **WaveImporter**: Handles *.wav (signed 16-bit PCM) with looping support via the "smpl" chunk.
- **MP3Importer**: Processes .mp3 files using [MP3Sharp](https://github.com/Nihlus/MP3Sharp), though it doesn't support looping.
- **VorbisImporter**: Converts .ogg and .oga files, utilizing [ffmpeg](https://www.gyan.dev/ffmpeg/builds/), with looping denoted by LOOPSTART/LOOPLENGTH.
- **MSU1Converter**: Converts .pcm files. If a file has a "loop start" of 0, it's considered non-looping.
- **MSFImporter**: Deals with .msf formats, supporting 16-bit PCM in both big or little-endian, or MP3.
- **VGMStreamImporter**: A general importer that functions only if test.exe is available, relying on [vgmstream](https://gitlab.kode54.net/kode54/vgmstream).
- **VGAudioImporter**: Processes a variety of formats like .adx, .brstm, and .hca using [VGAudio](https://github.com/Thealexbarney/VGAudio).
- **BrawlLibImporter**: General-purpose importer leveraging [BrawlCrate's BrawlLib.dll](https://github.com/soopercool101/BrawlCrate).
- **VGMImporter**: Works with .vgm and .vgz, using [VGMPlay](https://vgmrips.net/forum/viewtopic.php?t=112) or optionally ffmpeg.
- **FFmpegEngine**: A universal importer reliant on [ffmpeg](https://www.gyan.dev/ffmpeg/builds/).

### **Supported Exporters**:

- Various formats like BRSTM, [[BCSTM]], and BFSTM utilizing VGAudio with support for looping and codec-specific options.
- Exporters for formats like .dsp, .idsp, and .hps using VGAudio with looping capability.
- BrawlLib-based exporters for BRSTM and [[BCSTM]] in both ADPCM and PCM16 via BrawlCrate.
- WAV format exports with looping via "smpl" using ffmpeg.
- FFmpeg-based exporters for FLAC, MP3, AAC, and Vorbis.
- MSU-1 exporter for the .pcm format.
- [qaac](https://github.com/nu774/qaac) based exporters for AAC with QuickTime dependency.

### **Flexible Looping Options**:

- Keep existing loop points, remove them, add from start-to-end if missing, or specify custom points.
- Options to define segments like those before, within, or after the loop for export.
- Input loop specifications can be defined in a 'loop.txt' file, with each line having the format: `{loop-start} {loop-end} {filename}`.

### **Extensive Audio Effects**:

- Convert to mono for space-saving.
- Adjust the sample rate, amplify the volume, alter the pitch, or modify the tempo.
- Channel-specific export options to split or combine audio channels.

### **Convenient User Interface**:

- Filter options based on file extensions, input, and output directories.
- Options to load or save configurations, facilitating repetitive tasks.
- Command line arguments for automation, enabling conversions to start automatically, use specific XML settings, or define input files.

## **Additional Notes**:

- Users seeking simpler conversions between WAV and VGAudio-supported formats like BRSTM might consider using VGAudioCli.
