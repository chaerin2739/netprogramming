import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen()

def calculate_expression(expression):
    try:
        elements = expression.split()
        elements = [element.strip() for element in elements]

        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = round(num1 / num2, 1)

        return str(result)
    except:
        return "Invalid expression"

while True:
    conn, addr = s.accept()

    with conn:
        while True:
            data = conn.recv(1024)
            expression = data.decode()

            if expression.lower() == 'p':
                break

            result = calculate_expression(expression)
            conn.sendall(result.encode())

s.close()
