b *0x401469
b *0x401537
b *0x401556

run

set {long}($rbp-0x120) = 30
set {long}($rbp-0x118) = 0

continue

set $a = *(int*)($rbp - 0x144)
set $b = *(int*)($rbp - 0x140)
set $correct = $a + $b
set {int}($rbp - 0x124) = $correct

b *0x401556
continue

