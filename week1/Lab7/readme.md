# Lab 7 – Audio Transcription with Whisper

This lab demonstrates audio transcription using OpenAI's Whisper API, including guided prompts, audio chunking, timestamp extraction, and exporting results in multiple formats.

---

## Folder Structure

### `audio/`
Original audio files used in the lab.  
- Example: `CA138clip.mp3` – the audio clip of a historical interview after the first moon landing.

### `audio_chunks/`
Contains smaller segments of the original audio, created for easier processing with Whisper.  
- Chunks are typically 20 seconds each for demonstration purposes.  
- Naming convention: `chunk_1.mp3`, `chunk_2.mp3`, etc.

### `transcriptions/`
Holds transcription results generated from Whisper.  
- `transcription.txt` – human-readable text file with timestamps.  
- `transcription.srt` – subtitle file suitable for video.  
- `transcription.json` – structured JSON file with timestamps for programmatic use.

---

## Key Files

### `Lab7 Report.md`
Detailed report of the lab, including transcription comparisons, benefits of chunking, challenges faced, and recommendations.

### `whisper_transcription.ipynb`
Advanced notebook demonstrating:
- Audio chunking
- Transcription of each chunk
- Timestamp management
- Exporting transcriptions in multiple formats

---

## Notes

- **Guided Transcription:** Prompts are adapted to match the historical interview context, improving accuracy and readability.  
- **Chunking:** Even short audio is split to demonstrate the process; the same workflow scales to multi-hour recordings.  
- **Export Formats:** Transcriptions are available in `.txt`, `.srt`, and `.json` for flexibility.  

This lab is designed to show the complete pipeline for audio transcription with Whisper, including handling longer recordings and maintaining accurate timestamps.
