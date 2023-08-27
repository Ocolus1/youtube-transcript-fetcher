# YouTube Transcript Fetcher Documentation

This Python application utilizes Streamlit to create a web-based interface that allows users to fetch transcripts of YouTube videos. The YouTube Transcript API is used to retrieve the transcripts.

## Libraries and Modules Used

- `streamlit`: For creating the web interface.
- `youtube_transcript_api`: To fetch YouTube video transcripts.
- `json`: To format JSON data for easy readability.

## Functions

### `fetch_transcript(video_id: str) -> Tuple[Optional[List[Dict]], Optional[str]]`

#### Parameters

- `video_id`: A string representing the YouTube video ID.

#### Returns

- A tuple containing the transcript as a list of dictionaries, if it exists, or an error message.

#### Description

This function attempts to fetch the transcript of a YouTube video using its video ID. If fetching is unsuccessful, an error message will be returned.

### `main() -> None`

#### Description

This function contains the main logic for the Streamlit application. It initializes the Streamlit interface, manages state, and calls the `fetch_transcript` function to retrieve transcripts.

## Streamlit UI Components

- `st.title()`: Sets the title of the web application.
- `st.text_input()`: Creates a text input box for the user to enter a YouTube video ID.
- `st.button()`: Creates a button that triggers the transcript fetching when clicked.
- `st.error()`: Displays an error message on the Streamlit interface.
- `st.write()`: Writes text or data to the Streamlit interface.
- `st.text_area()`: Creates a text area for displaying data that the user can manually copy.

## Code Flow

1. The Streamlit session state is initialized to store the transcript.
2. The user inputs a YouTube video ID and clicks the "Fetch Transcript" button.
3. The `fetch_transcript` function is called, and the transcript or an error message is returned.
4. The transcript or error message is displayed on the Streamlit interface.
5. If a transcript is available, a "Copy Transcript" button appears. Clicking it will display the transcript in a text area for manual copying.

## Usage

Run the code with the following command:

```bash
streamlit run main.py
