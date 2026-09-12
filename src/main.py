from ui.cli import Cli
from services.find_frequency import FrequencyFinder


def main():
    interface = Cli()
    finder = FrequencyFinder()

    source = interface.get_source()

    frequency = finder.find_frequency(source)

    interface.print_frequency(frequency)
    
if __name__ == "__main__":
    main()