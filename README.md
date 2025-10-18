# de-week2-unittest--Opeoluwa-Oyebanji-

Project: Artificial Pancreas System (Simplified Model)

This is a simple simulation of a data-driven glucose regulation system.
### How It Works
- The `ArtificialPancreasSystem` class models how glucose changes after meals and exercise.
- It predicts whether to:
  - deliver_insulin (if glucose is too high)
  - warn_low_glucose (if too low)
  - maintain (if stable)

### Run Tests
Create a virtual environment and install dependencies:
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest -v
