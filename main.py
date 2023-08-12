import pdfplumber
import sys

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            # Extraction du texte brut de la page
            page_text = page.extract_text()
            
            # Ajout du texte de la page à la sortie
            text += page_text
            
            # Gestion des images (sous forme de texte [Image], par exemple)
            for img in page.images:
                text += "[Image]\n"
        
        return text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <chemin_vers_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
