import sys
import model
import os
from pyjon.reports import ReportFactory
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('hei', 'SIMHEI.TTF'))
from geraldo import Report, ReportBand, DetailBand, SystemField, Label, ObjectValue,SubReport
from geraldo.utils import cm, BAND_WIDTH, TA_CENTER, TA_RIGHT
def report1():
    class MyFamilyReport(Report):
        title = 'NCS_CS'

        class band_detail(DetailBand):
            height = 0.7*cm
            elements = [
                ObjectValue(expression='name', left=0.5*cm),
                ObjectValue(expression='c', left=3.5*cm,get_value=lambda instance: "%.5f" % instance.c),
                ObjectValue(expression='s', left=6.5*cm,get_value=lambda instance: "%.5f" % instance.s),
                ObjectValue(expression='user', left=9.5*cm),
                ObjectValue(expression='mdate', left=12.5*cm),
            ]
            borders = {'bottom': True}

        class band_page_header(ReportBand):
            height = 1.3*cm
            elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                Label(text="Name", top=0.8*cm, left=0.5*cm),
                Label(text="c", top=0.8*cm, left=3.5*cm),
                Label(text="s", top=0.8*cm, left=6.5*cm),
                Label(text="user", top=0.8*cm, left=9.5*cm),
                Label(text="time", top=0.8*cm, left=12.5*cm),
            ]
            borders = {'all': True}

        class band_page_footer(ReportBand):
            height = 0.5*cm
            elements = [
                Label(text='Geraldo Reports', top=0.1*cm),
                SystemField(expression='Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
            borders = {'top': True}
    from geraldo.generators import PDFGenerator
    my_report = MyFamilyReport(queryset=model.getAves())
    my_report.generate_by(PDFGenerator, filename='gen_aves.pdf')
def report2():    
    class MyFamilyReport(Report):
        title = 'NCS_CS'

        class band_detail(DetailBand):
            height = 0.7*cm
            elements = [
                ObjectValue(expression='name', left=0.5*cm),
                ObjectValue(expression='c', left=3.5*cm,get_value=lambda instance: "%.5f" % instance.c),
                ObjectValue(expression='s', left=6.5*cm,get_value=lambda instance: "%.5f" % instance.s),
                ObjectValue(expression='user', left=9.5*cm),
                ObjectValue(expression='mdate', left=12.5*cm),
            ]
            borders = {'top': True,'bottom':.3}

        class band_page_header(ReportBand):
            height = 1.3*cm
            elements = [
                SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                    style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
                SystemField(expression=u'Page %(page_number)d of %(page_count)d', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                Label(text="Name", top=0.8*cm, left=0.5*cm),
                Label(text="c", top=0.8*cm, left=3.5*cm),
                Label(text="s", top=0.8*cm, left=6.5*cm),
                Label(text="user", top=0.8*cm, left=9.5*cm),
                Label(text="time", top=0.8*cm, left=12.5*cm),
            ]
            #borders = {'all': True}

        class band_page_footer(ReportBand):
            height = 0.5*cm
            elements = [
                Label(text='Geraldo Reports', top=0.1*cm),
                SystemField(expression='Printed in %(now:%Y, %b %d)s at %(now:%H:%M)s', top=0.1*cm,
                    width=BAND_WIDTH, style={'alignment': TA_RIGHT}),
                ]
            borders = {'top': True}
        subreports = [
            SubReport(
                queryset_string = '%(object)s.singles',
                # band_header = ReportBand(
                        # height=0.9*cm,
                        # elements=[
                            # Label(text='id', top=0.2*cm, left=0.2*cm, style={'fontName': 'Helvetica-Bold'}),
                            # Label(text='name', top=0.2*cm, left=4*cm, style={'fontName': 'Helvetica-Bold'}),
                        # ],
                    # ),
                band_detail = ReportBand(
                        height=0.5*cm,

                        # This is a new attribute to force the band width
                        # width = 6*cm,

                        # # This attribute forces a distance at right and bottom sides of the band
                        # margin_right = 0.2*cm,
                        # margin_bottom = 0.2*cm,

                        # # With this attribute as True, the band will try to align in
                        # # the same line
                        # display_inline = True,

                        elements=[
                            ObjectValue(attribute_name='c',  left=3.5*cm,get_value=lambda instance: "%.5f" % instance.c),
                            ObjectValue(attribute_name='s', left=6.5*cm,get_value=lambda instance: "%.5f" % instance.s),
                        ],
                        #borders={'all': True},
                    ),
                # band_footer = ReportBand(
                        # height=0.9*cm,
                        # elements=[
                            # ObjectValue(attribute_name='id', top=0.2*cm, left=4*cm,\
                                # action=FIELD_ACTION_COUNT, display_format='%s permissions found',
                                # style={'fontName': 'Helvetica-Bold'}),
                        # ],
                    # ),
            ),
        ]
    from geraldo.generators import PDFGenerator
    my_report = MyFamilyReport(queryset=model.getAves())
    my_report.generate_by(PDFGenerator, filename='gen_aves.pdf')
if __name__=="__main__":    
    report2()        

    