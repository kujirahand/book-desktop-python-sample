import os

if os.name == "nt":
    import xhtml2pdf.document
    import xhtml2pdf.files

    _temporary_files = []
    _original_named_temporary_file = (
        xhtml2pdf.files.tempfile.NamedTemporaryFile
    )
    _original_clean_files = xhtml2pdf.files.cleanFiles

    def named_temporary_file(*args, **kwargs):
        kwargs["delete"] = False
        file = _original_named_temporary_file(*args, **kwargs)
        _temporary_files.append(file.name)
        return file

    def clean_files():
        _original_clean_files()
        for name in _temporary_files:
            try:
                os.remove(name)
            except FileNotFoundError:
                pass
        _temporary_files.clear()

    xhtml2pdf.files.tempfile.NamedTemporaryFile = named_temporary_file
    xhtml2pdf.files.cleanFiles = clean_files
    xhtml2pdf.document.cleanFiles = clean_files
