import uvicorn
from fastapi import FastAPI, HTTPException, Request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
from pydantic import BaseModel 

# Load the pre-trained model
model = load_model('model_version/classifier_model.h5', compile=False)

app = FastAPI()
labels = ['Business', 'Entertainment', 'Politics', 'Sports', 'Tech']
tokenizer = Tokenizer(num_words=25963, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
max_length = 3100


@app.post("/classify")
async def classify_complaint(request: Request):
    try:
        data = await request.json()
        input_text = data.get("text")
        if input_text is None:
            raise HTTPException(status_code=400, detail="Input text is missing.")
        
        seq = tokenizer.texts_to_sequences([input_text])  # Pass a list of texts
        padded = pad_sequences(seq, maxlen=max_length)
        pred = model.predict(padded)
        
        max_prob_idx = np.argmax(pred)
        predicted_label = labels[max_prob_idx]
        confidence_score = float(pred[0][max_prob_idx])
        
        return {"label": predicted_label, "confidence": format(confidence_score, '.6f')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=9999)
