                                @ ap3.s
          .text                 @ start of read-only segment
          .global _start
                                @                  address
f:        mov r0, #3            @ mov 77 into r0    8000
          mov pc, lr            @ return to caller  8004

_start:   bl  f                 @ call f            8008
          mov r7, #1            @ mov 1 into r7     8012
          svc 0                 @ terminate program 8016
