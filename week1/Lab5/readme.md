# Lab 5: Product Listing Generator with ChatGPT Vision

This lab demonstrates the generation of e-commerce product listings using the ChatGPT Vision API. The notebook processes product images, creates prompts, calls the API, and saves structured outputs.

## Contents

- **product_listing_generator.ipynb**: Step-by-step notebook that:
  - Loads product data
  - Encodes images to base64
  - Creates prompts for each product
  - Calls ChatGPT Vision API to generate listings
  - Saves results in JSON files
  - Logs outputs and displays human-readable previews

- **ProductDescription1.json** to **ProductDescription4.json**: Structured output from the API for each product, including:
  - Title
  - Description
  - Key features
  - SEO keywords

- **LAB5Report.txt**: Brief report covering:
  - API integration workflow
  - Challenges encountered
  - Quality of generated listings
  - Potential improvements

- **Lab5Outputslog.txt**: Captures console outputs and verification steps during notebook execution.

## Notes

- JSON files are structured for easy reuse or integration with e-commerce platforms.
- The notebook includes Markdown explanations for each step, making it self-contained.
