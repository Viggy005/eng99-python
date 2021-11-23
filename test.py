def is_prime(integer):
    if integer >= 2:
        for x in range(2, integer):
            if integer % x == 0:
                return False
            else:
                return True
    else:
        return False
print(is_prime(6545))