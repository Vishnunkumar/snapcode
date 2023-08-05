# CodeSnap
Retrieve code blocks from screenshots using Transformers and Tesseract

## Usage
```python
from snapcode.snapcode import CodeSnap

codesnap = CodeSnap(image_path)
codesnap.loadmodel()
codesnap.retrievecode()

```
