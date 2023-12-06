class Stack:
    def __init__(self, size):
        self.size = size
        self.remain = size
        self.filled = 0

    def is_empty(self):
        return self.remain == self.size

    def push(self):
        if self.remain == 0:
            return 1
        self.filled += 1
        self.remain -= 1
        return 0

    def pop(self):
        if self.remain == self.size:
            return 1
        self.filled -= 1
        self.remain += 1
        return 0


def get_correct_bracket_sequence(stack_first, stack_second, string, open, max_len):
    for v in "([)]":
        if v == '(':
            string += v
            if stack_second.remain == 0 or stack_first.push() == 1:
                string = string[:-1]
                continue
            if len(string) == max_len or len(string) + stack_first.filled + stack_second.filled > max_len:
                stack_first.pop()
                string = string[:-1]
                continue
            open += v
            get_correct_bracket_sequence(stack_first, stack_second, string, open, max_len)
            open = open[:-1]
            string = string[:-1]
            stack_first.pop()
        elif v == '[':
            string += v
            if stack_first.remain == 0 or stack_second.push() == 1:
                string = string[:-1]
                continue
            if len(string) == max_len or len(string) + stack_first.filled + stack_second.filled > max_len:
                stack_second.pop()
                string = string[:-1]
                continue
            open += v
            get_correct_bracket_sequence(stack_first, stack_second, string, open, max_len)
            open = open[:-1]
            string = string[:-1]
            stack_second.pop()
        elif v == ')':
            if len(open) < 1 or open[-1] == '[':
                continue
            string += v
            if stack_second.remain == 0 or stack_first.pop() == 1:
                string = string[:-1]
                continue
            if string[-2] == '[' or len(string) + stack_first.filled + stack_second.filled > max_len:
                string = string[:-1]
                stack_first.push()
                continue
            if len(string) == max_len:
                if stack_first.is_empty() and stack_second.is_empty():
                    print(string)
                    stack_first.push()
                    return
            tmp = open[-1]
            open = open[:-1]
            get_correct_bracket_sequence(stack_first, stack_second, string, open, max_len)
            open += tmp
            string = string[:-1]
            stack_first.push()
        elif v == ']':
            if len(open) < 1 or open[-1] == '(':
                continue
            string += v
            if stack_first.remain == 0 or stack_second.pop() == 1:
                string = string[:-1]
                continue
            if string[-2] == '(' or len(string) + stack_first.filled + stack_second.filled > max_len:
                string = string[:-1]
                stack_second.push()
                continue
            if len(string) == max_len:
                if stack_first.is_empty() and stack_second.is_empty():
                    print(string)
                    stack_second.push()
                    return
            tmp = open[-1]
            open = open[:-1]
            get_correct_bracket_sequence(stack_first, stack_second, string, open, max_len)
            open += tmp
            string = string[:-1]
            stack_second.push()


input_len = int(input())
ans = []
if input_len % 2 == 0:
    first_stack = Stack(input_len // 2)
    second_stack = Stack(input_len // 2)
    get_correct_bracket_sequence(first_stack, second_stack, "", "", input_len)
