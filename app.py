import os
import re
import json
from pdf2image import convert_from_path
import pytesseract
import spacy
from spacy.training.example import Example
from spacy.tokens import DocBin
import random
from pathlib import Path


# Path to Tesseract executable (Set this according to your OS)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Create output directories if they don't exist
os.makedirs("output", exist_ok=True)
os.makedirs("training_data", exist_ok=True)

# Convert PDF to images
def convert_pdf_to_images(pdf_path):
    images = convert_from_path(pdf_path)
    image_paths = []
    for i, image in enumerate(images):
        image_path = f"output/invoice_{i + 1}.png"
        image.save(image_path, "PNG")
        image_paths.append(image_path)
    return image_paths

# Extract text using Tesseract
def extract_text_from_image(image_path):
    text = pytesseract.image_to_string(image_path)
    return text

# Clean extracted text
def clean_text(text):
    text = re.sub(r'\n+', '\n', text)  # Remove excessive newlines
    text = re.sub(r'\s+', ' ', text)  # Remove excessive spaces
    return text.strip()







def extract_invoice_fields(text):
    invoice_number = re.search(r'(Invoice(?: No)?[:#]?\s*([A-Za-z0-9-]+))', text, re.IGNORECASE)
    invoice_date = re.search(r'(Invoice Date|Date)[:#]?\s*([0-9]{2,4}[-/][0-9]{2,4}[-/][0-9]{2,4})', text, re.IGNORECASE)
    line_items = re.findall(r'(\d+\s+[A-Za-z0-9\s,.-]+\s+\d+\.\d+\s+\d+\.\d+\s+\d+\.\d+)', text)

    result = {
        'invoice_number': invoice_number.group(2) if invoice_number else None,
        'invoice_date': invoice_date.group(2) if invoice_date else None,
        'line_items': line_items
    }
    return result






def train_spacy_model(training_data):
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner", last=True)

    # Add labels to the NER pipeline
    for _, annotations in training_data:
        for ent in annotations.get("entities"):
            ner.add_label(ent[2])

    optimizer = nlp.begin_training()

    for i in range(100):
        random.shuffle(training_data)
        losses = {}
        for text, annotations in training_data:
            doc = nlp.make_doc(text)
            example = Example.from_dict(doc, {"entities": annotations["entities"]})  # ✅ FIXED
            nlp.update([example], drop=0.2, losses=losses)
        print(f"Losses at iteration {i}: {losses}")

    # Save the model
    output_dir = Path("output/spacy_invoice_model")
    if not output_dir.exists():
        output_dir.mkdir(parents=True)
    nlp.to_disk(output_dir)

    
    
    
    
    

# Predict using trained Spacy model
def predict_using_spacy(model_path, text):
    nlp = spacy.load(model_path)
    doc = nlp(text)
    entities = {ent.label_: ent.text for ent in doc.ents}
    return entities

# Main function
def main(pdf_path):
    print("Converting PDF to images...")
    image_paths = convert_pdf_to_images(pdf_path)
    
    all_extracted_data = []
    
    for image_path in image_paths:
        print(f"Extracting text from {image_path}...")
        extracted_text = extract_text_from_image(image_path)
        cleaned_text = clean_text(extracted_text)
        
        print("Extracted text:")
        print(cleaned_text)

        extracted_data = extract_invoice_fields(cleaned_text)
        all_extracted_data.append(extracted_data)
    
    # Save extracted data to JSON
    with open("output/extracted_invoices.json", "w") as f:
        json.dump(all_extracted_data, f, indent=4)
    
    # Sample Training Data for Spacy (Add more examples)
    
    
    
    
    # training_data = [
    #     (cleaned_text, {"entities": [(extracted_data['invoice_number'].start(), extracted_data['invoice_number'].end(), "INVOICE_NUMBER"),
    #                                  (extracted_data['invoice_date'].start(), extracted_data['invoice_date'].end(), "INVOICE_DATE")]})
    # ]
    
    
    
    training_data = []
    if extracted_data['invoice_number'] and extracted_data['invoice_date']:
        entities = []
        if extracted_data['invoice_number']:
            start = cleaned_text.find(extracted_data['invoice_number'])
            end = start + len(extracted_data['invoice_number'])
            entities.append((start, end, "INVOICE_NUMBER"))
    
        if extracted_data['invoice_date']:
            start = cleaned_text.find(extracted_data['invoice_date'])
            end = start + len(extracted_data['invoice_date'])
            entities.append((start, end, "INVOICE_DATE"))
    
        training_data.append((cleaned_text, {"entities": entities}))

    
    



    
    
    
    print("Training Spacy model...")
    train_spacy_model(training_data)
    
    print("Predicting using Spacy model...")
    result = predict_using_spacy("output/spacy_invoice_model", cleaned_text)
    
    print("Prediction result:")
    print(result)




if __name__ == "__main__":
    pdf_path = r"C:\Users\sss\Desktop\assments\masterindia\ML Assignment Assignment (1).pdf"
    main(pdf_path)
