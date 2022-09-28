from abc import ABC, abstractmethod
from PIL import Image
from docx2pdf import convert as dc
from pdfy import Pdfy
from configparser import ConfigParser


class Converter(ABC):
    config = ConfigParser()
    config.read("config.ini")

    @abstractmethod
    def convert(self, input_file: str, output_file: str) -> None:
        pass


class ImageConverter(Converter):

    def convert(self, input_file: str, output_file: str) -> None:
        image = Image.open(input_file)
        image = image.convert(mode=self.config["image"]["mode"])
        image.save(output_file)


class DocxConverter(Converter):
    """Requires Microsoft Word installed on system."""

    def convert(self, input_file: str, output_file: str) -> None:
        dc(input_file, output_file)


class HtmlConverter(Converter):
    """Requires pdfy installed on system."""

    def convert(self, input_file: str, output_file: str) -> None:

        options = {"paperWidth": self.config.getfloat('html', 'paperWidth'),
                   "paperHeight": self.config.getfloat('html', 'paperHeight')}
        p = Pdfy()
        p.html_to_pdf(html_path=input_file,pdf_path=output_file, options=options)
