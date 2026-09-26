from ui.cli import Cli
from services.find_frequency import FrequencyFinder

def main():
    interface = Cli()
    finder = FrequencyFinder()

    source = interface.get_source()

    frequency = finder.find_frequency(source)

<<<<<<< HEAD
    interface.print_frequency(frequency)
    
    inverted = finder.inversefft(frequency)

=======
    interface.print_frequency(frequency[3])

    interface.show_plots(frequency[0], frequency[1], frequency[2])
>>>>>>> main

if __name__ == "__main__":
    main()
