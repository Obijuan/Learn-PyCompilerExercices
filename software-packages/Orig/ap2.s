                                @ ap2.s
          .text                 @ start of read-only segment
          .global _start
_start:
          ldr r0,x              @ load r0 from x
          str r0, y             @ store r0 in y (does not work)
          mov r7, #1            @ mov 1 into r7
          svc 0                 @ terminate program

x:        .word 2               @ the variable x
y:        .word 0               @ the variable y
