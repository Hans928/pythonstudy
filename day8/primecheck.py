def prime_checker(number):
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
    
    if is_prime == True:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")
        
    
    
n = int(input("소수인지 확인하고 싶은 숫자를 넣어주세요! "))
prime_checker(number=n)