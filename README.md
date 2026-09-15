# Audio Book Read Any PDF

A Python application that extracts text from a PDF document and reads it aloud using text-to-speech.

This project is useful for listening to study materials, notes, articles, and other text-based PDF documents.

## Features

- Extracts text from all pages of a PDF.
- Reads the extracted text aloud.
- Supports voice selection.
- Supports speech-rate adjustment.
- Displays the extraction progress.
- Handles missing files and empty PDFs.
- Works with text-based PDF files.

## Technologies Used

- Python
- PyPDF2
- pyttsx3

## How It Works

1. The program opens a PDF file.
2. Text is extracted from each page.
3. The extracted text is combined.
4. The text-to-speech engine reads the content aloud.

## Project Structure

```text
audio-book-read-any-pdf/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone [https://github.com/rafittishanneo/audio-book-read-any-pdf.git](https://github.com/rafittishanneo/audio-book-read-any-pdf.git)
```

### 2. Open the project folder

```bash
cd audio-book-read-any-pdf
```

### 3. Create a virtual environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS or Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

Place a PDF file in the project folder and run:

```bash
python main.py "your-file.pdf"
```

If no filename is provided, the program looks for:

```text
topic 1.pdf
```

### Select a Voice

First, identify the available voice indexes from your system. Then run:

```bash
python main.py "your-file.pdf" --voice 1
```

### Change Speech Rate

```bash
python main.py "your-file.pdf" --rate 150
```

You can combine both options:

```bash
python main.py "your-file.pdf" --voice 1 --rate 150
```

## Example

```bash
python main.py "study-notes.pdf" --rate 140
```

Example output:

```text
Number of pages: 10
Extracting page 1/10
Extracting page 2/10
...
All pages extracted.
Starting audiobook...
Audiobook finished!
```

## Limitations

- The program works best with text-based PDFs.
- Scanned PDFs may not contain extractable text.
- Image-only pages require OCR.
- Very large PDFs may take time to process.
- Available voices depend on the operating system.
- The application currently reads the PDF directly instead of exporting an MP3 file.

## Future Improvements

- Add a graphical user interface.
- Add OCR support for scanned PDFs.
- Export speech as MP3 or WAV.
- Add pause, resume, and stop controls.
- Read one page at a time.
- Add support for multiple languages.
- Display the available system voices automatically.
- Add bookmarks and reading progress.

## Copyright Notice

Only use PDF documents that you own, have permission to use, or are legally allowed to process.

Do not upload copyrighted books or other protected documents to this repository without permission.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
