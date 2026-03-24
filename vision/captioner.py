from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class ImageCaptioner:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

    def caption(self, image_path):
        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(images=image, return_tensors="pt")
        out = self.model.generate(**inputs)

        caption = self.processor.decode(out[0], skip_special_tokens=True)

        # simple keywords
        keywords = [w for w in caption.split() if len(w) > 3][:3]

        return caption, keywords