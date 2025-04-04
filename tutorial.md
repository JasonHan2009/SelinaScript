# SelinaScript Syntax Tutorial

This tutorial will walk you through the basics of SelinaScript syntax.


## preface

Please see selina_script.md

## Basic Syntax

In SelinaScript, we have these keywords:

```
Int Float >> <<>> | _
|* loop cond like -> next_cond cond_fin List extends .inc, unsafe safe ret 
```

## Example:
```
>> HelloWorld | ECHO A 'HELLO WORLD'
```

SelinaScript is not force the line indent, But we recommend you to use 4 spaces to indent to keep the code readable.

## DataType

In SelinaScript, we only have four types 

all of the types are being used to math logic operation

For example:
```
| This code's print is 3
| not '12'
>> Int 1 + '2'

| When just a single char but use integer Type:
>> Int '1' | it will be print the ascii code

>> Int 'Hello! SelinaScript' | it will print the sum of the ASCII codes

| When just a single char but use float Type:
>> Float '1' | it will be print the ascii code's float value

>> Float 'Hello! SelinaScript' | it will print the sum of the ASCII codes' float value

>> _ | it couldn't be print the value
```

In SelinaScript, we use ```0``` and ```1``` to declare the ```boolean``` value and use ```''``` to declare ```char```, use ```""``` to declare ```string```, use ```_``` to declare ```null```

when you not declare the type, but you ```number``` meets a ```string```, SelinaScript will auto translate the ```number``` to ```string```, you can use 
``` list ``` to declare the ```list```

for example:
```     
| it will be print '12'
>> "1" + 2
| error example:
>> '1' + 2
```

## Declare Variable And Function

in SelinaScripts, when you declare a function, you must with ```Variables```, ```idependent variables```, ```constants``` these args, if you want without, you mus t input ```_``` into your args

for example:
```
| declare a function
function_name = (x, y, z)->
>>     x + y + z
| without args
function_name = (_)->
>> with out args
```

when you want to declare a 
inline function, you can do this
for example:
```
| declare a function

function_name = (x, y, z)->

|* use extends to extends parent function's parameters*|
|* the inline function will be auto execute *|

    f(extends: x, y, z) ->
        >>  x + y + z

| without args

function_name = (_)->
    f(_) ->
        >> 'Hello SelinaScript!'

| and you can declare function with a type

function_name = (_)-> _
    f(_) -> _ | Not return any value
        >> 'Hello SelinaScript!'
```

you can declare a variableds with type or without type

for example:
```
| without type
a = 10
| with type
_ a = 0 | the value its None, this given value is unrechable
Int a = 10
Float j = 10
```

## Bitwise Operation

in SelinaScript, we must use ```<<>>``` to declare the bitwise operation

for example:
```
| when we want to shift left 1 bit
>>  1 << 12 >> _ | Do not shift right declare

| when we want to shift right 1 bit
>>  _ >> 12 >> 1 

| when we want to shift left 1 bit then shift right 1 bit
>>  1 << 12 >> 1

| if we dont input any value, SelinaScript will get the value's last bit
>> << 12 >>
```

## If Loop

In archeimedes, we can use ``` loop ``` to declare the loop, use ``` cond ``` to declare the condition, if you want to detect more condition branch, you can use ```next_cond```, and you can use ```cond_fin``` to declare the end of the condition    

for example:
```
a -> Int = 10

cond a == 10 ->
    >> 'a is ' + 10 
next_cond a !== 10 ->
    >> 'a is not ' + 10
cond_fin
```

in Archemides, we have many methods to declare a ```loop```

for example:

```
| While loop:

loop 1 ->
    >> 'Hello Archemides'

| Three expressions loop:
loop i = 0 -> i < 10 -> i++ -> 
    >> i

| foreach

list i = 0, 1, 2, 3, 4
loop j -> i:
>> j
```

## Unsafe Operation And Safe operation

in SelinaScript, we have two pointer operation, ```unsafe``` and ```safe```
you can use ```unsafe``` pointer to improve your application's performance, but you must be careful, it's not a safe operation, if you want more safety, you can use ```safe``` pointer, the safe pointer will be auto check the pointer's value, and make sure the pointer's value is not ```None``` or will happend ```wild pointers```

you can use the number index to visit the pointer's value, and you can use %addr to get the pointer's address

for example:
```
| unsafe pointer
unsafe a = () ->
    ret 10 | this value will be store in to the pointer

>> a()[0] 
>> %addr a() 
| safe pointer
safe b = () ->
    ret 10

>> b()[0]
>> %addr b()

| variable

_ a = _ | Initialize a memory segment
unsafe a[0] = 10 | Store the value

>> a[0]
>> %addr a
```

## Like and .inc

use ```.inc``` to include a file and use ```like``` to use the special name to use the file's function

for example:
```
| a.selina
test = () -> _ 
>> "Hello world"
| b.selina
.inc a.selina like a
a.test()
```