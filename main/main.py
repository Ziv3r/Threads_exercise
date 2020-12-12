from analyzer import Analyzer


class Main:
    @staticmethod
    def main():
        analyzer = Analyzer("http://norvig.com/big.txt", 1000, 5)
        analyzer.analyze()


m = Main()
m.main()
