shiftl
array [39, 91, 124, 92, 61, 51, 7, 105, 122, 106, 19, 41, 56, 75, 83, 132, 6, -35, 14, 105, 5, 106, 24, 37, 29, 78, 22]
shiftr

push 57
autokey_start: xor
dup
movr
peek
push 1
sub
jnz autokey_start
jnz autokey_cleanup # pops the remaining element=

funny: push 43
xor
push 5
add
jump funny_ret

autokey_cleanup: shiftr
jump transpose_pt1_start

transpose_pt1_cleanup: shiftl
transpose_pt2_start: movr
shiftr
push 24
sub
shiftr
shiftr
push 3
add
movl
shiftl
movl
movl
shiftl
shiftl
peek
jnz transpose_pt2_start

shiftr
funny_loop_start: jump funny
funny_ret: movl
peek
jnz funny_loop_start

push 0
shiftl
check_loop_start: movl
shiftl
sub
movr
shiftr
movr
shiftr
xor
shiftl
peek
jnz check_loop_start
shiftr
jump end

transpose_pt1_start: movl
movr
movr
shiftr
movr
shiftl
peek
jnz transpose_pt1_start
jump transpose_pt1_cleanup

end: movl
shiftl
movl
shiftl