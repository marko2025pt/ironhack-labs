# Load environment variables from .env file (for API keys, etc.)
from dotenv import load_dotenv

# Operating system interaction (environment variables, file paths)
import os

# Work with JSON data (reading/writing/parsing)
import json

# Encode images to base64 (needed for API image input)
import base64

# Make HTTP requests (e.g., downloading images)
import requests

# Work with file system paths in a clean way
from pathlib import Path

# Handle image data in memory
from io import BytesIO

# Work with tabular data (dataframes)
import pandas as pd

# Load datasets (if used in previous lab)
from datasets import load_dataset

# Image processing
from PIL import Image

# OpenAI API client
from openai import OpenAI


load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
print(os.getenv("OPENAI_API_KEY") is not None)

client = OpenAI() 
response = client.responses.create( model="gpt-4.1-mini", input="Hello! Respond with one short sentence." ) 
print(response.output_text)

# Step 2: Load and prepare the product dataset
# This block loads the dataset from HuggingFace (or fallback local dataset),
# converts it to a pandas DataFrame, and sets up the images folder.



print("Loading product dataset...")
try:
    # Load first 100 samples from HuggingFace dataset
    dataset = load_dataset("ashraq/fashion-product-images-small", split="train[:100]")
    print(f"✓ Loaded {len(dataset)} products")
    
    # Convert to pandas DataFrame
    products_df = pd.DataFrame(dataset)
    print(f"Dataset columns: {products_df.columns.tolist()}")
    
except Exception as e:
    print(f"⚠ Could not load HuggingFace dataset: {e}")
    print("Using local images instead...")
    
    # Fallback local dataset
    products_data = [
        {
            "id": 1,
            "name": "Wireless Headphones",
            "price": 79.99,
            "category": "Electronics",
            "image_path": "images/product1.jpg"
        },
        # Add more products if needed
    ]
    
    products_df = pd.DataFrame(products_data)

# Create images directory
images_dir = Path("product_images")
images_dir.mkdir(exist_ok=True)

print(f"\n✓ Dataset prepared!")
print(f"Total products: {len(products_df)}")

# Step 2 Verification: Display first 5 products and their images



# Show first 5 products in DataFrame
print("First 5 products:")
display(products_df.head())

# Display images for first 5 products (if 'image' column exists)
if 'image' in products_df.columns:
    print("\nDisplaying first 5 product images:")
    for i in range(min(5, len(products_df))):
        try:
            img = products_df.loc[i, 'image']  # Already a PIL image
            print(f"{i+1}. {products_df.loc[i, 'productDisplayName']}")
            display(img)
        except Exception as e:
            print(f"⚠ Could not display image {i+1}: {e}")

# Step 3: Encode all product images to base64 and verify



# Function to encode PIL.Image to base64
def encode_image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_bytes = buffered.getvalue()
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    return img_b64

# Add a new column to products_df with base64 images
products_df['image_b64'] = products_df['image'].apply(encode_image_to_base64)

print("✓ All product images encoded to base64.")

# Checkpoint: verify first 5 encoded images
print("\nVerifying first 5 images:")
for i in range(min(5, len(products_df))):
    img_b64 = products_df.loc[i, 'image_b64']
    print(f"{i+1}. Base64 length: {len(img_b64)} characters")
    
    # Decode and display image
    img_bytes = base64.b64decode(img_b64)
    img_reconstructed = Image.open(BytesIO(img_bytes))
    display(img_reconstructed)


# Step 4: Create product listing prompts using Ironhack template


def create_product_listing_prompt(product_name, price, category, additional_info=None):
    """
    Create a prompt for generating product listings.
    
    Parameters:
    - product_name: Name of the product
    - price: Price of the product
    - category: Product category
    - additional_info: Optional additional information
    
    Returns:
    - Formatted prompt string
    """
    prompt = f"""You are an expert e-commerce copywriter. Analyze the product image and create a compelling product listing.

Product Information:
- Name: {product_name}
- Price: ${price:.2f}
- Category: {category}
{f'- Additional Info: {additional_info}' if additional_info else ''}

Please create a professional product listing that includes:

1. **Product Title** (catchy, SEO-friendly, 60 characters max)
2. **Product Description** (detailed, 150-200 words)
   - Highlight key features and benefits
   - Use persuasive language
   - Include relevant details visible in the image
3. **Key Features** (bullet points, 5-7 items)
4. **SEO Keywords** (comma-separated, 10-15 relevant keywords)

Format your response as JSON with the following structure:
{{
    "title": "Product title here",
    "description": "Full description here",
    "features": ["Feature 1", "Feature 2", ...],
    "keywords": "keyword1, keyword2, ..."
}}

Be specific about what you see in the image. Mention colors, materials, design elements, and any distinctive features."""
    
    return prompt

