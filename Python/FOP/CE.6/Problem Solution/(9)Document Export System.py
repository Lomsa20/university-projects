class DocumentEditor:
    def __init__(self, doc):
        self._doc = doc
    def export(self):
        raise NotImplementedError("Subclasses must override this method")
class PDF(DocumentEditor):
    def export(self):
        return"export as PDF"
class HTML(DocumentEditor):
    def export(self):
        return "export as HTML"
class WORD(DocumentEditor):
    def export(self):
        return "export as WORD"
exported = [PDF('ads'), HTML('dfg'), WORD('hgd')]
for d in exported:
    print(f"Exporting: {d.export()}")