import click
import resizer as rs
from pypdf import PdfReader as pdfr
from pypdf import PdfWriter as pdwr
v='*******777777******7777777***********7777777*****777777*****7777777******\n'+'*******7****777******77**************77***77****7****777***77************\n'+'*******7****77******77**************777777*****7****77****77777**********\n'+'*******7***77******77**************77*********7***77*****77**************\n'+'*******7777*****7777777***********77*********77777******77***************'
func_names=['redd','help']
def redd(args,filepath1,filepath2):
    assert args in ['-0','-1']
    assert filepath1[-4:]=='.pdf'
    assert filepath2[-4:]=='.pdf'
    if  args=='-0':
        writer=rs.resize_without_loss(filepath1)
        with open(filepath2,"wb") as f:
            writer.write(f)
    if args=='-1':
        writer=rs.resize_with_loss_of_qimage(filepath1)
        with open(filepath2,"wb") as f:
            writer.write(f)
    return 0
def help():
    size='SIZE REDUCTION:\n'+'to reduce size of pdf without loss use : redd <argument> [filepath1] [filepath1]\n'+  'arguments: -0     without loss of quality\n'+' '*9+'  -1     with loss of image  quality'
    click.secho(size,fg='bright_blue')

def hello():
    '''dissect pdf on your local machone'''
    a=''
    for x in v:
        if x=="*":
            a+=click.style(x,bold=True,fg='magenta')
        else:
            a+=click.style(x,bold=True,fg='bright_green')
    click.echo(a)
    click.secho('-'*31+'DISSECT PDF'+'-'*31,fg='bright_blue')
def run():
    while True:
        cinn=click.prompt(click.style('>>>>',italic=True,fg='green'))
        if cinn=='exit':
            break
        else:
            try:
                cinn=cinn.split()
                click.secho(str(cinn),fg='red',bold=True)
                assert cinn[0] in func_names
                globals()[cinn[0]](*cinn[1:])
                click.secho('SUCCESS',fg='red',bold=True)
            except Exception as ex :
                click.secho(ex,fg='bright_red')
                click.secho('I did not understand your request please type <help> for info',fg='bright_red')
def main():
    hello()
    run()
if __name__=='__main__':
    main()