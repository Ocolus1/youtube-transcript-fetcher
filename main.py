import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound, VideoUnavailable
import json

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript, None
    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video."
    except NoTranscriptFound:
        return None, "No transcript found for this video."
    except VideoUnavailable:
        return None, "This video is unavailable."
    except Exception as e:
        return None, f"An unexpected error occurred: {e}"

def main():
    st.title("YouTube Transcript Fetcher")
    
    # Initialize state variable
    if 'transcript' not in st.session_state:
        st.session_state.transcript = None

    video_id = st.text_input("Enter YouTube Video ID:", "")

    if st.button("Fetch Transcript"):
        transcript, error = fetch_transcript(video_id)

        if error:
            st.session_state.transcript = None
            st.error(error)
        else:
            st.session_state.transcript = transcript

    if st.session_state.transcript:
        readable_transcript = "\n".join([entry["text"] for entry in st.session_state.transcript])
        st.write("### Transcript:")
        st.write(readable_transcript)
        
        if st.button("Copy Transcript"):
            st.text_area("Copy the text below:", value=readable_transcript)

if __name__ == "__main__":
    main()
