#Lab M1.07 - Whisper STT Implementation
##Marco Martins

This lab demonstrates transcription of audio using OpenAI’s Whisper API, including guided prompts, chunking, timestamps, and multiple export formats.

---

### Step 1: Loading OpenAI API Key from `.env`

In this step, we securely load the OpenAI API key from a `.env` file instead of hardcoding it in the notebook.  

**Steps performed:**
1. Import required libraries: `os` for environment variables, `dotenv` to load `.env` files, and `openai` for API access.
2. Load environment variables from the `.env` file using `load_dotenv()`.
3. Set the OpenAI API key for the `openai` library with `os.getenv("OPENAI_API_KEY")`.
4. Optionally, verify that the key is loaded by printing `True` if it exists.

**Security Note:** This prevents the API key from being pushed to GitHub if `.env` is added to `.gitignore`.

---

### Step 2: Prep Audio (Manually)

The audio file was prepared and placed in the project folder for processing.  
- File format: MP3
- Duration: 1 minute 26 seconds
- Single speaker, historical interview after the first moon landing

---

### Step 3: Basic Transcription (Without Chunking)

We transcribed the short audio file using Whisper API without prompts.  

**Objectives:**
- Understand basic API usage
- See response format
- Extract transcription text

**Outcome:**  
- The unguided transcription captured most content accurately
- Some sentences were run-on with minimal punctuation
- Minor contextual errors (e.g., “back to Maine” instead of “back to Earth”)

---

### Step 4: Transcription with Prompts (Guided Approach)

We guided the Whisper transcription using a **context-adapted prompt** for the moon landing interview.

**Objectives:**
- Improve transcription accuracy
- Capture astronaut names and mission details
- Preserve dialogue flow
- Compare with unguided transcription

**Process:**
- Defined a prompt emphasizing historical context, dialogue, and technical terms
- Sent audio + prompt to Whisper API
- Received guided transcription

**Guided transcription improvements:**
- Better punctuation and sentence separation
- Context-specific corrections (“back to Earth” instead of “back to Maine”)
- Clearer dialogue flow
- Professional, archival-quality transcript

**Note on audio realism:**  
While real business meetings often involve multiple speakers and overlapping speech, this lab uses a single-speaker audio sample to demonstrate transcription, chunking, and timestamp extraction.  
The same pipeline applies to multi-speaker meetings, though additional techniques (speaker diarization, noise handling) would be required in production.  
Although the sample is short, the pipeline scales to multi-hour recordings.

---

### Step 5: Audio Chunking

For demonstration, we split the audio into **20-second chunks**.

**Objectives:**
- Process manageable segments with Whisper
- Preserve timestamps for each chunk
- Allow multiple chunks to be shown during the demo

**Note:**  
Even though the audio was short, chunking demonstrates scalability to longer recordings.

---

### Step 6: Transcribing Audio Chunks with Timestamps

Each chunk was sent individually to Whisper API.  

**Process:**
- Transcribe each chunk
- Adjust timestamps to match original audio position
- Combine chunks into a full transcript

**Outcome:**  
- Each segment has start/end times
- Full transcript can be navigated or searched using timestamps

---

### Step 7: Exporting Transcriptions with Timestamps

The chunked transcription data was exported in three formats:

1. **Human-readable text file** – easy to review
2. **SRT (subtitle) file** – for video captions
3. **JSON file** – structured format for programmatic use

All exports preserve timestamps for each chunk, maintaining context and sequence.

---

### Step 8: Comparison of Unguided vs Guided Transcriptions

**Unguided Transcription (without prompts):**
- Captured basic content
- Run-on sentences, minimal punctuation
- Some context errors (“back to Maine”)
- Harder to follow dialogue

**Guided Transcription (with context-adapted prompt):**
- Prompt tailored to moon landing interview
- Corrected context-specific terms (“back to Earth”)
- Improved punctuation and sentence separation
- Clearer dialogue, natural phrasing
- Professional and archival-quality transcript

**Conclusion:**  
Guided transcription improves both **accuracy** and **readability**, making it better suited for archival, research, or professional use. Using prompts that reflect actual audio context is highly beneficial for Whisper transcription.


### Issues Encountered and Resolutions

During this lab, we faced several technical and workflow challenges. Below is a summary of the main issues and how we resolved them:

1. **FFmpeg Not Found by PyDub**
   - **Issue:** PyDub could not locate FFmpeg, causing `FileNotFoundError`.
   - **Resolution:** Added FFmpeg to the system PATH and verified installation with `ffmpeg -version`. Restarting VS Code ensured the environment recognized the change.

