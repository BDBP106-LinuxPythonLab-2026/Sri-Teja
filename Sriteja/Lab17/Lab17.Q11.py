def compute_stats(numbers):
    total = 0
    count = 0
    for n in numbers:
        total += n
        count += 1
    average = total / count
    return average

def normalize(numbers):
    avg = compute_stats(numbers)
    return [n / avg for n in numbers]

def process_dataset(dataset):
    results = {}
    for name, values in dataset.items():
        results[name] = normalize(values)
    return results

if __name__ == "__main__":
    data = {
        "sample_a": [10, 20, 30, 40],
        "sample_b": [5, 0, 5, 10],   # will cause a bug later
    }
    output = process_dataset(data)
    print(output)
