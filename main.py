from converter import Converter, ImageConverter, DocxConverter, HtmlConverter


class PDFProcessor:
    def __init__(self, input_file: str, output_file: str, converter: Converter):

        self.input_file = input_file
        self.output_file = output_file
        self.converter = converter()

    def convert(self):
        self.converter.convert(self.input_file, self.output_file)


if __name__ == '__main__':
    input_file = "C:\\Users\\aahmed\\IdeaProjects\\pdf-utility\\sample\\sample_image.jpg"
    output_file = input_file + '.pdf'

    ps = PDFProcessor(input_file, output_file, ImageConverter)
    ps.convert()

    input_file =  "C:\\Users\\aahmed\\IdeaProjects\\pdf-utility\\sample\\sample_document.docx"
    output_file = input_file + '.pdf'

    ps = PDFProcessor(input_file, output_file, DocxConverter)
    ps.convert()

    input_file =  "C:\\Users\\aahmed\\IdeaProjects\\pdf-utility\\sample\\sample_webpage.html"
    output_file = input_file + '.pdf'

    ps = PDFProcessor(input_file, output_file, HtmlConverter)
    ps.convert()