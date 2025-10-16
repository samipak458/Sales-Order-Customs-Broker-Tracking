#!/usr/bin/env python3
"""
PDF to Markdown Converter

This script converts PDF documents into clean Markdown files with support for:
- Text extraction with proper formatting
- Table extraction and markdown table formatting
- Image and diagram extraction with references
- Multi-page document handling
- Robust error handling and logging

Usage:
    python pdf2md.py input.pdf output.md
"""

import argparse
import logging
import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional

try:
    import fitz  # PyMuPDF
    import pdfplumber
    import pandas as pd
    from PIL import Image
except ImportError as e:
    print(f"Error: Missing required library - {e}")
    print("Please install dependencies: pip install -r requirements.txt")
    sys.exit(1)


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class PDFToMarkdownConverter:
    """Convert PDF documents to Markdown format with text, tables, and images."""
    
    def __init__(self, pdf_path: str, output_path: str):
        """
        Initialize the converter.
        
        Args:
            pdf_path: Path to the input PDF file
            output_path: Path to the output Markdown file
        """
        self.pdf_path = Path(pdf_path)
        self.output_path = Path(output_path)
        self.output_dir = self.output_path.parent
        self.image_dir = self.output_dir / "images"
        self.image_counter = 0
        self.markdown_content = []
        
        # Validate input file
        if not self.pdf_path.exists():
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        # Create output directory if it doesn't exist
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.image_dir.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Initialized converter for {self.pdf_path}")
    
    def extract_text_pymupdf(self, page) -> str:
        """
        Extract text from a page using PyMuPDF.
        
        Args:
            page: PyMuPDF page object
            
        Returns:
            Extracted text as string
        """
        try:
            text = page.get_text()
            return text.strip()
        except Exception as e:
            logger.error(f"Error extracting text with PyMuPDF: {e}")
            return ""
    
    def extract_images_from_page(self, doc, page_num: int) -> List[str]:
        """
        Extract images from a PDF page.
        
        Args:
            doc: PyMuPDF document object
            page_num: Page number (0-indexed)
            
        Returns:
            List of image file paths
        """
        image_paths = []
        
        try:
            page = doc[page_num]
            image_list = page.get_images()
            
            for img_index, img in enumerate(image_list):
                try:
                    xref = img[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_ext = base_image["ext"]
                    
                    self.image_counter += 1
                    image_filename = f"image{self.image_counter}.{image_ext}"
                    image_path = self.image_dir / image_filename
                    
                    # Save image
                    with open(image_path, "wb") as img_file:
                        img_file.write(image_bytes)
                    
                    # Return relative path for markdown
                    relative_path = f"images/{image_filename}"
                    image_paths.append(relative_path)
                    logger.info(f"Extracted image: {relative_path}")
                    
                except Exception as e:
                    logger.warning(f"Failed to extract image {img_index} from page {page_num + 1}: {e}")
        
        except Exception as e:
            logger.error(f"Error extracting images from page {page_num + 1}: {e}")
        
        return image_paths
    
    def extract_tables_from_page(self, page) -> List[str]:
        """
        Extract tables from a PDF page and convert to markdown.
        
        Args:
            page: pdfplumber page object
            
        Returns:
            List of markdown table strings
        """
        markdown_tables = []
        
        try:
            tables = page.extract_tables()
            
            for table_index, table in enumerate(tables):
                if not table or len(table) == 0:
                    continue
                
                try:
                    # Convert table to pandas DataFrame for easier markdown conversion
                    df = pd.DataFrame(table[1:], columns=table[0])
                    
                    # Clean up the dataframe
                    df = df.fillna('')
                    df = df.map(lambda x: str(x).strip() if x else '')
                    
                    # Convert to markdown
                    markdown_table = df.to_markdown(index=False)
                    markdown_tables.append(markdown_table)
                    logger.info(f"Extracted table {table_index + 1} with {len(df)} rows")
                    
                except Exception as e:
                    logger.warning(f"Failed to convert table {table_index + 1} to markdown: {e}")
        
        except Exception as e:
            logger.error(f"Error extracting tables: {e}")
        
        return markdown_tables
    
    def detect_headers(self, text: str) -> str:
        """
        Detect potential headers and format them.
        
        Args:
            text: Text to analyze
            
        Returns:
            Text with headers formatted
        """
        lines = text.split('\n')
        formatted_lines = []
        
        for line in lines:
            line = line.strip()
            if not line:
                formatted_lines.append(line)
                continue
            
            # Detect potential headers (all caps, short lines, etc.)
            if len(line) < 100 and line.isupper() and len(line.split()) <= 10:
                formatted_lines.append(f"## {line.title()}")
            elif len(line) < 80 and len(line.split()) <= 8 and line[0].isupper():
                # Check if it might be a header (short, starts with capital)
                if any(keyword in line.lower() for keyword in ['section', 'chapter', 'overview', 'introduction', 'conclusion', 'summary']):
                    formatted_lines.append(f"### {line}")
                else:
                    formatted_lines.append(line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)
    
    def process_page(self, doc_pymupdf, doc_pdfplumber, page_num: int) -> str:
        """
        Process a single page and extract all content.
        
        Args:
            doc_pymupdf: PyMuPDF document object
            doc_pdfplumber: pdfplumber document object
            page_num: Page number (0-indexed)
            
        Returns:
            Markdown content for the page
        """
        page_content = []
        
        logger.info(f"Processing page {page_num + 1}")
        
        # Add page separator for multi-page documents
        if page_num > 0:
            page_content.append(f"\n---\n")
        
        page_content.append(f"\n<!-- Page {page_num + 1} -->\n")
        
        # Extract text using PyMuPDF
        try:
            pymupdf_page = doc_pymupdf[page_num]
            text = self.extract_text_pymupdf(pymupdf_page)
            
            if text:
                # Detect and format headers
                formatted_text = self.detect_headers(text)
                page_content.append(formatted_text)
                page_content.append("\n")
        except Exception as e:
            logger.error(f"Error processing text on page {page_num + 1}: {e}")
        
        # Extract tables using pdfplumber
        try:
            pdfplumber_page = doc_pdfplumber.pages[page_num]
            tables = self.extract_tables_from_page(pdfplumber_page)
            
            for table in tables:
                page_content.append("\n")
                page_content.append(table)
                page_content.append("\n")
        except Exception as e:
            logger.error(f"Error processing tables on page {page_num + 1}: {e}")
        
        # Extract images
        try:
            image_paths = self.extract_images_from_page(doc_pymupdf, page_num)
            
            for img_path in image_paths:
                page_content.append(f"\n![Image]({img_path})\n")
        except Exception as e:
            logger.error(f"Error processing images on page {page_num + 1}: {e}")
        
        return ''.join(page_content)
    
    def convert(self) -> None:
        """
        Main conversion method. Extracts all content from PDF and saves to Markdown.
        """
        logger.info(f"Starting conversion of {self.pdf_path}")
        
        try:
            # Open PDF with both libraries
            doc_pymupdf = fitz.open(str(self.pdf_path))
            doc_pdfplumber = pdfplumber.open(str(self.pdf_path))
            
            num_pages = len(doc_pymupdf)
            logger.info(f"Document has {num_pages} pages")
            
            # Add document title
            self.markdown_content.append(f"# {self.pdf_path.stem}\n\n")
            
            # Process each page
            for page_num in range(num_pages):
                try:
                    page_markdown = self.process_page(doc_pymupdf, doc_pdfplumber, page_num)
                    self.markdown_content.append(page_markdown)
                except Exception as e:
                    logger.error(f"Failed to process page {page_num + 1}: {e}")
                    self.markdown_content.append(f"\n<!-- Error processing page {page_num + 1} -->\n")
            
            # Close documents
            doc_pymupdf.close()
            doc_pdfplumber.close()
            
            # Write to output file
            self.save_markdown()
            
            logger.info(f"Conversion completed successfully. Output: {self.output_path}")
            logger.info(f"Extracted {self.image_counter} images to {self.image_dir}")
            
        except Exception as e:
            logger.error(f"Fatal error during conversion: {e}")
            raise
    
    def save_markdown(self) -> None:
        """Save the markdown content to the output file."""
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(''.join(self.markdown_content))
            logger.info(f"Saved markdown to {self.output_path}")
        except Exception as e:
            logger.error(f"Error saving markdown file: {e}")
            raise


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description='Convert PDF documents to Markdown format with text, tables, and images.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python pdf2md.py input.pdf output.md
  python pdf2md.py document.pdf converted/document.md
  
The script will create an 'images' directory next to the output file
for storing extracted images.
        """
    )
    
    parser.add_argument(
        'input_pdf',
        help='Path to the input PDF file'
    )
    
    parser.add_argument(
        'output_md',
        help='Path to the output Markdown file'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    try:
        converter = PDFToMarkdownConverter(args.input_pdf, args.output_md)
        converter.convert()
        print(f"\n✓ Conversion successful!")
        print(f"  Output: {args.output_md}")
        print(f"  Images: {converter.image_dir}")
        return 0
    
    except FileNotFoundError as e:
        logger.error(str(e))
        return 1
    except Exception as e:
        logger.error(f"Conversion failed: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
