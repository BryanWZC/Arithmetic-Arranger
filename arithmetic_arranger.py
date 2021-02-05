import re;

def arithmetic_arranger(problems, show_ans=False):
    # assign strings to be concatenated into the result str in the end
    left_str = ''
    right_str = ''
    dash_str = ''
    solve_str = ''

    # raise exception if there are more than 5 problems
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    for index, problem in enumerate(problems):
        # remove spaces from each problem string
        problem = re.sub(r'\s', '', problem)

        # if the operation has mult or div, raise Exception
        if re.search(r'[\*\/]', problem):
            return "Error: Operator must be '+' or '-'."

        # split the string into left operand, sign and right operand, and assign them accordingly
        split = re.split(r'([\+\-])', problem)

        left_operand = split[0];
        right_operand = split[2];
        sign = split[1];
        
        # raise exception if operand length is greater than 4
        if len(left_operand) > 4 or len(right_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # raise exception if operand has non-digits in them
        if re.search(r'\D', left_operand) or re.search(r'\D', right_operand):
            return 'Error: Numbers must only contain digits.'

        # solve the problem and convert to string
        solve = int(left_operand) + int(right_operand) if sign == '+' else int(left_operand) - int(right_operand)
        solve = str(solve)

        # find the max string length
        max_len = max([len(left_operand), len(right_operand)])
        
        # perform string manipulations based on max string length
        right_str += sign + ' ' + right_operand.rjust(max_len)
        left_str += left_operand.rjust(max_len + 2)
        dash_str += ''.rjust(max_len + 2, '-')
        solve_str += solve.rjust(max_len + 2)
        
        # add a padding for the next operation if not the last index
        if(index < len(problems) - 1):
            left_str += ''.rjust(4)
            right_str += ''.rjust(4)
            dash_str += ''.rjust(4)
            solve_str += ''.rjust(4)

    # if option to show answer is True, show answer
    if show_ans:
        return left_str + '\n' + right_str  + '\n' + dash_str  + '\n' + solve_str

    return left_str + '\n' + right_str  + '\n' + dash_str