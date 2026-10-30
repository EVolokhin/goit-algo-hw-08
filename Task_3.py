import heapq  # Мінімальна купа дозволяє швидко діставати два найкоротші кабелі.


def min_connection_cost(cables):
    if any(length < 0 for length in cables):
        raise ValueError("Довжини кабелів не можуть бути від'ємними")


    heap = list(cables)
    # heapify перетворює копію на мінімальну купу: найменший елемент
    # завжди можна отримати через heappop.
    heapq.heapify(heap)
    total_cost = 0  # Сума вартостей усіх виконаних з'єднань.
    connections = []  # Порядок з'єднань для відображення результату.

    # Поки кабелів більше одного ми можего їх поєднати.
    while len(heap) > 1:
        #heappop дістає найменший елемент з купи і видаляє його.
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = first + second  # Довжина нового кабелю і ціна цього кроку.

        connections.append((first, second, combined))
        total_cost += combined  # оновлюємо загальні витрати додаючи нову вартість.
        heapq.heappush(heap, combined)  # Новий кабель додаємо до купи.

    return total_cost, connections


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    cost, steps = min_connection_cost(cables)

    for first, second, combined in steps:
        print(f"{first} + {second} = {combined}")
    print(f"Мінімальні загальні витрати: {cost}")