2. **Incorrect Audio Paths**
   - **Issue:** Hardcoded or absolute paths prevented reproducibility on other machines.
   - **Resolution:** Switched to relative paths (`audio/CA138clip.mp3`) so the notebook works across different systems.

3. **Chunk Length Misconfiguration**
   - **Issue:** Initially set for 10 minutes, which was too long for our 1:26 clip.
   - **Resolution:** Adjusted chunk length to 20 seconds for demonstration, showing multiple chunks even with short audio.

4. **OpenAI API Changes**
   - **Issue:** Older `openai.Audio` interface no longer supported, causing `APIRemovedInV1`.
   - **Resolution:** Migrated to the updated OpenAI v1 interface using `openai.audio.transcriptions.create()`.

5. **Unguided Transcription Limitations**
   - **Issue:** Without a prompt, transcription had long sentences, minimal punctuation, and some context errors.
   - **Resolution:** Implemented a context-adapted prompt emphasizing historical interview content, astronaut names, mission details, and dialogue structure.

6. **Ensuring Multi-format Export**
   - **Issue:** Needed readable output in text, SRT, and JSON formats with timestamps.
   - **Resolution:** Implemented an export pipeline that produces all three formats with proper start/end times for each chunk.

**Additional Notes:**
- Audio realism: Single-speaker audio was used to simplify demonstration. Multi-speaker or noisy recordings would require additional techniques like speaker diarization or noise filtering.
- Chunking and timestamping: Designed to scale for longer recordings, demonstrating robustness of the pipeline.

# Audio Transcription Lab Report

This lab explored audio transcription using OpenAI's Whisper API, comparing unprompted vs guided transcriptions, implementing chunking, and exporting results in multiple formats.

---

### 1. Differences Between Prompted and Unprompted Transcriptions

We transcribed the same audio clip in two ways:

- **Unguided Transcription:**  
  Captured the basic content accurately but had long sentences, minimal punctuation, and minor context errors (e.g., “back to Maine” instead of “back to Earth”). Dialogue flow was harder to follow, making it less readable.

- **Guided Transcription (Prompted):**  
  Used a context-adapted prompt reflecting a historical interview after the moon landing.  
  - Corrected context-specific terms (e.g., “back to Earth”).  
  - Improved sentence separation, punctuation, and readability.  
  - Separated questions and answers for clearer dialogue flow.  
  - Produced a professional, archival-quality transcript suitable for historical records.  

**Conclusion:** Contextual prompts significantly improve transcription accuracy, readability, and professional quality.

---

### 2. Benefits of Chunking for Long Audio

Chunking splits long recordings into smaller segments for processing:

- Enables handling of multi-hour audio without overwhelming the API.  
- Preserves timestamps for each segment, making it easier to navigate or align with video.  
- Reduces the risk of errors from long, continuous audio streams.  
- Demonstrated with 20-second chunks, the same pipeline scales to larger recordings.

---

### 3. Challenges Faced

- **FFmpeg Path Issues:** PyDub could not locate FFmpeg initially. Resolved by adding FFmpeg to the system PATH.  
- **Audio File Paths:** Absolute paths caused reproducibility issues; switched to relative paths.  
- **API Interface Changes:** Older `openai.Audio` calls were deprecated; migrated to the updated v1 interface.  
- **Chunk Length Adjustments:** Original 10-minute chunks were too long for a short clip; reduced to 20 seconds for demo purposes.  
- **Unguided Transcription Limitations:** Without context, output was less readable and contained minor inaccuracies.

---

### 4. Recommendations for Improving Accuracy

- **Context-Adaptive Prompts:** Always tailor prompts to the audio content (e.g., technical terms, speaker roles, historical context).  
- **Speaker Identification:** For multi-speaker audio, implement speaker diarization to separate dialogue.  
- **Noise Reduction:** Preprocess audio to reduce background noise and overlapping speech.  
- **Punctuation and Formatting:** Post-process transcriptions for punctuation, capitalization, and readability.  
- **Chunking Strategy:** Optimize chunk length based on recording length and content density for balance between accuracy and processing efficiency.

---

**Summary:**  
Guided transcription with chunking produces accurate, readable, and timestamped outputs suitable for archival or research purposes. The pipeline is scalable to longer recordings and can be enhanced further with speaker separation and noise handling.

