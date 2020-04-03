from random import randrange
import sys

begin_number = sys.argv[1]
end_number = sys.argv[2]

random_number = randrange(int(begin_number), int(end_number), 1)

print(random_number)
