# Estate Site

A Lagos home search, written in Python (Flask). Listings are samples.

## Open in VS Code

1. Unzip this folder.
2. In VS Code choose **File → Open Folder** and select this folder.
3. Open the terminal and run:

```bash
python -m pip install -r requirements.txt
python app.py
```

4. Open http://127.0.0.1:5000

You can also press **Run and Debug** and choose **Estate Site** if the Python extension is installed.

## Edit

- Homes: `listings.py`
- WhatsApp, email, and phone: `CONTACT` at the top of `app.py`
- Pages: `templates/`
- Look: `static/site.css`

Photos live in `static/photos/`. The map uses OpenStreetMap and needs an internet connection.