# Test prompt creation
test_prompt = create_product_listing_prompt(
    product_name="Wireless Bluetooth Headphones",
    price=79.99,
    category="Electronics",
    additional_info="Noise cancelling, 30-hour battery"
)

print("\n" + "="*50)
print("PROMPT TEMPLATE")
print("="*50)
print(test_prompt[:1500] + "...")  # Show first 1500 characters




# Preview the first N products (set to 5)
num_preview = min(5, len(products_df))

for i in range(num_preview):
    product = products_df.iloc[i]
    
    # Show product info
    print(f"\n--- Product {i+1} ---")
    print(f"Name: {product['productDisplayName']}")
    print(f"Category: {product['masterCategory']} > {product['subCategory']} > {product['articleType']}")
    print(f"Color: {product['baseColour']}, Season: {product['season']}")
    
    # Display the image (already a PIL Image object)
    img = product['image']  # no indexing needed
    img.show()
    
    # Wait for user to close image before moving to next
    input("Press Enter to continue to next product...")


# Step 5: Call ChatGPT API with vision for one product (using prepared prompt and encoded image)



# Initialize the OpenAI client (if not already initialized)
client = OpenAI()

# Select the first product
first_product = products_df.iloc[0]

# Create the prompt using the Ironhack function
product_prompt = create_product_listing_prompt(
    product_name=first_product['productDisplayName'],
    price=first_product.get('price', 0.0),
    category=f"{first_product['masterCategory']} > {first_product['subCategory']} > {first_product['articleType']}",
    additional_info=f"Color: {first_product['baseColour']}, Season: {first_product['season']}"
)

# Retrieve the base64-encoded image from Step 3
img_b64 = first_product['image_b64']

# Prepare API input using the vision-supported format
api_input = [
    {
        "role": "user",
        "content": [
            {"type": "input_text", "text": product_prompt},
            {"type": "input_image", "image_url": f"data:image/jpeg;base64,{img_b64}"}
        ]
    }
]

# Call the API
try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=api_input
    )
    
    # Extract JSON output
    output_text = response.output_text
    product_listing = json.loads(output_text)
    
    print("✓ Product listing generated successfully!\n")
    print(json.dumps(product_listing, indent=4))

except Exception as e:
    print(f"⚠ Error calling ChatGPT API: {e}")


# Store product description into a JSON file
output_filename = "ProductDescription1.json"

# Save the generated product listing
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(product_listing, f, indent=4, ensure_ascii=False)

print(f"✓ Product listing saved to {output_filename}")


# Step 6: Call ChatGPT API with vision for products 2, 3, and 4

# Loop over products 2, 3, 4 (indices 1, 2, 3)
for i in [1, 2, 3]:
    try:
        product = products_df.iloc[i]

        # Create the prompt using the Ironhack function
        product_prompt = create_product_listing_prompt(
            product_name=product['productDisplayName'],
            price=product.get('price', 0.0),
            category=f"{product['masterCategory']} > {product['subCategory']} > {product['articleType']}",
            additional_info=f"Color: {product['baseColour']}, Season: {product['season']}"
        )

        # Retrieve the base64-encoded image from Step 3
        img_b64 = product['image_b64']

        # Prepare API input using vision-supported format
        api_input = [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": product_prompt},
                    {"type": "input_image", "image_url": f"data:image/jpeg;base64,{img_b64}"}
                ]
            }
        ]

        # Call the API
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=api_input
        )

        # Extract JSON output
        output_text = response.output_text
        product_listing = json.loads(output_text)

        # Save JSON file
        filename = f"ProductDescription{i+1}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(product_listing, f, indent=4, ensure_ascii=False)

        # Print in human-readable format
        print(f"\n=== Product {i+1} Listing ===")
        print("TITLE:")
        print(product_listing["title"])
        print("\nDESCRIPTION:")
        print(product_listing["description"])
        print("\nFEATURES:")
        for ftr in product_listing["features"]:
            print(f"- {ftr}")
        print("\nKEYWORDS:")
        print(product_listing["keywords"])
        print(f"\n✓ Saved to {filename}")

    except Exception as e:
        print(f"⚠ Error processing product {i+1}: {e}")

print("\n✓ Step 6 completed: Multiple products processed.")
