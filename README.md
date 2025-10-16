# Sales Order Customs Broker Tracking

Complete implementation of Sales Order Customs Broker Tracking functionality for Microsoft Dynamics 365 Finance and Operations, developed for Leggett & Platt Automotive (LPA).

## Project Overview

This repository contains:
1. **Dynamics 365 Implementation** - Complete customization artifacts (EDTs, table extensions, form extensions, business logic)
2. **Comprehensive Documentation** - Deployment, configuration, testing, and user guides
3. **Functional Design Document** - FDD SCM0603 V2.0 in Markdown format
4. **PDF to Markdown Converter** - Utility tool for document conversion

---

## Quick Links

### For Implementation
- 📦 [Implementation Artifacts](Dynamics365/) - All D365 metadata and code
- 📋 [Implementation Summary](IMPLEMENTATION_SUMMARY.md) - Complete overview of what's been implemented
- 📖 [Deployment Guide](Dynamics365/Documentation/DEPLOYMENT_GUIDE.md) - Step-by-step deployment instructions
- ⚙️ [Configuration Guide](Dynamics365/Documentation/CONFIGURATION_GUIDE.md) - System setup procedures
- 🧪 [Test Validation Scripts](Dynamics365/Documentation/TEST_VALIDATION_SCRIPTS.md) - Comprehensive test cases
- 👥 [User Training Guide](Dynamics365/Documentation/USER_TRAINING_GUIDE.md) - End-user documentation

### For Reference
- 📄 [Functional Design Document](FDD_SCM0603_Sales_Order_Customs_Broker_Tracking_V2.0.md) - Business requirements (FDD SCM0603 V2.0)

---

## What This Implementation Provides

### Business Capabilities

✅ **Customer Broker Management**
- Assign customs broker to customer master records
- Track broker information throughout sales process

✅ **Automatic Data Flow**
- Customer → Sales Agreement → Sales Order → Load → Packing Slip
- Broker ID automatically defaults and transfers through the chain

✅ **Flexibility**
- Override broker on sales orders when needed
- Optional field (not mandatory)
- User-friendly lookup and validation

✅ **Reporting & Tracking**
- List page columns for broker filtering
- Historical tracking on packing slips
- Support for workspace tiles

### Technical Components

- **1 Extended Data Type (EDT)** - TMSBrokerId
- **5 Table Extensions** - CustTable, SalesTable, SalesAgreementHeader, WHSLoadTable, CustPackingSlipJour
- **5 Form Extensions** - Customer, Sales Order, Sales Agreement, Load, Packing Slip Journal
- **5 Business Logic Classes** - Defaulting, validation, and transfer logic
- **Complete Documentation** - Deployment, configuration, testing, training

---

## Getting Started

### For Developers

1. Review the [Implementation Summary](IMPLEMENTATION_SUMMARY.md)
2. Read the [Technical Specification](Dynamics365/Documentation/TECHNICAL_SPECIFICATION.md)
3. Follow the [Deployment Guide](Dynamics365/Documentation/DEPLOYMENT_GUIDE.md)
4. Import artifacts from `Dynamics365/Metadata/` into your D365 project

### For Administrators

1. Review the [Configuration Guide](Dynamics365/Documentation/CONFIGURATION_GUIDE.md)
2. Setup customs brokers in Shipping Carriers
3. Configure security roles
4. Run test validation scripts

### For End Users

1. Read the [User Training Guide](Dynamics365/Documentation/USER_TRAINING_GUIDE.md)
2. Practice in test environment
3. Attend training sessions

---

## Repository Structure

```
Sales-Order-Customs-Broker-Tracking/
├── Dynamics365/                              # Main implementation
│   ├── Metadata/                             # D365 artifacts
│   │   ├── EDTs/                             # Extended Data Types
│   │   ├── Tables/                           # Table extensions
│   │   ├── Forms/                            # Form extensions
│   │   └── Classes/                          # Business logic (X++)
│   ├── Documentation/                        # Complete guides
│   │   ├── DEPLOYMENT_GUIDE.md
│   │   ├── CONFIGURATION_GUIDE.md
│   │   ├── TECHNICAL_SPECIFICATION.md
│   │   ├── TEST_VALIDATION_SCRIPTS.md
│   │   └── USER_TRAINING_GUIDE.md
│   └── README.md
├── FDD_SCM0603_Sales_Order_Customs_Broker_Tracking_V2.0.md
├── IMPLEMENTATION_SUMMARY.md
├── README.md                                 # This file
└── pdf2md.py                                 # PDF converter utility
```

---

## Implementation Status

✅ **COMPLETE** - All components implemented per FDD SCM0603 V2.0

- ✅ Extended Data Type (TMSBrokerId)
- ✅ All table extensions created
- ✅ All form extensions created
- ✅ All business logic classes implemented
- ✅ Deployment guide completed
- ✅ Configuration guide completed
- ✅ Technical specification completed
- ✅ Test validation scripts completed
- ✅ User training guide completed

---

## Technology Stack

- **Platform:** Microsoft Dynamics 365 Finance and Operations
- **Language:** X++ (business logic)
- **Metadata:** XML (extensions)
- **Architecture:** Extension-based (no overlayering)

---

## Support

For questions or issues:
- Review documentation in `Dynamics365/Documentation/`
- Contact your Dynamics 365 administrator
- Reference FDD SCM0603 V2.0 for business requirements

---

# PDF to Markdown Converter (Utility Tool)

A robust Python script that converts PDF documents into clean, structured Markdown files with support for text extraction, table formatting, and image extraction.

**Note:** This utility was used to convert the FDD documents to Markdown format.

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
