import solve

def main():
    with open("./input", "r") as input_file:
        result = solve.solve_file(input_file)
        print(result)

if __name__ == "__main__":
    main()
