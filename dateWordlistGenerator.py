import click
import time
from datetime import date
from datetime import timedelta
from progress.bar import ChargingBar as Bar

@click.command()
@click.option('--start', default=1900, help='Start year.')
@click.option('--end', default=2040, help='End year.')
@click.option('--output', default='output.txt', help='Define output file.')
@click.option('--separator', default='', help='Separator character.')

def generate(start, end, output, separator):
    """Dator - Simple Date Generator program that generate wordlist from date."""

    one_day = timedelta(days=1)
    start_date = date(start, 1, 1)
    end_date = date(end + 1, 1, 1)
    total_days = abs(end_date - start_date)

    with Bar('Generating new wordlist', max=total_days.days) as bar:
        with open(output, 'w') as the_file:
            for x in range(total_days.days):
                temp_date = start_date + (x * one_day)
                the_file.write(temp_date.strftime('%d' + separator + '%m' + separator + '%Y\n'))
                bar.next()
            the_file.close()
            
if __name__ == '__main__':
    generate()
