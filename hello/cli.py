import argparse
import core



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("name", help="name for hello")
    args = parser.parse_args()

    core.say_hello(args.name)


if __name__ == "__main__":
    main()
