import math

def approximation_method(sizes, weights, k):

    if not sizes or not weights or len(sizes) != len(weights):
        return "Error: Invalid input parameters"
    
    # Convert all sizes to decimal fractions if provided as strings like '1/3'
    processed_sizes = []
    for size in sizes:
        if isinstance(size, str) and '/' in size:
            num, denom = size.split('/')
            processed_sizes.append(float(num) / float(denom))
        else:
            processed_sizes.append(float(size))
    
    # Find the shallowest branch (largest subproblem size)
    shallowest_size = max(processed_sizes)
    shallowest_index = processed_sizes.index(shallowest_size)
    shallowest_weight = weights[shallowest_index]
    
    # Find the deepest branch (smallest subproblem size)
    deepest_size = min(processed_sizes)
    deepest_index = processed_sizes.index(deepest_size)
    deepest_weight = weights[deepest_index]
    
    # Calculate the depth for each branch
    shallowest_depth = math.ceil(math.log(1/shallowest_size, 1/shallowest_size))
    deepest_depth = math.ceil(math.log(1/deepest_size, 1/deepest_size))
    
    # Calculate the approximate complexity based on depth and work per level
    # Shallowest branch (lower bound)
    lower_bound = ""
    # Deepest branch (upper bound)
    upper_bound = ""
    
    # Determine complexity based on branch depth and combine step
    if k == 0:  # Constant work per level
        lower_bound = f"Ω(log n)"
        upper_bound = f"O(log n)"
    elif k == 1:  # Linear work per level
        lower_bound = f"Ω(n)"
        upper_bound = f"O(n log n)"
    else:  # Polynomial work per level
        lower_bound = f"Ω(n^{k})"
        upper_bound = f"O(n^{k} log n)"
    
    explanation = (
        f"Lower bound from shallowest branch (size factor: {shallowest_size}): {lower_bound}\n"
        f"Upper bound from deepest branch (size factor: {deepest_size}): {upper_bound}"
    )
    
    return lower_bound, upper_bound, explanation


def print_approximation_method_result(sizes, weights, k):

    lower_bound, upper_bound, explanation = approximation_method(sizes, weights, k)
    
    # Print the recurrence relation
    recurrence = "T(n) = "
    for i in range(len(sizes)):
        if i > 0:
            recurrence += "+ "
        if weights[i] != 1:
            recurrence += f"{weights[i]}"
        
        # Format the size as fraction if its a string fraction
        if isinstance(sizes[i], str) and '/' in sizes[i]:
            recurrence += f"T(n/{sizes[i].split('/')[1]}) "
        else:
            denom = int(1/float(sizes[i])) if float(sizes[i]) != 0 else 0
            recurrence += f"T(n/{denom}) "
    
    recurrence += f"+ Θ(n^{k})"
    
    print(f"Recurrence relation: {recurrence}")
    print(f"Approximate bounds:")
    print(explanation)
    print(f"Time complexity: {lower_bound} to {upper_bound}")
    print("Note: This is an approximation based on the depth of recursion trees on the shallowest and deepest branches.")