# UC-XXXX-XXXX · FastAPI PoC

PoC for UC-XXXX-XXXX · PLANT · process — proof-of-concept, not production data.

Structure follows FastAPI's [Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/) layout (`app/` package, typed models).

```bash
cd poc
pip install -r requirements.txt
uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
pytest                          # smoke tests
```
