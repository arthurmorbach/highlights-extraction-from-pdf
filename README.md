# Extract Highlights from PDF

This project extracts highlighted text from a **PDF file** and saves it into a **.txt file**. It uses the **PyMuPDF (fitz) library** to detect annotations and extract the corresponding highlighted text.

## Features

- Extracts text from highlighted areas in a PDF.
- Saves the extracted text into a text file with the corresponding **page number**.
- Includes a separate script to check if a PDF contains annotations.

## Requirements

Ensure you have **Python 3.x** installed, along with the required dependencies.

### Install dependencies

Run the following command to install PyMuPDF:

```sh
pip install pymupdf
```

## Cloning the Repository

### Install Git

Before cloning the repository, ensure you have Git installed. You can download and install it from:

- **Windows:** [Git for Windows](https://git-scm.com/download/win)
- **Mac:** Install via Homebrew with:
  ```sh
  brew install git
  ```
- **Linux:** Install via package manager:
  ```sh
  sudo apt install git  # Debian/Ubuntu
  sudo dnf install git  # Fedora
  sudo pacman -S git    # Arch
  ```

### Clone the Repository

To get started, clone this repository using Git:

To get started, clone this repository using Git:

```sh
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

Replace `your-username/your-repo` with the actual repository URL.

## Usage

### 1. Extract Highlights from PDF

Run the `main.py` script to extract highlighted text from a PDF and save it to a `.txt` file:

```sh
python main.py
```

By default, the script will process the file:

```
FGV-DAPP-2020-A-economia-de-Roraima-e-o-fluxo-vene_250323_141023.pdf
```

and save the extracted text to:

```
highlights.txt
```

### 2. Check if a PDF has Annotations

Before running the extraction, you can check if the PDF contains highlights using:

```sh
python check_annotations.py
```

This script will list the number of annotations found on each page.

## File Descriptions

- **`main.py`**: Extracts highlighted text and saves it with the corresponding page number.
- **`check_annotations.py`**: Checks whether the PDF contains annotations.
- **`highlights.txt`**: Output file containing the extracted highlighted text.

## Example Output

If highlights are found, `highlights.txt` will contain:

```
This is an important concept.
(Page 12)

Another key point.
(Page 25)
```

If no highlights are detected, the script will print:

```
No highlights found!
```

## Troubleshooting

### No highlights found?

- Ensure your PDF **actually contains** highlight annotations.
- Run `check_annotations.py` to verify the presence of annotations.
- Some PDFs might store highlights differently, in which case **image-based OCR extraction** (e.g., using `pdf2image` + `pytesseract`) may be needed.

## License

This project is open-source and available under the **MIT License**.



