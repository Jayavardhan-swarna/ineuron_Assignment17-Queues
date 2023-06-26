from collections import deque

def countStudents(students, sandwiches):
    count = 0
    queue = deque(students)
    stack = []

    for sandwich in sandwiches:
        stack.append(sandwich)

    while queue:
        if queue[0] == stack[-1]:
            queue.popleft()
            stack.pop()
            count = 0  # Reset the count since a student was able to eat
        else:
            queue.append(queue.popleft())
            count += 1

        if count == len(students):
            return count

    return 0



print(countStudents([1, 1, 0, 0], [0, 1, 0, 1]))            # Output: 0
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))  # Output: 3
