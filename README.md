# PDF to Markdown Converter

A robust Python script that converts PDF documents into clean, structured Markdown files with support for text extraction, table formatting, and image extraction.

## Features

- **Text Extraction**: Extracts and preserves text content from PDF documents
- **Table Support**: Automatically detects and converts tables to Markdown table syntax
- **Image Extraction**: Extracts images and diagrams, saving them to disk with proper references
- **Multi-page Support**: Handles documents of any length
- **Smart Formatting**: Attempts to detect and format headers appropriately
- **Robust Error Handling**: Gracefully handles extraction failures with detailed logging
- **Modular Design**: Clean, maintainable code structure for future enhancements

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Install Dependencies

```bash
pip install -r requirements.txt
```

The required libraries are:
- **PyMuPDF (fitz)**: Fast PDF parsing and image extraction
- **pdfplumber**: Advanced table detection and extraction
- **pandas**: Table data manipulation and markdown conversion
- **Pillow**: Image processing
- **camelot-py**: Additional table extraction capabilities

## Usage

### Basic Usage

```bash
python pdf2md.py input.pdf output.md
```

### With Verbose Logging

```bash
python pdf2md.py input.pdf output.md --verbose
```

### Examples

Convert a document to markdown:
```bash
python pdf2md.py "FDD SCM0603- Sales Order Customs Broker Tracking-V2.0 (1).pdf" output.md
```

Specify a custom output location:
```bash
python pdf2md.py document.pdf converted/document.md
```

### Output Structure

The script generates:
1. **Markdown file** at the specified output path
2. **images/** directory containing extracted images (created in the same directory as the output file)

Example output structure:
```
output.md
images/
  ├── image1.png
  ├── image2.png
  └── image3.jpg
```

## Command-Line Options

```
positional arguments:
  input_pdf          Path to the input PDF file
  output_md          Path to the output Markdown file

optional arguments:
  -h, --help         Show help message and exit
  -v, --verbose      Enable verbose logging
```

## Output Format

The generated Markdown includes:

### Headers
The script attempts to detect headers from the PDF and formats them appropriately:
```markdown
## Section Title
### Subsection
```

### Tables
Tables are converted to clean Markdown syntax:
```markdown
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Images
Images are extracted and referenced:
```markdown
![Image](images/image1.png)
```

### Page Separators
Multi-page documents include page markers:
```markdown
---
<!-- Page 2 -->
```

## Logging

The script provides detailed logging of the conversion process:
- **INFO**: Normal operation messages (page processing, extraction success)
- **WARNING**: Non-fatal issues (failed to extract specific table/image)
- **ERROR**: Fatal errors that prevent conversion

Example log output:
```
2024-01-15 10:30:45 - INFO - Initialized converter for document.pdf
2024-01-15 10:30:45 - INFO - Document has 25 pages
2024-01-15 10:30:46 - INFO - Processing page 1
2024-01-15 10:30:46 - INFO - Extracted table 1 with 5 rows
2024-01-15 10:30:47 - INFO - Extracted image: images/image1.png
```

## Limitations

### Current Limitations

1. **Header Detection**: The script uses heuristics to detect headers. Complex layouts may not be perfectly identified.

2. **Table Complexity**: 
   - Very complex tables with merged cells may not convert perfectly
   - Tables spanning multiple pages are treated as separate tables
   
3. **Image Quality**: 
   - Extracted images maintain their original resolution from the PDF
   - Vector graphics may be rasterized
   
4. **Layout Preservation**: 
   - Multi-column layouts may not preserve the exact visual structure
   - Text wrapping around images is not maintained
   
5. **Special Content**:
   - Form fields are extracted as text only
   - Annotations and comments are not extracted
   - Hyperlinks may not be preserved in some cases

### Known Issues

- PDFs with heavy encryption may fail to process
- Scanned PDFs without OCR will have limited text extraction
- Very large PDFs may require significant processing time

## Troubleshooting

### Import Errors

If you encounter import errors, ensure all dependencies are installed:
```bash
pip install --upgrade -r requirements.txt
```

### Permission Errors

Ensure you have write permissions for the output directory:
```bash
chmod 755 /path/to/output/directory
```

### Memory Issues

For very large PDFs, consider:
- Processing smaller page ranges
- Increasing available system memory
- Using a more powerful machine

## Development

### Code Structure

```
pdf2md.py
├── PDFToMarkdownConverter (main class)
│   ├── __init__: Initialize converter with paths
│   ├── extract_text_pymupdf: Extract text from pages
│   ├── extract_images_from_page: Extract and save images
│   ├── extract_tables_from_page: Extract and format tables
│   ├── detect_headers: Format headers intelligently
│   ├── process_page: Coordinate extraction for a page
│   ├── convert: Main conversion orchestration
│   └── save_markdown: Write output file
└── main: CLI entry point
```

### Future Enhancements

Potential improvements for future versions:
- [ ] OCR support for scanned PDFs
- [ ] Preserve hyperlinks
- [ ] Better multi-column layout handling
- [ ] Custom header detection rules
- [ ] Page range selection
- [ ] Batch processing multiple PDFs
- [ ] Configuration file support
- [ ] HTML output option
- [ ] GUI interface

## Contributing

Contributions are welcome! Areas for improvement:
- Enhanced table detection algorithms
- Better header/structure recognition
- Performance optimizations
- Additional output formats
- Test coverage

## License

This project is provided as-is for educational and professional use.

## Support

For issues, questions, or suggestions:
1. Check the Limitations section above
2. Review the Troubleshooting guide
3. Enable verbose logging (`-v`) to get detailed diagnostic information
4. Open an issue on the repository with:
   - Python version
   - Operating system
   - Full error message and logs
   - Sample PDF (if possible)

## Acknowledgments

This script leverages excellent open-source libraries:
- PyMuPDF (MuPDF) - Fast PDF rendering
- pdfplumber - Excellent table extraction
- pandas - Data manipulation
- Pillow - Image processing
