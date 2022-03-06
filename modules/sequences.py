# This module holds basic sequence functions

import json
import os
import itertools

class Sequence:
    display_len = 10

    def __init__(self,n: int):
        self.cache_file = '../caches/sequences/'+self.name+'.json'
        self.read_cache()
        if len(self.seq) < n:
            self.extend_seq(n-len(self.seq))

    def reset(self):
        self.seq = self.starter_seq
        self.update_cache()

    def read_cache(self):
        # initilizes self.seq
        if os.path.exists(self.cache_file):
            with open(self.cache_file,'r') as cache:
                self.seq = json.load(cache)
        else:
            self.seq = self.starter_seq
            self.update_cache()
        
    def update_cache(self):
        with open(self.cache_file,'w') as cache:
            cache.write(json.dumps(self.seq))

    def __repr__(self):
        if len(self) < Sequence.display_len:
            return str(self.seq) 
        return str(self.seq[:Sequence.display_len])

    def __getitem__(self,index):
        length = len(self.seq)
        if index < length:
            return self.seq[index]
        else:
            self.extend_seq(index-length+1)
            return self.seq[index]

    def __len__(self):
        return len(self.seq)

    def display(self):
        print(self.seq)

    def nexts(self):
        return self.next_item_batch()

    def add_items(self):
        nxts = self.nexts()
        self.seq += nxts
        self.update_cache()
        return nxts

    def extend_seq(self,n: int):
        while n > 0:
            added = self.add_items()
            n -= len(added)
        return self

    def take_while(self,include_condition,last_index=200000) -> list:
        passing = []
        length = 0
        while length < last_index:
            new_item = self[length]
            if include_condition(new_item):
                passing.append(new_item)
                length += 1
            else:
                return passing
        raise Exception(f'Sequence {self.name} satisfies {include_condition} past {last_index=}')

    def take_while_lt(self,n: float,last_index=1000) -> list:
        return self.take_while(lambda x: x< n,last_index=last_index)
    def take_while_gt(self,n: float,last_index=1000) -> list:
        return self.take_while(lambda x: x> n,last_index=last_index)
    def take_while_le(self,n: float,last_index=1000) -> list:
        return self.take_while(lambda x: x<=n,last_index=last_index)
    def take_while_ge(self,n: float,last_index=1000) -> list:
        return self.take_while(lambda x: x>=n,last_index=last_index)

class Primes(Sequence):
    def __init__(self,n=1):
        self.name = 'primes'
        self.starter_seq = [2]
        super().__init__(n)
    def next_item(self):
        return self.next_item_batch[0]     
    def next_item_batch(self):
        current = self.seq[-1]
        primes = range(current,2*current+1)
        for p in self.seq:
            primes = [x for x in primes if x%p != 0]
        print(f'Adding primes between {primes[0]} and {primes[-1]}')
        return primes


class Fibonacci(Sequence):
    def __init__(self,n=2):
        self.name = 'Fibonacci'
        self.starter_seq = [1,1]
        super().__init__(n)
    def next_item_batch(self):
        return [self.seq[-2] + self.seq[-1]]

class Natural(Sequence):
    def __init__(self,n=1):
        self.name = 'Natural'
        self.starter_seq = [1]
        super().__init__(n)
    def next_item_batch(self):
        return [self.seq[-1]+1]
