import subprocess


def process_words(words):

    print("Вхідні дані:")
    print(words)
    print("-" * 30)

 
    p1 = subprocess.Popen(
        ["echo", words],
        stdout=subprocess.PIPE,
        text=True
    )

 
    p2 = subprocess.Popen(
        ["tr", " ", "\n"],
        stdin=p1.stdout,
        stdout=subprocess.PIPE,
        text=True
    )

    p3 = subprocess.Popen(
        ["sort"],
        stdin=p2.stdout,
        stdout=subprocess.PIPE,
        text=True
    )

 
    p4 = subprocess.Popen(
        ["uniq", "-c"],
        stdin=p3.stdout,
        stdout=subprocess.PIPE,
        text=True
    )

    output, _ = p4.communicate()

    return output


def main():
  
    words = "apple banana apple orange banana apple kiwi apple banana"

    result = process_words(words)

    print("Результат обробки:")
    print(result)


if __name__ == "__main__":
    main()
