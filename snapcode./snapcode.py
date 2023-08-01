import pytesseract
import torch
from PIL import Image
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class CodeSnap:
  def __init__(self, image_path):

    self.image_path = image_path
  
  def loadmodel(self):
    
    tokenizer = AutoTokenizer.from_pretrained("vishnun/codenlbert-sm")
    model = AutoModelForSequenceClassification.from_pretrained("vishnun/codenlbert-sm")

    return tokenizer, model

  def retrievecode(self):

    ocr_list = [x for x in pytesseract.image_to_string(self.image_path).split("\n") if x != '']
    tokenizer, model = self.loadmodel()

    ## Retrieve Code Blocks
    text_list = []
    for text in ocr_list:
      input_ids = tokenizer(text, return_tensors="pt")
      with torch.no_grad():
          logits = model(**input_ids).logits

      predicted_class_id = logits.argmax().item()

      if model.config.id2label[predicted_class_id].upper() == "CODE":
        text_list.append(text)
    
    return ('\n').join(text_list)


