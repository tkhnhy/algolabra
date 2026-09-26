from ui.cli import Cli
from services.find_frequency import FrequencyFinder

def main():
    interface = Cli()


    source = interface.get_source()
    finder = FrequencyFinder(source)

    frequency = finder.find_frequency()

    # 0 -original_data, 1 - transformed, 2 - sample_rate, 3 - peak_frequency
    interface.print_frequency(frequency[3])

    interface.show_plots(frequency[0], frequency[1], frequency[2])

    finder.invert_and_write(frequency[1])
    interface.print_written()
if __name__ == "__main__":
    main()
