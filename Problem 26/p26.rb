
def reciprocal_cycles (d)
    primes = getPrimes(d)
    primes.reject! {|k| k == 2 || k == 5}
    
    maxRepeatingLength = 0
    maxRepeatingDivisor = 0

    primeIndex = primes.length-1

    while (primeIndex >= 0)
        prime = primes[primeIndex]
        nineLevel = 9
        counter = 1
        while (nineLevel % prime != 0)
            nineLevel = nineLevel*9+9
            counter +=1
        end
        if (counter == prime-1)
            p "used this"
            return prime
        elsif (counter > maxRepeatingLength)
            maxRepeatingLength = counter
            maxRepeatingDivisor = prime
            p [maxRepeatingDivisor, maxRepeatingLength]
        end
        primeIndex -= 1
    end
    maxRepeatingDivisor
end

def getPrimes(d)
    primes = []
    array = Array.new(d, false)
    currDivisor = 2    
    while (currDivisor < d)
        if !array[currDivisor]
            primes << currDivisor
            counter = currDivisor*2
            while (counter < d)
                array[counter] = true
                counter += currDivisor
            end
        end
        currDivisor += 1
    end
    primes
end

p reciprocal_cycles(8000)