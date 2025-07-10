import requests


def main():
    print("Hello from minime-llm!")
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos",
    )


if __name__ == "__main__":
    main()
